import time
import asyncio

def accumulate(n):
    result=1
    for i in range(n,1,-1):
        result+=i
        time.sleep(0.01)
    print(f"->{n}的结果：{result}")

async def accumulateasync(n):
    result=1
    for i in range(n,1,-1):
        result+=i
        await asyncio.sleep(0.01)
    print(f"->{n}的结果：{result}")



def main1():
    print(time.strftime('%X'))
    accumulate(800)
    accumulate(500)
    accumulate(100)
    print(time.strftime('%X'))
async def main2():
    print(time.strftime('%X'))
    # await accumulate(800)
    # await accumulate(500)
    # await accumulate(100)
    task1=asyncio.create_task(accumulateasync(800))
    task2=asyncio.create_task(accumulateasync(500))
    task3=asyncio.create_task(accumulateasync(100))
    await task1
    await task2
    await task3
    print(time.strftime('%X'))
main1()
asyncio.run(main2())