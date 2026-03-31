from simple_queue import SimpleQueue
from consumer import Consumer

class QueueSystem:
    def __init__(self):
        self.__queues = {}
        self.__consumers = {}
        self.__queue_consumer_mapping = {}

    def create_queue(self, id, name, max_size = 10):
        if id in self.__queues:
            print("Queue already exists")
            return
        
        self.__queues[id] = SimpleQueue(id, name, max_size)
        print(f"Queue {name} created")

    def create_consumer(self, id, queue_id, callback):
        if id in self.__consumers:
            print("Consumer already exists")
            return
        
        if queue_id not in self.__queues:
            print("Queue not found")
            return

        self.__consumers[id] = Consumer(id, self.__queues[queue_id], callback)

        if queue_id not in self.__queue_consumer_mapping:
            self.__queue_consumer_mapping[queue_id] = []

        self.__queue_consumer_mapping[queue_id].append(id)
        print(f"Consumer {id} created")

    def remove_consumer(self, id):
        if id not in self.__consumers:
            print("Consumer not found")
            return

        queue_id = self.__consumers[id].get_queue().get_id()
        self.__queue_consumer_mapping[queue_id].remove(id)

        del self.__consumers[id]
        print(f"Consumer {id} removed")

    def push_into_queue(self, queue_id, payload):
        if queue_id not in self.__queues:
            print("Queue not found")
            return
        
        self.__queues[queue_id].add_to_ready_queue(payload)

    def run_consumer(self, consumer_id):
        if consumer_id not in self.__consumers:
            print("Consumer not found")
            return
        
        self.__consumers[consumer_id].process()