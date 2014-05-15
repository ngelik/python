import logging
from tcpsender import *
from tcpsender_args import *
from  common import timer_dec, setup_logging, press_any_key


@timer_dec
def run(log):
    args = get_args(log)
    tcp_sender_run(log, args)

if __name__ == '__main__':
    log = object
    try:
        log = setup_logging()
        log = logging.getLogger(__name__)

        run(log)
        log.debug(__name__ + 'finish!')
    except Exception as inst:
        log.exception(inst)
        #print(inst)
    else:
        log.debug('TCPSender successful done!')
        pass
    finally:
        log.debug('Finish!')
        #press_any_key()
        pass
