# coding: utf-8
import os
import time
import random
import socket
import struct
import cPickle as pickle
from multiprocessing import Process


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", type=str, help="host:port pair.")
    parser.add_argument("-f", "--format", type=str, choices=["line", "pickle"], help="Format of data.")
    parser.add_argument("-p", "--process", type=int, default=1, help="Number of processes.")
    parser.add_argument("-m", "--metric", type=int, default=1000, help="Number of metrics for one process.")
    parser.add_argument("-i", "--interval", type=int, default=10, help="Publish time interval.")
    parser.add_argument("-d", "--debug", action='store_true', help="Debug mode, send the metrics to terminal.")
    args = parser.parse_args()

    stresser(args)


def stresser(args):
    host, port = args.address.split(":")
    port = int(port)
    metric_args = (host, port, args.format, args.metric, args.interval, args.debug)

    processes = []
    for _ in xrange(args.process):
        p = Process(target=send_metrics, args=metric_args)
        p.start()
        processes.append(p)

    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        print 'KeyboardInterrupt'


def send_metrics(host, port, format, num_metrics, interval, debug):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except socket.error:
        raise SystemError("Couldn't connect to %s on port %s" %
                          (host, port))
    process_id = os.getpid()
    metrics = list(gen_metrics(process_id, num_metrics))
    while True:
        points = gen_metric_points(metrics, format)
        if debug:
            print '\n'.join(map(str, points))
        else:
            if format == 'line':
                msg = '\n'.join(points) + '\n'  # all lines end in a newline
                sock.sendall(msg)
            else:
                # pickle
                package = pickle.dumps(points, 1)
                size = struct.pack('!L', len(package))
                sock.sendall(size)
                sock.sendall(package)
        time.sleep(interval)


def gen_metrics(id_, num_metrics):
    METRIC_PATTERN = 'stresser.process_id.{0}.metric_id.%s.metric_test'.format(id_)
    for i in xrange(num_metrics):
        yield METRIC_PATTERN % str(i)


def gen_metric_points(metrics, format):
    val = random.random()
    now = int(time.time())
    if format == 'line':
        r = ['%s %s %s' % (m, val, now) for m in metrics]
    else:
        # pickle
        r = [(m, (now, val)) for m in metrics]
    return r


if __name__ == '__main__':
    main()
