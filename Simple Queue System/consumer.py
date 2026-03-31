class Consumer:
    def __init__(self, id, queue, callback):
        self.__id = id
        self.__queue = queue
        self.__callback = callback

    def get_id(self):
        return self.__id
    
    def get_queue(self):
        return self.__queue
    
    # will process n messages once run
    def process(self, count = 10):
        for i in range(count):
            payload =  self.__queue.add_to_in_progress(self.__id)
            if payload:
                print(f"Consumer {self.__id} started processing")
                self.__callback(payload)
                self.__queue.remove_from_in_progress(self.__id)
                print(f"Consumer {self.__id} finished processing")
            else:
                print("no payload found")