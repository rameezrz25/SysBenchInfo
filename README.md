# SysBenchInfo

`sysbenchinfo` is a Python package designed to provide comprehensive details about your system's CPU, GPU, memory, and operating system. Additionally, it includes basic benchmarks for both the CPU and GPU, with support for retrieving specific system parameters upon request.

## Features

- Obtain in-depth CPU details such as architecture, model, count, and frequency.
- Get information about GPUs including name, load, memory usage, and temperature.
- Access memory statistics including virtual and swap memory.
- Retrieve OS details including system, node, release, version, machine, and processor.
- Run simple benchmarks to measure CPU and GPU performance.
- Fetch specific parameters of the system based on user requests.

## Installation

To install `sysbenchinfo`, use pip:

```sh
pip install SysBenchInfo
```

Certainly! Here’s a detailed example of how to use the `sysbenchinfo` package, demonstrating its various functionalities:

### Example Usage

#### 1. Basic Usage

```python
from sysbenchinfo import fetch_info

# Specify which parameters you want to fetch
requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']

# Fetch the requested system information
system_info = fetch_info(requested_params)

# Print the information in a human-readable format
for title, data in system_info.items():
    print(f"\n{title}\n")
    if isinstance(data, str):
        print(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            for key, value in item.items():
                print(f"{key}: {value}")
            print("-" * 40)
```

#### 2. Using Specific Functions

If you only need specific information, you can directly call individual functions:

```python
from sysbenchinfo import get_cpu_info, get_gpu_info, get_memory_info, get_os_info, get_python_version, get_java_version, get_benchmarks

# Fetch specific information
cpu_info = get_cpu_info()
gpu_info = get_gpu_info()
memory_info = get_memory_info()
os_info = get_os_info()
python_version = get_python_version()
java_version = get_java_version()
benchmarks = get_benchmarks()

# Print CPU Information
print("CPU Information:")
for key, value in cpu_info.items():
    print(f"{key}: {value}")

# Print GPU Information
print("\nGPU Information:")
if isinstance(gpu_info, str):
    print(gpu_info)
else:
    for gpu in gpu_info:
        for key, value in gpu.items():
            print(f"{key}: {value}")
        print("-" * 40)

# Print Memory Information
print("\nMemory Information:")
for key, value in memory_info.items():
    print(f"{key}: {value}")

# Print OS Information
print("\nOS Information:")
for key, value in os_info.items():
    print(f"{key}: {value}")

# Print Python Version
print("\nPython Version:")
print(python_version)

# Print Java Version
print("\nJava Version:")
print(java_version)

# Print Benchmarks
print("\nBenchmark Results:")
for key, value in benchmarks.items():
    print(f"{key}: {value}")
```
### Example Output

