"""

Imagine you're a chef in a kitchen, and you have three tasks to complete:

1-Boiling Water (Task 1): It takes 2 minutes.
2-Chopping Vegetables (Task 2): It takes 1 minute.
3-Baking a Cake (Task 3): It takes 3 minutes.

In traditional cooking (synchronous way), you would do these tasks one after the other:

Start boiling water.
Wait for 2 minutes until the water boils.
Start chopping vegetables.
Wait for 1 minute until the vegetables are chopped.
Start baking the cake.
Wait for 3 minutes until the cake is baked.
Total time: 2 + 1 + 3 = 6 minutes.

Now, let's use the async cooking approach:

Start boiling water.
While waiting for water to boil, start chopping vegetables.
While waiting for vegetables to be chopped, start baking the cake.
You're not just waiting idly; you're using the time efficiently by doing other tasks. This is similar to how async works.

"""

import asyncio

async def boil_water():
    print("Start boiling water")
    await asyncio.sleep(2)
    print("End boiling water")

async def chop_vegetables():
    print("Start chopping vegetables")
    await asyncio.sleep(1)
    print("End chopping vegetables")

async def bake_cake():
    print("Start baking cake")
    await asyncio.sleep(3)
    print("End baking cake")

async def main():

    # Using asyncio.gather to run tasks concurrently

    await asyncio.gather(boil_water(), chop_vegetables(), bake_cake())

# Run the async main function

asyncio.run(main())



