import sys
import importlib
import yaml
import inspect
import os

run_params = {'module_name': sys.argv[1], 'class_name': sys.argv[2], 'action': sys.argv[3]}


def load_params():
    stream = open(os.path.dirname(os.path.abspath(__file__)) + "/params.yml", 'r')
    return yaml.load(stream)


def str_to_class(module_name, class_name, params):
    try:
        module_ = importlib.import_module(module_name)
        try:
            return getattr(module_, class_name)(params)
        except AttributeError:
            print('Class does not exist')
            return None
    except ImportError:
        print('Module does not exist')
        return None

if __name__ == '__main__':
    try:
        obj = str_to_class(run_params['module_name'], run_params['class_name'], load_params())
        method = getattr(obj, run_params['action'])
        if not method:
            raise Exception("Action %s not implemented" % run_params['action'])
        #print(inspect.getargspec(method).args)
        if len(sys.argv) > len(run_params):
            method(*tuple(sys.argv[(len(run_params) + 1):]))
        else:
            method()
    except Exception, e:
        print(e)