```plaintext

CPU Information

+-----------------+-----------------------------------------------------+
| Category        | Details                                             |
+=================+=====================================================+
| Architecture    | AMD64                                               |
+-----------------+-----------------------------------------------------+
| Model           | Intel64 Family 6 Model 186 Stepping 2, GenuineIntel |
+-----------------+-----------------------------------------------------+
| Logical Cores   | 12                                                  |
+-----------------+-----------------------------------------------------+
| Frequency (MHz) | 2100.0 MHz                                          |
+-----------------+-----------------------------------------------------+

GPU Information

+------+----------------------------------------+--------+--------------------+--------------------+---------------------+-------------------+
|   ID | Name                                   | Load   |   Free Memory (MB) |   Used Memory (MB) |   Total Memory (MB) |   Temperature (C) |
+======+========================================+========+====================+====================+=====================+===================+
|    0 | NVIDIA GeForce RTX 3050 6GB Laptop GPU | 0.00%  |               5.88 |                  0 |                   6 |                41 |
+------+----------------------------------------+--------+--------------------+--------------------+---------------------+-------------------+

Memory Information

+---------------------------------+-----------+
| Category                        |   Details |
+=================================+===========+
| Virtual Memory (Total) (GB)     |     15.65 |
+---------------------------------+-----------+
| Virtual Memory (Available) (GB) |      5.02 |
+---------------------------------+-----------+
| Swap Memory (Total) (GB)        |      2.88 |
+---------------------------------+-----------+
| Swap Memory (Free) (GB)         |      2.7  |
+---------------------------------+-----------+

Operating System Information

+------------+-----------------------------------------------------+
| Category   | Details                                             |
+============+=====================================================+
| System     | Windows                                             |
+------------+-----------------------------------------------------+
| Node       | Victus_HumaiRA                                      |
+------------+-----------------------------------------------------+
| Release    | 11                                                  |
+------------+-----------------------------------------------------+
| Version    | 10.0.22631                                          |
+------------+-----------------------------------------------------+
| Machine    | AMD64                                               |
+------------+-----------------------------------------------------+
| Processor  | Intel64 Family 6 Model 186 Stepping 2, GenuineIntel |
+------------+-----------------------------------------------------+

Python Version

+------------+---------------+
| Category   | Details       |
+============+===============+
| Details    | Python 3.12.4 |
+------------+---------------+

Java Version

+------------+----------------+
| Category   | Details        |
+============+================+
| Details    | Java not found |
+------------+----------------+

Benchmark Results

+------------------------+-----------+
| Category               |   Details |
+========================+===========+
| CPU Benchmark Time (s) |    0.4777 |
+------------------------+-----------+
| GPU Benchmark Time (s) |    4.9888 |
+------------------------+-----------+

CPU Information

+-----------------+-----------------------------------------------------+
| Category        | Details                                             |
+=================+=====================================================+
| Architecture    | AMD64                                               |
+-----------------+-----------------------------------------------------+
| Model           | Intel64 Family 6 Model 186 Stepping 2, GenuineIntel |
+-----------------+-----------------------------------------------------+
| Logical Cores   | 12                                                  |
+-----------------+-----------------------------------------------------+
| Frequency (MHz) | 2100.0 MHz                                          |
+-----------------+-----------------------------------------------------+

GPU Information

+------+----------------------------------------+--------+--------------------+--------------------+---------------------+-------------------+
|   ID | Name                                   | Load   |   Free Memory (MB) |   Used Memory (MB) |   Total Memory (MB) |   Temperature (C) |
+======+========================================+========+====================+====================+=====================+===================+
|    0 | NVIDIA GeForce RTX 3050 6GB Laptop GPU | 0.00%  |               5.88 |                  0 |                   6 |                42 |
+------+----------------------------------------+--------+--------------------+--------------------+---------------------+-------------------+

Memory Information

+---------------------------------+-----------+
| Category                        |   Details |
+=================================+===========+
| Virtual Memory (Total) (GB)     |     15.65 |
+---------------------------------+-----------+
| Virtual Memory (Available) (GB) |      5.07 |
+---------------------------------+-----------+
| Swap Memory (Total) (GB)        |      2.88 |
+---------------------------------+-----------+
| Swap Memory (Free) (GB)         |      2.7  |
+---------------------------------+-----------+

Operating System Information

+------------+-----------------------------------------------------+
| Category   | Details                                             |
+============+=====================================================+
| System     | Windows                                             |
+------------+-----------------------------------------------------+
| Node       | Victus_HumaiRA                                      |
+------------+-----------------------------------------------------+
| Release    | 11                                                  |
+------------+-----------------------------------------------------+
| Version    | 10.0.22631                                          |
+------------+-----------------------------------------------------+
| Machine    | AMD64                                               |
+------------+-----------------------------------------------------+
| Processor  | Intel64 Family 6 Model 186 Stepping 2, GenuineIntel |
+------------+-----------------------------------------------------+

Python Version

+------------+---------------+
| Category   | Details       |
+============+===============+
| Details    | Python 3.12.4 |
+------------+---------------+

Java Version

+------------+----------------+
| Category   | Details        |
+============+================+
| Details    | Java not found |
+------------+----------------+

Benchmark Results

+------------------------+-----------+
| Category               |   Details |
+========================+===========+
| CPU Benchmark Time (s) |    0.5112 |
+------------------------+-----------+
| GPU Benchmark Time (s) |    5.0473 |
+------------------------+-----------+

CPU Information

+-----------------+-----------------------------------------------------+
| Category        | Details                                             |
+=================+=====================================================+
| Architecture    | AMD64                                               |
+-----------------+-----------------------------------------------------+
| Model           | Intel64 Family 6 Model 186 Stepping 2, GenuineIntel |
+-----------------+-----------------------------------------------------+
| Logical Cores   | 12                                                  |
+-----------------+-----------------------------------------------------+
| Frequency (MHz) | 2100.0 MHz                                          |
+-----------------+-----------------------------------------------------+

GPU Information

+------+----------------------------------------+--------+--------------------+--------------------+---------------------+-------------------+
|   ID | Name                                   | Load   |   Free Memory (MB) |   Used Memory (MB) |   Total Memory (MB) |   Temperature (C) |
+======+========================================+========+====================+====================+=====================+===================+
|    0 | NVIDIA GeForce RTX 3050 6GB Laptop GPU | 0.00%  |               5.88 |                  0 |                   6 |                42 |
+------+----------------------------------------+--------+--------------------+--------------------+---------------------+-------------------+

Memory Information

+---------------------------------+-----------+
| Category                        |   Details |
+=================================+===========+
| Virtual Memory (Total) (GB)     |     15.65 |
+---------------------------------+-----------+
| Virtual Memory (Available) (GB) |      5.08 |
+---------------------------------+-----------+
| Swap Memory (Total) (GB)        |      2.88 |
+---------------------------------+-----------+
| Swap Memory (Free) (GB)         |      2.7  |
+---------------------------------+-----------+

Operating System Information

+------------+-----------------------------------------------------+
| Category   | Details                                             |
+============+=====================================================+
| System     | Windows                                             |
+------------+-----------------------------------------------------+
| Node       | Victus_HumaiRA                                      |
+------------+-----------------------------------------------------+
| Release    | 11                                                  |
+------------+-----------------------------------------------------+
| Version    | 10.0.22631                                          |
+------------+-----------------------------------------------------+
| Machine    | AMD64                                               |
+------------+-----------------------------------------------------+
| Processor  | Intel64 Family 6 Model 186 Stepping 2, GenuineIntel |
+------------+-----------------------------------------------------+

Python Version

+------------+---------------+
| Category   | Details       |
+============+===============+
| Details    | Python 3.12.4 |
+------------+---------------+

Java Version

+------------+----------------+
| Category   | Details        |
+============+================+
| Details    | Java not found |
+------------+----------------+

Benchmark Results

+------------------------+-----------+
| Category               |   Details |
+========================+===========+
| CPU Benchmark Time (s) |    0.5056 |
+------------------------+-----------+
| GPU Benchmark Time (s) |    5.1672 |
+------------------------+-----------+
```

## Available Functions

- **`get_cpu_info()`**: Returns detailed CPU information.
- **`get_gpu_info()`**: Returns detailed GPU information.
- **`get_memory_info()`**: Returns detailed memory information.
- **`get_os_info()`**: Returns detailed OS information.
- **`get_python_version()`**: Returns the Python version.
- **`get_java_version()`**: Returns the Java version.
- **`get_benchmarks()`**: Returns benchmark results for CPU and GPU.
- **`fetch_info(requested_params)`**: Fetches specific parameters based on the provided list of requests.


### Summary

- **`fetch_info(requested_params)`**: Allows you to fetch a specific set of system parameters. You pass a list of strings indicating which parameters you want (`'cpu'`, `'gpu'`, `'memory'`, `'os'`, `'python'`, `'java'`, `'benchmarks'`).

- **Direct Functions**: Use `get_cpu_info()`, `get_gpu_info()`, `get_memory_info()`, `get_os_info()`, `get_python_version()`, `get_java_version()`, and `get_benchmarks()` to fetch and print specific types of system information.

Each function and example shows how to fetch and display different types of system information in a user-friendly format. Adjust the example based on your specific requirements or the format you prefer.

