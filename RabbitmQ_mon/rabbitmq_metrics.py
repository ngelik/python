# -*- coding: utf-8 -*-м# -*- coding: utf-8 -*-

#Script for python 2.4
from rabbitmq_helper import *


class Rabbitmq_Metrics(Rabbitmq_Helper):
    @exc_dec
    def queue_availability(self, queue_name):
        self.get_queue_data(queue_name)
        print 1

    @exc_dec
    def exchange_availability(self, exchange_name):
        self.get_exchange_data(exchange_name)
        print 1

    @exc_dec
    def queue_consumers(self, queue_name):
        print(self.get_queue_data(queue_name)['consumers'])

    @exc_dec
    def messages_all(self, queue_name):
        print(self.get_messages(queue_name, 'messages'))

    @exc_dec
    def messages_ready(self, queue_name):
        print(self.get_messages(queue_name, 'messages_ready'))

    @exc_dec
    def messages_unacknowledged(self, queue_name):
        print(self.get_messages(queue_name, 'messages_unacknowledged'))

    @exc_dec
    def queue_memory(self, queue_name):
        print(self.get_queue_data(queue_name)['memory'])

    @exc_dec
    def messages_all_sum(self):
        print(self.get_msg_sum('messages'))

    @exc_dec
    def messages_ready_sum(self):
        print(self.get_msg_sum('messages_ready'))

    @exc_dec
    def messages_unacknowledged_sum(self):
        print(self.get_msg_sum('messages_unacknowledged'))

    @exc_dec
    def rates_publish(self, queue_name):
        print(self.get_rates(queue_name, "publish_details"))

    @exc_dec
    def rates_confirm(self, queue_name):
        print(self.get_rates(queue_name, "confirm_details"))

    @exc_dec
    def rates_ack(self, queue_name):
        print(self.get_rates(queue_name, "ack_details"))

    @exc_dec
    def rates_get(self, queue_name):
        print(self.get_rates(queue_name, "get_details"))

    @exc_dec
    def rates_deliver_no_ack(self, queue_name):
        print(self.get_rates(queue_name, "deliver_no_ack_details"))

    @exc_dec
    def rates_publish_sum(self):
        print(self.get_rates_sum('publish_details'))

    @exc_dec
    def rates_confirm_sum(self):
        print(self.get_rates_sum('confirm_details'))

    @exc_dec
    def rates_redelivered_sum(self):
        print(self.get_rates_sum('redeliver_details'))

    @exc_dec
    def rates_ack_sum(self):
        print(self.get_rates_sum('ack_details'))

    @exc_dec
    def rates_get_sum(self):
        print(self.get_rates_sum('get_details'))

    @exc_dec
    def rates_deliver_no_ack_sum(self):
        print(self.get_rates_sum('deliver_no_ack_details'))

    @exc_dec
    def fd_used(self):
        print(self.get_resources_info('fd_used'))

    @exc_dec
    def sockets_used(self):
        print(self.get_resources_info('sockets_used'))

    @exc_dec
    def proc_used(self):
        print(self.get_resources_info('proc_used'))

    @exc_dec
    def mem_used(self):
        print(self.get_resources_info('mem_used'))

    @exc_dec
    def channels_total(self):
        print(self.get_totals('channels'))

    @exc_dec
    def connections_total(self):
        print(self.get_totals('connections'))

    @exc_dec
    def consumers_total(self):
        print(self.get_totals('consumers'))

    @exc_dec
    def exchanges_total(self):
        print(self.get_totals('exchanges'))

    @exc_dec
    def queues_total(self):
        print(self.get_totals('queues'))
