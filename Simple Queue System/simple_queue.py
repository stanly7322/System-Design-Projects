# Creation of new queue

from queue import Queue

class SimpleQueue:
    def __init__(self, id, name, max_size = 10):
        self.__name = name
        self.__id = id
        self.__max_size = max_size

        self.__ready_queue = Queue(maxsize = self.__max_size)
        self.__in_progress_elements = {}

        self.__failed_elements = []

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_max_size(self):
        return self.__max_size
    
    def add_to_ready_queue(self, payload):
        if self.__ready_queue.full():
            print("Queue is full can't push more elements")
            return
        
        self.__ready_queue.put(payload)
        print(f"Element {payload} added to queue")

    def add_to_in_progress(self, consumer_id):
        if self.__ready_queue.empty():
            print("Queue is empty can't add element to in progress")
            return None
        
        payload = self.__ready_queue.get()
        self.__in_progress_elements[consumer_id] = (payload)
        print(f"Element {payload} added to in progress queue")
        return payload

    def get_failed_elements(self):
        return self.__failed_elements
    
    def remove_from_in_progress(self, consumer_id):
        if consumer_id in self.__in_progress_elements:
            payload = self.__in_progress_elements[consumer_id]
            del self.__in_progress_elements[consumer_id]
            print(f"Element {payload} removed from in progress queue")
        else:
            print("Consumer not found")
