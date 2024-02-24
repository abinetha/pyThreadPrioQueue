from threaded_priority_message_queue import PriorityMessageQueue, ThreadPool, MessagePasser
import time

def test_priority_message_queue():
    print("Testing Priority Message Queue...")
    priority_message_queue = PriorityMessageQueue()

    # Test Enqueue and Peek
    priority_message_queue.enqueue_message("Message 1", priority=1)
    priority_message_queue.enqueue_message("Message 2", priority=2)
    assert priority_message_queue.peek_message() == "Message 2"

    # Test Dequeue
    assert priority_message_queue.dequeue_message() == "Message 2"
    assert priority_message_queue.dequeue_message() == "Message 1"

    # Test Empty Check
    assert priority_message_queue.is_empty() == True
    print("Priority Message Queue test passed!\n")

def test_thread_pool():
    print("Testing Thread Pool...")
    thread_pool = ThreadPool(num_threads=3)

    # Test Submit Job and Wait Completion
    def dummy_job():
        print("Dummy job executed!")
    thread_pool.submit_job(dummy_job)
    thread_pool.submit_job(dummy_job)
    thread_pool.submit_job(dummy_job)
    thread_pool.wait_completion()
    print("Thread Pool test passed!\n")

def test_message_passer():
    print("Testing Message Passer...")
    priority_message_queue = PriorityMessageQueue()
    thread_pool = ThreadPool(num_threads=3)
    message_passer = MessagePasser(priority_message_queue, thread_pool)

    # Test Sending and Receiving Messages
    message_passer.send_message("Hello", priority=2)
    message_passer.send_message("World", priority=1)
    time.sleep(2)  # Simulate other work
    message_passer.receive_message()
    message_passer.receive_message()
    thread_pool.wait_completion()
    print("Message Passer test passed!\n")

if __name__ == "__main__":
    test_priority_message_queue()
    test_thread_pool()
    test_message_passer()
