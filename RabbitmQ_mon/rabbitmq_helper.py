import urllib2
import base64
import simplejson as json
from pprint import pprint
import os
import time
import inspect


def exc_dec(f):
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception:
            print -1
    return wrapper


class Rabbitmq_Helper:
    def __init__(self, params):
        self.ip = params['ip']
        self.port = params['port']
        self.usr = params['usr']
        self.pwd = params['pwd']
        self.cache_file_path = os.path.dirname(os.path.abspath(__file__))
        self.cache_period_sec = 60

    def make_url(self, api):
        return "http://" + self.ip + ":" + self.port + '/' + api

    def make_cache_file_name_from_url(self, url):
        return self.cache_file_path + '/' + url.replace('/', '_') + ".tmp"

    def is_old_cache_file(self, file_name):
        one_minute_ago = time.time() - self.cache_period_sec
        if not os.path.isfile(file_name) or (os.stat(file_name).st_mtime < one_minute_ago):
            return True
        else:
            return False

    def make_cache_file(self, file_name, data):
        f = open(file_name, 'w')
        try:
            json.dump(data, f)
        finally:
            f.close()

    def get_data_from_file(self, file_name):
        stream = open(file_name, 'r')
        data = json.load(stream)
        return data

    def get_data_from_http(self, url):
        try:
            request = urllib2.Request(self.make_url(url))
            base64string = base64.encodestring('%s:%s' % (self.usr, self.pwd)).replace('\n', '')
            request.add_header("Authorization", "Basic %s" % base64string)
            result = urllib2.urlopen(request)
            return json.load(result)
        except Exception, e:
            print ("URL" + self.make_url(url))
            print (e)
            return None

    def get_data_from_api(self, url):
        if self.is_old_cache_file(self.make_cache_file_name_from_url(url)):
            new_data = self.get_data_from_http(url)
            self.make_cache_file(self.make_cache_file_name_from_url(url), new_data)
            return new_data
        else:
            return self.get_data_from_file(self.make_cache_file_name_from_url(url))

    def get_api_queues(self):
        return self.get_data_from_api("api/queues")

    def get_api_exchanges(self):
        return self.get_data_from_api("api/exchanges")

    def get_api_overview(self):
        return self.get_data_from_api("api/overview")

    def get_api_resources(self):
        return self.get_data_from_api("api/nodes")

    def get_queue_data(self, queue_name):
        return [item for item in self.get_api_queues()
                if item["name"] == queue_name][0]

    def get_exchange_data(self, exchange_name):
        return [item for item in self.get_api_exchanges()
                if item["name"] == exchange_name][0]

    def get_messages(self, queue_name, msg_type):
        return self.get_queue_data(queue_name)[msg_type]

    def get_rates(self, queue_name, rate_type):
        return self.get_queue_data(queue_name)["message_stats"][rate_type]["rate"]

    def get_msg_sum(self, msg_type):
        return self.get_api_overview()["queue_totals"][msg_type]

    def get_rates_sum(self, rate_type):
        return self.get_api_overview()["message_stats"][rate_type]["rate"]

    def get_resources_info(self, res_type):
        return self.get_api_resources()[0][res_type]

    def get_totals(self, total_type):
        return self.get_api_overview()["object_totals"][total_type]

    def get_api_tests(self):
        print('------------------------- GET API QUEUES ---------------------------------------')
        pprint(self.get_api_queues())
        print('------------------------- GET API EXCHANGES ------------------------------------')
        pprint(self.get_api_exchanges())
        print('------------------------- GET API OVERVIEW -------------------------------------')
        pprint(self.get_api_overview())
        print('------------------------- GET API RESOURCES ------------------------------------')
        pprint(self.get_api_resources())