# Metric Stresser

A graphite metric stresser, this is inspired by [graphite-stresser](https://github.com/feangulo/graphite-stresser),
which is a Java program, and can only test line format. I want test pickle easily.

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
    ('stresser.process_id.39825.metric_id.0.metric_test', (1440136188, 0.9146787869698118))
    ('stresser.process_id.39825.metric_id.1.metric_test', (1440136188, 0.9146787869698118))
    ('stresser.process_id.39826.metric_id.0.metric_test', (1440136188, 0.006932140572044498))
    ('stresser.process_id.39826.metric_id.1.metric_test', (1440136188, 0.006932140572044498))
    ('stresser.process_id.39826.metric_id.0.metric_test', (1440136189, 0.8385083474955232))
    ('stresser.process_id.39826.metric_id.1.metric_test', (1440136189, 0.8385083474955232))
    ('stresser.process_id.39825.metric_id.0.metric_test', (1440136189, 0.10841156575128208))
    ('stresser.process_id.39825.metric_id.1.metric_test', (1440136189, 0.10841156575128208))
    ('stresser.process_id.39826.metric_id.0.metric_test', (1440136190, 0.04381879697428048))
    ('stresser.process_id.39826.metric_id.1.metric_test', (1440136190, 0.04381879697428048))
    ('stresser.process_id.39825.metric_id.0.metric_test', (1440136190, 0.8571470994720299))
    ('stresser.process_id.39825.metric_id.1.metric_test', (1440136190, 0.8571470994720299))
    ('stresser.process_id.39826.metric_id.0.metric_test', (1440136191, 0.3451892571886054))
    ('stresser.process_id.39825.metric_id.0.metric_test', (1440136191, 0.21581244636910735))
    ('stresser.process_id.39825.metric_id.1.metric_test', (1440136191, 0.21581244636910735))
    ('stresser.process_id.39826.metric_id.1.metric_test', (1440136191, 0.3451892571886054))
