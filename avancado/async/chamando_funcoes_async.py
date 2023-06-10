import asyncio

async def func1():
    print("FUNC1")


async def func2():
    print("FUNC2")
    await asyncio.sleep(1)


async def func3():
    print("FUNC3")

async def main():
    tasks = [func1(), func2(), func3()]
    await asyncio.gather(*tasks)

asyncio.run(main())
