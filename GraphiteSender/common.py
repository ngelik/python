# -*- coding: utf-8 -*-м# -*- coding: utf-8 -*-

import time
import logging
import logging.config
import os
import yaml
import inspect
import platform
from abc import ABCMeta, abstractmethod
import shutil
#from zipfile import ZipFile
import  zipfile
import stat
import errno
from os.path import join
from glob import iglob
from shutil import copy
from os.path import join


def log_init(
        default_logging_format='%(asctime)s %(name)-8s %(levelname)-8s '
                               '%(filename)s[on line:%(lineno)d][%(funcName)s]# %(message)s',
        default_level=logging.INFO):

    logging.basicConfig(format=default_logging_format, level=default_level)
    log = logging.getLogger()
    return  log


def contains(stepsList, my_filter):
    for x in stepsList:
        if my_filter(x):
            return True
    return False


def setup_logging(
        default_path='logging.yaml',
        env_key='LOG_CFG'):

    """Setup logging configuration
     """

    # handler = TimedCompressedRotatingFileHandler()
    # log.addHandler(handler)

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

        log = logging.getLogger()
    else:
        log = log_init()
    log.debug('Logging init!')

    return log


def timer_dec(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        args[0].debug('<{}> start'.format(f.__name__))
        res = f(*args, **kwargs)
        args[0].debug('<{}> finish'.format(f.__name__))
        args[0].debug("Working time for function <%s>: %f" % (f.__name__, time.time() - t))
        return  res

    return wrapper


def timer_dec_class(decorator):
    def decTheClass(cls):
        for name, m in inspect.getmembers(cls, inspect.ismethod):
            setattr(cls, name, decorator(m))
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return cls
    return decTheClass


def whoami():
    return inspect.stack()[1][3]


def whosdaddy():
    return inspect.stack()[2][3]


class ParamCountException(Exception):
    """Исключение, порождается если при старте программы
        не передано ниодного аргумента командной строки
    """

    def __init__(self, message1, message2):
        self.message = []
        self.message.append(message1)
        self.message.append(message2)
        self.message.append("Count if command line arguments is incorrect!")

    def __str__(self):
        return repr(self.message)


class A(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def method(self):
        pass


@timer_dec
def t(log):
    log.debug(u'This is a debug message - ')
    log.info(u'This is an info message')
    time.sleep(.1)


class B(A):
    def method(self):
        print 'B'


class C(A):
    def method(self):
        print 'C'


class D:
    def method(self):
        print 'D'


def abc_test():
    for obj in [B(), C(), D()]:
        if issubclass(type(obj), A):
            obj.method()


def press_any_key():
    if platform.system() == 'Windows':
        os.system('pause')
    else:
        os.system('read -p "Press  any key to continue"')


def get_os_type():
    if platform.system() == 'Windows':
        return 'Windows'
    else:
        return 'Linux'


def deleteAllInDir(log, fileList, path):
    for f in fileList:
        p = os.path.join(path, f)
        log.debug("Delete file - '{}'".format(p))
        if os.path.isdir(p):
            shutil.rmtree(p, True)
        else:
            os.remove(p)


def doublePrint(log, msg):
    print(msg)
    log.debug(msg)


def zipDir(log, dir_name):
    zipF = zipfile.ZipFile(dir_name + '.zip', 'w', zipfile.ZIP_DEFLATED)
    L = len(dir_name) + 1

    for dirPath, dirs, files in os.walk(dir_name):
        if not files and not dirs:
            log.debug("Create empty file - '{}'".format(dirPath + '/.empty'))
            f = open(dirPath + '/.empty', 'w')
            f.close()

    for dirPath, dirs, files in os.walk(dir_name):
        for name in files:
            fn = os.path.join(dirPath, name)
            zipF.write(fn, fn[L:])
            log.debug("adding - '{}'".format(fn))


def myRmTree(pathToFile):
    def handleRemoveReadonly(func, path, exc):
        excvalue = exc[1]
        if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
            # 0777
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            func(path)
        else:
            raise

    shutil.rmtree(pathToFile, ignore_errors=False, onerror=handleRemoveReadonly)


def copy_files(log, src_glob, dst_folder):
    for fName in iglob(src_glob):
        log.debug("copy_files: from '{}' to '{}'".format(fName, dst_folder))
        shutil.copy(fName, dst_folder)
