object=$1
queue_name=$2
queue_param=$3

case "$object" in
    rates.publish) 
	python /etc/zabbix/scripts/rabbitmq/get_rates.py $queue_name "publish_details"
        exit $?        
        ;;
    rates.deliver)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py $queue_name "deliver_no_ack_details"
        exit $?
        ;;
    rates.ack)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py $queue_name "ack_details"
        exit $?
        ;;
    rates.get)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py $queue_name "get_details"
        exit $?
        ;;     
    rates.publish.sum)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "publish_details_sum"
        exit $?
        ;;
    rates.deliver.sum)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "deliver_no_ack_sum"
        exit $?
        ;;
    rates.ack.sum)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "ack_details_sum"
        exit $?
        ;;
    rates.get.sum)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "get_details_sum"
        exit $?
        ;;
    rates.confirm.sum)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "confirm_details_sum"
        exit $?
	;;
    res.fd)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "res" "fd_used"
        exit $?
        ;; 
    res.sd)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "res" "sockets_used"
        exit $?
        ;;                                                              
    res.ep)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "res" "proc_used"
        exit $?
        ;;                                     	
    res.mem)
        python /etc/zabbix/scripts/rabbitmq/get_rates.py "res" "mem_used"
        exit $?
        ;;                                
esac
        
if [ "${3}" != "" ]; then
    sudo rabbitmqctl $object name $queue_param | grep $queue_name | awk '{ print $2 }'
else
    sudo rabbitmqctl $object name | grep -c $queue_name    
fi

#echo Return code - $?
exit $?
