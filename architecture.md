# Architecture and Design Document: Multi-Threaded Priority Message Queue Implementation

## Overview

The Multi-Threaded Priority Message Queue Implementation project aims to create a system where multiple threads can send messages to each other with varying priorities. Upon receiving a message, the receiving thread performs a simple action using a thread pool.

## Components

### Priority Message Queue

The Priority Message Queue is implemented using Python's `queue.PriorityQueue`. It provides the following operations:
- Enqueue Message: Adds a message to the queue with a specified priority.
- Dequeue Message: Removes and returns the highest priority message from the queue.
- Peek Message: Returns the highest priority message without removing it from the queue.
- Empty Check: Checks if the queue is empty.

### Thread Pool

The Thread Pool manages a fixed number of threads using Python's `threading.Thread`. It provides the following functionality:
- Submit Job: Adds a job to the job queue for execution by the threads.
- Wait Completion: Blocks until all jobs in the queue are completed.
- Shutdown: Stops all threads gracefully after completing the current jobs.

### MessagePasser

MessagePasser facilitates sending and receiving messages between threads. It enqueues messages into the priority message queue and executes actions using the thread pool upon receiving messages.

## Design Considerations

- **Thread Safety**: Synchronization mechanisms such as locks are used to ensure thread safety in the implementation.
- **Error Handling**: The code includes error handling to handle potential exceptions that may arise in multithreading scenarios.
- **Port Availability Check**: Before starting the program, a check is performed to ensure that the specified port is available to avoid port collisions.
- **Modularity**: The code is structured into separate classes for the priority message queue, thread pool, and message passer, promoting modularity and ease of maintenance.
- **Documentation**: Comments are included within the code to explain specific sections and functionalities, enhancing readability and understanding.

## Conclusion

The Multi-Threaded Priority Message Queue Implementation provides a robust solution for facilitating communication between threads with varying priorities. By employing thread-safe data structures, error handling mechanisms, and modular design principles, the system ensures reliability and scalability in multithreaded environments.
