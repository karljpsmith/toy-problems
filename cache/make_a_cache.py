# Homework for SDE study club: write a get_value() method that takes advantage of the pre-build caches
# to get the lowest possible score.

import numpy as np

score = 0

SMALL_CACHE_MEM_SIZE = 500
SMALL_CACHE_WRITE_COST = 1
SMALL_CACHE_READ_COST = 1

LARGE_CACHE_MEM_SIZE = 5000
LARGE_CACHE_WRITE_COST = 10
LARGE_CACHE_READ_COST = 10

DISK_MEM_SIZE = 1000000
DISK_MEM_WRITE_COST = 1000
DISK_MEM_READ_COST = 1000

TEST_SIZE = 1000000
standard_dev = 100
NUMBER_TIMES_TO_SHIFT_INPUT = 3


class SmallCache:
    def __init__(self):
        self.memory = np.zeros(SMALL_CACHE_MEM_SIZE)

    def read(self, index):
        global score
        score += SMALL_CACHE_READ_COST
        return self.memory[index]

    def write(self, index, value):
        global score
        score += SMALL_CACHE_WRITE_COST
        self.memory[index] = value


class LargeCache:
    def __init__(self):
        self.memory = np.zeros(LARGE_CACHE_MEM_SIZE)

    def read(self, index):
        global score
        score += LARGE_CACHE_READ_COST
        return self.memory[index]

    def write(self, index, value):
        global score
        score += LARGE_CACHE_WRITE_COST
        self.memory[index] = value


class DiskMemory:
    def __init__(self):
        self.memory = np.random.rand(DISK_MEM_SIZE)

    def read(self, index):
        global score
        score += DISK_MEM_READ_COST
        return self.memory[index]

    def write(self, index, value):
        global score
        score += DISK_MEM_WRITE_COST
        self.memory[index] = value

    def check(self, index):
        # THIS METHOD IS FOR CHECKING ONLY - YOU CANNOT USE IT FOR YOUR READS
        return self.memory[index]


disk = DiskMemory()
small_cache = SmallCache()
large_cache = LargeCache()


def generate_normal_dist_random_number(centerpoint):
    # Generates a pseudo-random number according to a normal distribution centered around centerpoint
    return int(np.random.normal(centerpoint, standard_dev))


def get_value(to_read):
    # PUT YOUR CODE HERE
    # Right now this reads from disk each time, which is the most expensive read operation by a lot.
    # You should cache these disk reads in your large and small caches
    return disk.read(to_read)


def get_centerpoint():
    return np.random.randint(standard_dev, DISK_MEM_SIZE-standard_dev)


def run_test():
    for i in range(0, TEST_SIZE):

        if i % int(TEST_SIZE/NUMBER_TIMES_TO_SHIFT_INPUT) == 0:
            centerpoint = get_centerpoint()
            # reset the center of our normal distribution, so that the caches will need to adapt

        to_read = generate_normal_dist_random_number(centerpoint)
        candidate_value = get_value(to_read)

        if candidate_value != DiskMemory.check(disk, to_read):
            raise ValueError('Error reading from disk')

    print("Score: {}".format(score))


run_test()
