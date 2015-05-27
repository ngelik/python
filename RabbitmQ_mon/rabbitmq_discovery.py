from rabbitmq_helper import *


class Rabbitmq_Discovery(Rabbitmq_Helper):
    def get_queues(self, param):
        return [q[param] for q in self.get_api_queues()]

    def get_exchanges(self, param):
        return [q[param] for q in self.get_api_exchanges()]

    def convert_data_for_zabbix(self, data, prefix):
        l = []
        [l.append({prefix: q}) for q in data]
        return json.dumps({'data': l}, indent=4)

    def queues_all_discovery(self):
        print(self.convert_data_for_zabbix(self.get_queues("name"), "{#MQ_ALL_QUEUE}"))

    def queues_durable_discovery(self):
        durable_queues = [item for item in self.get_api_queues() if item["durable"] is True]
        print(self.convert_data_for_zabbix([q["name"] for q in durable_queues], "{#MQ_DURABLE_QUEUE}"))

    def queues_no_durable_discovery(self):
        durable_queues = [item for item in self.get_api_queues() if item["durable"] is False]
        print(self.convert_data_for_zabbix([q["name"] for q in durable_queues], "{#MQ_NO_DURABLE_QUEUE}"))

    def exchanges_discovery(self):
        print(self.convert_data_for_zabbix(self.get_exchanges("name"), "{#MQ_EXCHANGE}"))