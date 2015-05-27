## RabbitmQ_mon

Templates collection for monitoring RabbitMQ from Zabbix

You can monitor the following parameters:

* queue availability

* queue consumers count

* queue messages count

* queue messages_ready count

* queue messages_unacknowledged count

* queue memory usage

* exchange availability

* consumers availability

* rates publish count for queue

* rates deliver count for queue

* rates ack count for queue

* rates get count for queue

* rates publish sum 

* rates deliver sum

* rates ack sum

* rates get sum

* rates confirm sum

* file descriptors usage

* socket descriptors usage

* erlang processes usage

* memory usage

### Run as non root user

```sh
visudo
%rabbitmq ALL=(ALL) NOPASSWD: /usr/sbin/rabbitmqctl
%rabbitmq ALL=(ALL) NOPASSWD: /usr/local/bin/erl
%zabbix ALL=(ALL) NOPASSWD: /usr/sbin/rabbitmqctl
Defaults    !requiretty
```

### Example usage

Add to **zabbix_agentd.userparams.conf**

```
UserParameter=rabbitmq.queue.availability[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1
UserParameter=rabbitmq.queue.consumers[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 consumers
UserParameter=rabbitmq.queue.messages[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 messages
UserParameter=rabbitmq.queue.messages_ready[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 messages_ready
UserParameter=rabbitmq.queue.messages_unacknowledged[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 messages_unacknowledged
UserParameter=rabbitmq.queue.memory[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_queues $1 memory

UserParameter=rabbitmq.exchange.availability[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_exchanges $1
UserParameter=rabbitmq.consumers.availability[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh list_consumers $1

UserParameter=rabbitmq.rates.publish[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.publish $1
UserParameter=rabbitmq.rates.deliver[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.deliver $1
UserParameter=rabbitmq.rates.ack[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.ack $1
UserParameter=rabbitmq.rates.get[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.get $1

UserParameter=rabbitmq.queue.messages_unacknowledged.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh messages_unacknowledged.sum
UserParameter=rabbitmq.queue.messages_ready.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh messages_ready.sum
UserParameter=rabbitmq.queue.messages.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh messages.sum

UserParameter=rabbitmq.rates.publish.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.publish.sum
UserParameter=rabbitmq.rates.deliver.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.deliver.sum
UserParameter=rabbitmq.rates.ack.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.ack.sum
UserParameter=rabbitmq.rates.get.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.get.sum
UserParameter=rabbitmq.rates.confirm.sum[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh rates.confirm.sum

UserParameter=rabbitmq.res.filedescriptors[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh res.fd
UserParameter=rabbitmq.res.socketdescriptors[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh res.sd
UserParameter=rabbitmq.res.erlangprocesses[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh res.ep
UserParameter=rabbitmq.res.memory[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh res.mem

UserParameter=rabbitmq.totals.channels[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh totals.channels
UserParameter=rabbitmq.totals.connections[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh totals.connections
UserParameter=rabbitmq.totals.consumers[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh totals.consumers
UserParameter=rabbitmq.totals.exchanges[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh totals.exchanges
UserParameter=rabbitmq.totals.queues[*],/etc/zabbix/scripts/rabbitmq/rabbitmq_stat.sh totals.queues
```
