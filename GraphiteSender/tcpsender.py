import socket
import time
from  common import timer_dec


@timer_dec
def tcp_sender_run(log, args):
    TCP_IP = args['address']
    TCP_PORT = args['port']
    MESSAGE = '%s %s %d\n' % (args['metric'], args['value'], int(time.time()))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    log.info('Connecting to tcp address {}...'.format(TCP_IP + ":" + TCP_PORT))
    s.connect((TCP_IP, int(TCP_PORT)))

    log.info('Sending data: {}'.format(MESSAGE))
    s.sendall(MESSAGE)

    log.info('Closing socket...')
    s.close()

    log.info('Send finished!')
