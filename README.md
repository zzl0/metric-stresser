# Metric Stresser

A graphite metric stresser, this is inspired by [graphite-stresser](https://github.com/feangulo/graphite-stresser),
which is a Java program, and can only test line format. I want to test pickle easily.

# Usage

    $ python mstresser.py -h
    usage: mstresser.py [-h] [-a ADDRESS] [-f {line,pickle}] [-p PROCESS]
                        [-m METRIC] [-i INTERVAL] [-d]

    optional arguments:
      -h, --help            show this help message and exit
      -a ADDRESS, --address ADDRESS
                            host:port pair.
      -f {line,pickle}, --format {line,pickle}
                            Format of data.
      -p PROCESS, --process PROCESS
                            Number of metrics for one process.
      -m METRIC, --metric METRIC
                            Number of metrics.
      -i INTERVAL, --interval INTERVAL
                            Publish time interval.
      -d, --debug           Debug mode, send the metrics to terminal.


The following command will generate 100 processes, each process will have 2 metrics.

    $ python mstresser.py -a localhost:2004 -f pickle -p 2 -m 2 -i 1 -d
    ('stresser.process_1.metric_id.0.metric_test', (1440571797, 0.15515189562009912))
    ('stresser.process_1.metric_id.1.metric_test', (1440571797, 1.155151895620099))
    ('stresser.process_0.metric_id.0.metric_test', (1440571798, 0.6304694904611914))
    ('stresser.process_0.metric_id.1.metric_test', (1440571798, 1.6304694904611914))
    ('stresser.process_1.metric_id.0.metric_test', (1440571798, 0.4246871048425469))
    ('stresser.process_1.metric_id.1.metric_test', (1440571798, 1.424687104842547))
    ('stresser.process_0.metric_id.0.metric_test', (1440571799, 0.22902973694517137))
    ('stresser.process_0.metric_id.1.metric_test', (1440571799, 1.2290297369451713))
