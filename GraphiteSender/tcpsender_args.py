# -*- coding: utf-8 -*-
import argparse
from  common import timer_dec


@timer_dec
def get_args(log):
    program = {'version': '1.0.0', 'modify_date': '03.04.2014'}

    parser = argparse.ArgumentParser(description='%(prog)s, version - ' + program["version"],
                                     prog='TCPSender', epilog="Good luck!")

    parser.add_argument("--addr", '-a', type=str, required=True, dest='address',
                        help="Destination IP address", metavar='0.0.0.0')
    parser.add_argument("--port", '-p', type=str, required=True, dest='port',
                        help="TCP port", metavar='0')

    parser.add_argument("--metric", '-m', type=str, required=True, dest='metric',
                        help="Metric for sent in Graphite via TCP", metavar='"your metric here"')

    parser.add_argument("--value", '-v', type=int, required=True, dest='value',
                        help="Value for sent in Graphite via TCP", metavar='123')

    args = vars(parser.parse_args())
    log.info('Args - {}'.format(args))

    return args
