import asyncio
async def async_task(name, delay):
    print(f"Task {name} starting with delay {delay}")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.gather(async_task("A", 3), async_task("B", 1)))
loop.close()
