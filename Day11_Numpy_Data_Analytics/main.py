import numpy as np
import time

def create_arrays():
    arr = np.array([10, 20, 30, 40, 50])
    print("Array:", arr)
    print("Shape:", arr.shape)
    print("Data Type:", arr.dtype)
    print("-" * 40)

def array_operations():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Addition:", a + b)
    print("Multiplication:", a * b)
    print("Broadcasting:", a + 5)
    print("-" * 40)

def reshaping_demo():
    arr = np.arange(1, 13)
    print("Original Array:", arr)
    reshaped = arr.reshape(3, 4)
    print("Reshaped (3x4):\n", reshaped)
    print("-" * 40)

def statistics_demo():
    data = np.array([5, 10, 15, 20, 25])
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Standard Deviation:", np.std(data))
    print("Sum:", np.sum(data))
    print("-" * 40)

def performance_comparison():
    size = 1_000_000
    py_list = list(range(size))
    np_array = np.arange(size)

    start = time.time()
    py_sum = [x * 2 for x in py_list]
    end = time.time()
    print(f"Python list time: {end - start:.4f} sec")

    start = time.time()
    np_sum = np_array * 2
    end = time.time()
    print(f"NumPy array time: {end - start:.4f} sec")
    print("-" * 40)

def main():
    print("NumPy Data Analytics Toolkit\n")
    create_arrays()
    array_operations()
    reshaping_demo()
    statistics_demo()
    performance_comparison()

if __name__ == "__main__":
    main()