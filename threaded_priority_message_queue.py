import threading
import queue
import time
import socket

class PriorityMessageQueue:
    def __init__(self):
        self._queue = queue.PriorityQueue()
        self._lock = threading.Lock()

    def enqueue_message(self, message, priority):
        with self._lock:
            self._queue.put((priority, message))

    def dequeue_message(self):
        with self._lock:
            if not self._queue.empty():
                return self._queue.get()[1]
            else:
                return None

    def peek_message(self):
        with self._lock:
            if not self._queue.empty():
                return self._queue.queue[0][1]
            else:
                return None

    def is_empty(self):
        with self._lock:
            return self._queue.empty()


class ThreadPool:
    def __init__(self, num_threads):
        if num_threads <= 0:
            raise ValueError("Number of threads must be greater than 0.")
        
        self._thread_pool = []
        self._job_queue = queue.Queue()
        for _ in range(num_threads):
            thread = threading.Thread(target=self._worker)
            thread.start()
            self._thread_pool.append(thread)

    def _worker(self):
        while True:
            job_func = self._job_queue.get()
            if job_func is None:
                break
            try:
                job_func()
            except Exception as e:
                print("An error occurred in thread:", threading.current_thread().name)
                print("Error:", e)
            finally:
                self._job_queue.task_done()

    def submit_job(self, job_func):
        self._job_queue.put(job_func)

    def wait_completion(self):
        self._job_queue.join()

    def shutdown(self):
        for _ in self._thread_pool:
            self._job_queue.put(None)
        for thread in self._thread_pool:
            thread.join()


class MessagePasser:
    def __init__(self, priority_message_queue, thread_pool):
        self._priority_message_queue = priority_message_queue
        self._thread_pool = thread_pool

    def send_message(self, message, priority):
        self._priority_message_queue.enqueue_message(message, priority)

    def receive_message(self):
        message = self._priority_message_queue.dequeue_message()
        if message:
            self._thread_pool.submit_job(lambda: self._process_message(message))

    def _process_message(self, message):
        # Example action: Printing the message
        print("Received message:", message)
        # Simulating some work
        time.sleep(1)


def check_port_availability(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('127.0.0.1', port))
            return True
        except OSError as e:
            print(f"Port {port} is not available:", e)
            return False


def main():
    try:
        # Checking port availability before starting the program
        port = 12345  # Example port number
        if not check_port_availability(port):
            print("Port is not available. Exiting.")
            return

        priority_message_queue = PriorityMessageQueue()
        thread_pool = ThreadPool(num_threads=3)
        message_passer = MessagePasser(priority_message_queue, thread_pool)

        # Example usage
        message_passer.send_message("Hello", priority=2)
        message_passer.send_message("World", priority=1)

        time.sleep(2)  # Simulating other work

        message_passer.receive_message()
        message_passer.receive_message()

        thread_pool.wait_completion()
        thread_pool.shutdown()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
