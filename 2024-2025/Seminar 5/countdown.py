import time

def countdown(n):
    if (n == 0):
        return
    time.sleep(1)
    print(n)
    countdown(n - 1)

countdown(10)