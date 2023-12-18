#https://docs.python.org/3/library/asyncio-runner.html
#https://docs.python.org/3/library/asyncio-task.html

'''
# Exapmle 1
import asyncio
# Define a coroutine
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
asyncio.run(main(),debug=True)
'''

'''
# Exapmle 2
# running code syncronously
import asyncio
import time
# Define a coroutine
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())
'''


# Exapmle 3
import asyncio
import time
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())