from queue_system import QueueSystem

class MainTest:
    def __init__(self):
        self.__queue_system = QueueSystem()

    def create_queue(self, id, name, max_size = 10):
        self.__queue_system.create_queue(id, name, max_size)

    def create_consumer(self, id, queue_id, callback):
        self.__queue_system.create_consumer(id, queue_id, callback)

    def remove_consumer(self, id):
        self.__queue_system.remove_consumer(id)

    def push_into_queue(self, queue_id, payload):
        self.__queue_system.push_into_queue(queue_id, payload)

    def run_consumer(self, consumer_id):
        self.__queue_system.run_consumer(consumer_id)

if __name__ == "__main__":
    main = MainTest()
    main.create_queue(1, "test_queue 1")
    main.create_queue(2, "test_queue 2")

    main.create_consumer(1, 1, lambda x: print(f"Consumer 1 received {x}"))
    main.create_consumer(2, 2, lambda x: print(f"Consumer 2 received {x}"))
    main.create_consumer(3, 1, lambda x: print(f"Consumer 3 received {x}"))
    main.create_consumer(4, 2, lambda x: print(f"Consumer 4 received {x}"))

    while True:
        type = int(input("Enter 1 to push into queue 1 or 2 to push into queue 2: "))
        if type == 1:
            main.push_into_queue(1, "hello")
        elif type == 2:
            main.push_into_queue(2, "world")
        elif type == 3:
            consumer_run = int(input("Enter number of consumer to run: "))
            if consumer_run == 1:
                main.run_consumer(1)
            elif consumer_run == 2:
                main.run_consumer(2)
            elif consumer_run == 3:
                main.run_consumer(3)
            elif consumer_run == 4:
                main.run_consumer(4)
        else:
            break