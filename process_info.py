import time
import socket
import psutil
import struct

try:
    import cPickle as pickle
except:
    import pickle


METRIC_PATTERN = "monitor.carbon.process_id.%d"


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--addr", help="hort:port of carbon server (use pickle port).")
    parser.add_argument("-i", "--interval", type=int, default=10, help="Publish time interval.")
    parser.add_argument("pids", metavar="N", type=int, nargs="+",
                        help="process id.")
    args = parser.parse_args()

    host, port = args.addr.split(":")
    sock = socket.socket()
    try:
        sock.connect((host, int(port)))
    except socket.error:
        raise SystemError("Couldn't connect to %s on port %s" %
                          (host, port))

    pids = set(args.pids)
    while True:
        metrics = process_info(pids)
        print metrics
        send_graphite(sock, metrics)
        time.sleep(args.interval)


def process_info(pids):
    now = int(time.time())
    metrics = []
    for p in psutil.get_process_list():
        try:
            if p.pid in pids:
                pid, cpu = p.pid, p.get_cpu_percent()
                datapoint = (METRIC_PATTERN % pid, (now, cpu))
                metrics.append(datapoint)
        except psutil.NoSuchProcess:
            pass
    return metrics


def send_graphite(sock, metrics):
    package = pickle.dumps(metrics, 1)
    size = struct.pack('!L', len(package))
    sock.sendall(size)
    sock.sendall(package)


if __name__ == '__main__':
    main()
