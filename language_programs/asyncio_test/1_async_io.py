import asyncio
import time
from concurrent.futures.process import ProcessPoolExecutor

import random


async def coro_a(n):
    print("> a", n)
    await asyncio.sleep(random.uniform(0.1, 1))
    result = await asyncio.gather(coro_b(n),
                                  loop.run_in_executor(None, slow_method_c, n))
    print("< a", n, result)


async def coro_b(n):
    print("> b", n)
    await asyncio.sleep(random.uniform(0.1, 1))
    result = await loop.run_in_executor(None, slow_method_d, n)
    print("< b", n, result)
    return ("B", result)


def slow_method_c(n):
    print("> c", n)
    time.sleep(random.uniform(0.5, 5))
    print("< c", n)
    return ("C", n)


def slow_method_d(n):
    print("> d", n)
    time.sleep(random.uniform(0.5, 5))
    print("< d", n)
    return ("D", n)


async def main_producer():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(coro_a(i + 1)))
        await asyncio.sleep(1)
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.set_default_executor(ProcessPoolExecutor())
loop.run_until_complete(main_producer())
loop.close()