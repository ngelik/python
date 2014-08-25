# Script for python 2.4
import simplejson as json
from pprint import pprint
import urllib2, base64
from sys import argv


url_queues="http://127.0.0.1:15672/api/queues"
url_overview="http://127.0.0.1:15672/api/overview"
url_res="http://127.0.0.1:15672/api/nodes"
usr="monitor_user"
pwd="monitor_pwd"

# q_rate_types = ["deliver_no_ack_details", "publish_details", "ack_details", "get_details"]
# a_rate_types = ["confirm_details"]

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

def get_queues_rates(data, queue_name, rate_type):
    try:
        rates = [item for item in data
	    if item["name"] == queue_name]	

	rate = rates[0]["message_stats"][rate_type]["rate"]
	#pprint(rate_type + " - " + str(rate))

	return rate
    except Exception,e:
       return -1
    

def get_rates_sum(data, rate_type):
    return data["message_stats"][rate_type]["rate"]
                                

def get_resources_info(data, res_type):
    return data[0][res_type]

    
if argv[1] == "deliver_no_ack_sum":
    print get_rates_sum(get_data(url_overview, usr, pwd), "deliver_no_ack_details")
elif argv[1] == "publish_details_sum":
    print get_rates_sum(get_data(url_overview, usr, pwd), "publish_details")
elif argv[1] == "ack_details_sum":
    print get_rates_sum(get_data(url_overview, usr, pwd), "ack_details")
elif argv[1] == "get_details_sum":
    print get_rates_sum(get_data(url_overview, usr, pwd), "get_details")
elif argv[1] == "confirm_details_sum":
    print get_rates_sum(get_data(url_overview, usr, pwd), "confirm_details")        
elif argv[1] == "res":
    print get_resources_info(get_data(url_res, usr, pwd), argv[2])        
else: 
    #for degug
    #print get_rates(get_data(url, usr, pwd), "MTSPROD-niagaraEntryAsyncProtocol-pc-mtspso", "deliver_get_details")
    print get_queues_rates(get_data(url_queues, usr, pwd), argv[1], argv[2])