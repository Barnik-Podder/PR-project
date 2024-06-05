import time
import multiprocessing
import numpy as np
import psutil

def cpu_info():
    """Print CPU information."""
    print("CPU Information")
    print("================")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

def benchmark_integer_operations():
    """Benchmark integer operations."""
    print("\nInteger Operations Benchmark")
    print("============================")
    start = time.time()
    total = 0
    for i in range(1, 100000000):
        total += i
    end = time.time()
    print(f"Time taken for integer operations: {end - start:.2f} seconds")

def benchmark_floating_point_operations():
    """Benchmark floating-point operations."""
    print("\nFloating-Point Operations Benchmark")
    print("===================================")
    start = time.time()
    total = 0.0
    for i in range(1, 100000000):
        total += 1.0 / i
    end = time.time()
    print(f"Time taken for floating-point operations: {end - start:.2f} seconds")

def benchmark_memory_throughput():
    """Benchmark memory throughput using numpy."""
    print("\nMemory Throughput Benchmark")
    print("===========================")
    array_size = 100000000
    start = time.time()
    a = np.random.rand(array_size)
    b = np.random.rand(array_size)
    c = a + b
    end = time.time()
    print(f"Time taken for memory operations: {end - start:.2f} seconds")

def worker():
    """Function to simulate workload for multiprocessing."""
    total = 0
    for i in range(1, 10000000):
        total += i

def benchmark_multithreading():
    """Benchmark multi-threading performance."""
    print("\nMulti-threading Benchmark")
    print("==========================")
    num_processes = psutil.cpu_count(logical=True)
    processes = []
    start = time.time()
    for _ in range(num_processes):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    print(f"Time taken with {num_processes} threads: {end - start:.2f} seconds")

if __name__ == "__main__":
    cpu_info()
    benchmark_integer_operations()
    benchmark_floating_point_operations()
    benchmark_memory_throughput()
    benchmark_multithreading()
