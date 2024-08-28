import time


def boil_water():
    print("Start boiling water")
    time.sleep(2)
    print("End boiling water")


def chop_vegetables():
    print("Start chopping vegetables")
    time.sleep(1)
    print("End chopping vegetables")


def bake_cake():
    print("Start baking cake")
    time.sleep(3)
    print("End baking cake")


def main():
    boil_water()
    chop_vegetables()
    bake_cake()
    return "Success"


print(main())
