# since Python 3.5 https://www.python.org/dev/peps/pep-0492/

import asyncio

async def coro_example_one():
    print("Go to sleep from one.")
    await asyncio.sleep(0.1)
    print("Finish one")

async def coro_example_second():
    print("Call coro_example_second")
    await coro_example_one()
    print("Go to sleep from second")
    await asyncio.sleep(0.1)
    print("Finish second")

async def coro_example_third():
    print("call coro_example_third")
    await coro_example_one()
    print("Go to sleep from third.")
    await asyncio.sleep(0.1)
    print("Finish third")



print("What is if not called: ", type(coro_example_one))

"""
print("What is if called: ", type(coro_example_one()))

async_await.py:9: RuntimeWarning: coroutine 'coro_example_one' was never awaited
  print("What is if called: ", type(coro_example_one()))
What is if called:  <class 'coroutine'>
"""

loop = asyncio.get_event_loop()
loop.run_until_complete(coro_example_second())

print("show how to run tasks in parallel")

loop.run_until_complete(asyncio.gather(
    coro_example_second(),
    coro_example_third()))

loop.close()

"""
What is if not called:  <class 'function'>

Call coro_example_second
Go to sleep from one.
Finish one
Go to sleep from second
Finish second

show how to run tasks in parallel

Call coro_example_second
Go to sleep from one.
call coro_example_third
Go to sleep from one.
Finish one
Go to sleep from second
Finish one
Go to sleep from third.
Finish second
Finish third
"""