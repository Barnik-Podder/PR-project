import time
import concurrent.futures
import numpy as np
import psutil
import tkinter as tk
from tkinter import scrolledtext

def cpu_info():
    """Print CPU information."""
    info = "CPU Information\n"
    info += "================\n"
    info += f"Physical cores: {psutil.cpu_count(logical=False)}\n"
    info += f"Total cores: {psutil.cpu_count(logical=True)}\n"
    cpufreq = psutil.cpu_freq()
    info += f"Max Frequency: {cpufreq.max:.2f}Mhz\n"
    info += f"Min Frequency: {cpufreq.min:.2f}Mhz\n"
    info += f"Current Frequency: {cpufreq.current:.2f}Mhz\n"
    return info

def benchmark_integer_operations():
    """Benchmark integer operations."""
    start = time.time()
    total = 0
    for i in range(1, 100000000):
        total += i
    end = time.time()
    return f"Time taken for integer operations: {end - start:.2f} seconds\n"

def benchmark_floating_point_operations():
    """Benchmark floating-point operations."""
    start = time.time()
    total = 0.0
    for i in range(1, 100000000):
        total += 1.0 / i
    end = time.time()
    return f"Time taken for floating-point operations: {end - start:.2f} seconds\n"

def benchmark_memory_throughput():
    """Benchmark memory throughput using numpy."""
    array_size = 100000000
    start = time.time()
    a = np.random.rand(array_size)
    b = np.random.rand(array_size)
    c = a + b
    end = time.time()
    return f"Time taken for memory operations: {end - start:.2f} seconds\n"

def worker():
    """Function to simulate workload for multiprocessing."""
    total = 0
    for i in range(1, 10000000):
        total += i

def benchmark_multithreading():
    """Benchmark multi-threading performance."""
    num_threads = psutil.cpu_count(logical=True)
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(worker) for _ in range(num_threads)]
        concurrent.futures.wait(futures)
    end = time.time()
    return f"Time taken with {num_threads} threads: {end - start:.2f} seconds\n"

def clear_and_display_result(result):
    """Clear the output text widget and display the result."""
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

def show_cpu_info():
    result = cpu_info()
    clear_and_display_result(result)

def run_integer_benchmark():
    result = benchmark_integer_operations()
    clear_and_display_result(result)

def run_floating_benchmark():
    result = benchmark_floating_point_operations()
    clear_and_display_result(result)

def run_memory_benchmark():
    result = benchmark_memory_throughput()
    clear_and_display_result(result)

def run_multithreading_benchmark():
    result = benchmark_multithreading()
    clear_and_display_result(result)

# Create the main window
root = tk.Tk()
root.title("CPU Benchmarking Tool")

# Create a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
output_text.grid(column=0, row=0, columnspan=4)

# Create buttons for each benchmark
cpu_info_button = tk.Button(root, text="CPU Info", command=show_cpu_info)
cpu_info_button.grid(column=0, row=1, padx=10, pady=10)

integer_benchmark_button = tk.Button(root, text="Integer Operations Benchmark", command=run_integer_benchmark)
integer_benchmark_button.grid(column=1, row=1, padx=10, pady=10)

floating_benchmark_button = tk.Button(root, text="Floating-Point Operations Benchmark", command=run_floating_benchmark)
floating_benchmark_button.grid(column=2, row=1, padx=10, pady=10)

memory_benchmark_button = tk.Button(root, text="Memory Throughput Benchmark", command=run_memory_benchmark)
memory_benchmark_button.grid(column=3, row=1, padx=10, pady=10)

multithreading_benchmark_button = tk.Button(root, text="Multi-threading Benchmark", command=run_multithreading_benchmark)
multithreading_benchmark_button.grid(column=0, row=2, columnspan=4, padx=10, pady=10)

# Run the GUI main loop
root.mainloop()