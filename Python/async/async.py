#!/usr/bin/env python3
# Synchronous Programming
def foo():
    return
foo()
print('Hello')

# Asynchronous Programming
import asyncio

async def main():
    print('Hello')
    # await foo2('Functioned!')
    text = asyncio.create_task(foo2('Functioned!'))
    print('Run before async')

async def foo2(text):
    print(text)
    await asyncio.sleep(3)

# asyncio.run(foo2('OliOli'))
# print('Not async!')
asyncio.run(main())

# Future
async def fetch_data():
    print('Start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    await task2
asyncio.run(main())