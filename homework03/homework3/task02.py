import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def run_slow_calculate():
    numbers = [i for i in range(500)]
    number_of_processes = 25
    start = time.time()
    with Pool(number_of_processes) as p:
        slow_calculate(p.map(slow_calculate, numbers))
    end = time.time()
    # print(f'calculation time {end - start = } seconds')
    return end - start
