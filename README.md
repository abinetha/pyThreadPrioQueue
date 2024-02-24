# Multi-Threaded Priority Message Queue Implementation

This project implements a multi-threaded priority message queue system in Python. It allows multiple threads to send messages to each other with varying priorities and performs actions upon receiving messages using a thread pool.

## Table of Contents

- [Overview](#overview)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
  

## Overview

In this project, we implement the following components:

- Priority Message Queue: Supports operations like enqueue, dequeue, peek, and empty check.
- Thread Pool: Manages a fixed number of threads to execute tasks concurrently.
- MessagePasser: Facilitates message passing between threads and action execution using the priority message queue and thread pool.

## Components

### Priority Message Queue

The priority message queue is implemented using Python's `queue.PriorityQueue`. It provides the following operations:

- Enqueue Message: Adds a message to the queue with a specified priority.
- Dequeue Message: Removes and returns the highest priority message from the queue.
- Peek Message: Returns the highest priority message without removing it from the queue.
- Empty Check: Checks if the queue is empty.

### Thread Pool

The thread pool manages a fixed number of threads using Python's `threading.Thread`. It provides the following functionality:

- Submit Job: Adds a job to the job queue for execution by the threads.
- Wait Completion: Blocks until all jobs in the queue are completed.
- Shutdown: Stops all threads gracefully after completing the current jobs.

### MessagePasser

MessagePasser facilitates sending and receiving messages between threads. It enqueues messages into the priority message queue and executes actions using the thread pool upon receiving messages.

## Installation

No installation is required. Simply clone the repository to your local machine.

```bash
git clone https://github.com/your-username/multi-threaded-message-queue.git
```

## Usage

Navigate to the project directory.

Run the main Python script.

```bash
python main.py
```

## Example

An example usage scenario is provided in the `main()` function of the `main.py` script. It demonstrates sending and receiving messages between threads with different priorities.

