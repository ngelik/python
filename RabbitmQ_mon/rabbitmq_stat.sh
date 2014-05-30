queue_name=$2
queue_param=$3
object=$1

if [ "${1}" == "rates.publish" ]; then
    #echo "Rates for queue - ${queue_name}"
    python /etc/zabbix/scripts/rabbitmq/get_rates.py $queue_name "publish_details"
    exit $?
fi

if [ "${1}" == "rates.deliver" ]; then
    #echo "Rates for queue - ${queue_name}"
    python /etc/zabbix/scripts/rabbitmq/get_rates.py $queue_name "deliver_get_details"
    exit $?
fi
            
if [ "${1}" == "rates.publish.sum" ]; then
    python /etc/zabbix/scripts/rabbitmq/get_rates.py "publish_details_sum"
    exit $?
fi
            
if [ "${1}" == "rates.deliver.sum" ]; then
    python /etc/zabbix/scripts/rabbitmq/get_rates.py "deliver_get_details_sum"
    exit $?
fi
        

if [ "${3}" != "" ]; then
    sudo rabbitmqctl $object name $queue_param | grep $queue_name | awk '{ print $2 }'
else
    sudo rabbitmqctl $object name | grep -c $queue_name    
fi

#echo Return code - $?

exit $?
