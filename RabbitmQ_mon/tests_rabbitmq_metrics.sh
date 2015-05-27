echo ---------------------------
echo GET API DATA
/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh get_api_tests > get_api_tests


echo ---------------------------
echo COMMON
echo "queue_availability success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh queue_availability MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "queue_availability error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh queue_availability MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "exchange_availability success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh exchange_availability MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "exchange_availability error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh exchange_availability MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "queue_consumers success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh queue_consumers MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "queue_consumers error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh queue_consumers MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"

echo ---------------------------
echo QUEUE MESSAGES COUNT INFO
echo "messages_all success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_all MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "messages_all error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_all MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "messages_ready success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_ready MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "messages_ready error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_ready MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "messages_unacknowledged success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_unacknowledged MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "messages_unacknowledged error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_unacknowledged MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "queue_memory success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh queue_memory MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "queue_memory error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh queue_memory MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"

echo ---------------------------
echo QUEUE MESSAGES RATES INFO
echo "rates_publish success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_publish MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "rates_publish error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_publish MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "rates_confirm success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_confirm MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "rates_confirm error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_confirm MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "rates_ack success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_ack MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "rates_ack error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_ack MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "rates_get success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_get MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "rates_get error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_get MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"
echo "rates_deliver_no_ack success $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_deliver_no_ack MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc)"
echo "rates_deliver_no_ack error $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_deliver_no_ack MTSTEST-niagaraEntryAsyncProtocol-mtspso-pc1)"

echo ---------------------------
echo SUMMARY MESSAGES COUNT INFO
echo "messages_all_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_all_sum)"
echo "messages_ready_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_ready_sum)"
echo "messages_unacknowledged_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh messages_unacknowledged_sum)"

echo ---------------------------
echo SUMMARY MESSAGES RATES INFO
echo "rates_publish_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_publish_sum)"
echo "rates_confirm_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_confirm_sum)"
echo "rates_redelivered_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_redelivered_sum)"
echo "rates_ack_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_ack_sum)"
echo "rates_get_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_get_sum)"
echo "rates_deliver_no_ack_sum $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh rates_deliver_no_ack_sum)"

echo ---------------------------
echo SUMMARY RESOURSES
echo "fd_used $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh fd_used)"
echo "sockets_used $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh sockets_used)"
echo "proc_used $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh proc_used)"
echo "mem_used $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh mem_used)"

echo ---------------------------
echo TOTAL INFO
echo "channels_total $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh channels_total)"
echo "connections_total $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh connections_total)"
echo "consumers_total $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh consumers_total)"
echo "exchanges_total $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh exchanges_total)"
echo "queues_total $(/etc/zabbix/scripts/rabbitmq/rabbitmq_metrics.sh queues_total)"
