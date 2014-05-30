# Script for python 2.4
import simplejson as json
from pprint import pprint
import urllib2, base64
from sys import argv


url="http://127.0.0.1:15672/api/queues"
usr="monitor_user"
pwd="monitor_pwd"

#rate_types = ["deliver_get_details", "publish_details"]

def get_data(url, usr, pwd):
    try:
        request = urllib2.Request(url)
	base64string = base64.encodestring('%s:%s' % (usr, pwd)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)
	result = urllib2.urlopen(request)
    
	data = json.load(result)
	#pprint(data)
	return data
	
    except Exception,e:
	return None

def get_rates(data, queue_name, rate_type):
    try:
        rates = [item for item in data
	    if item["name"] == queue_name]	

	rate = rates[0]["message_stats"][rate_type]["rate"]
	#pprint(rate_type + " - " + str(rate))

	return rate
    except Exception,e:
       return -1
    

def get_rates_sum(data, rate_type):
    return sum((data[i]["message_stats"][rate_type]["rate"]) for i in range(0, int(len(data))))
    
    
if argv[1] == "deliver_get_details_sum":
    print get_rates_sum(get_data(url, usr, pwd), "deliver_get_details")
elif argv[1] == "publish_details_sum":
    print get_rates_sum(get_data(url, usr, pwd), "publish_details")
else: 
    #for degug
    #print get_rates(get_data(url, usr, pwd), "MTSPROD-niagaraEntryAsyncProtocol-pc-mtspso", "deliver_get_details")
    print get_rates(get_data(url, usr, pwd), argv[1], argv[2])