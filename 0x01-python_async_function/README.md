# 0x01-python_async_function


## Learning Objectives

- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module


## Tasks

### [0. The basics of async](./0-basic_async_syntax.py)
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.

### [1. Let's execute multiple coroutines at the same time with `async`](./1-concurrent_coroutines.py)
Write a function named `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.

### [2. Measure the runtime](./2-measure_runtime.py)
Write a function named `measure_time` that measures the total execution time for `wait_n`.

### [3. Tasks](./3-tasks.py)
Take the code from wait_n and alter it into a new function named `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

### [4. Tasks](./4-tasks.py)
Take the code from `3-tasks` and alter it into a new function named `task_wait_random`. The code is nearly identical to `wait_random` except the loop is created outside the coroutine.