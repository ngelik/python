## RabbitmQ_mon

Templates collection for monitoring RabbitMQ from Zabbix

You can monitor the following parameters:

* queue availability

* queue consumers

* queue messages

* queue memory

* exchange availability

* consumers availability

* rates publish

* rates deliver

* rates publish sum

* rates deliver sum

*Example usage:*

*zabbix_agentd.userparams.conf*

UserParameter=rabbitmq.queue.availability[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1

UserParameter=rabbitmq.queue.consumers[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 consumers

UserParameter=rabbitmq.queue.messages[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 messages

UserParameter=rabbitmq.queue.memory[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 memory

UserParameter=rabbitmq.exchange.availability[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_exchanges $1

UserParameter=rabbitmq.consumers.availability[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_consumers $1

UserParameter=rabbitmq.rates.publish[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.publish $1

UserParameter=rabbitmq.rates.deliver[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.deliver $1

UserParameter=rabbitmq.rates.publish.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.publish.sum

UserParameter=rabbitmq.rates.deliver.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.deliver.sum
