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

## Usage

Here is an example of how to use `sysbenchinfo` in a Python environment:

```sh
C:\Users\humai\Downloads\Rameez\SysBenchInfo\dist>python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from sysbenchinfo import fetch_info
>>>
>>> # Fetch specific parameters
>>> requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
>>> system_info = fetch_info(requested_params)
>>> for title, data in system_info.items():
...     print(f"\n{title}\n")
...     print(data)
```

### Example Output

```plaintext
Operating System Information
{'System': 'Windows', 'Node': 'Victus_HumaiRA', 'Release': '11', 'Version': '10.0.22631', 'Machine': 'AMD64', 'Processor': 'Intel64 Family 6 Model 186 Stepping 2, GenuineIntel'}

CPU Information
{'Architecture': 'AMD64', 'Model': 'Intel64 Family 6 Model 186 Stepping 2, GenuineIntel', 'Logical Cores': 12, 'Frequency (MHz)': '2100.0 MHz'}

Memory Information
{'Virtual Memory (Total) (GB)': '15.67', 'Virtual Memory (Available) (GB)': '5.74', 'Swap Memory (Total) (GB)': '2.87', 'Swap Memory (Free) (GB)': '2.78'}

Python Version
Python 3.12.4

Java Version
Java 17.0.1

GPU Information
ID    Name                                Load   Free Memory (MB)   Used Memory (MB)   Total Memory (MB)   Temperature (C)
0     NVIDIA GeForce RTX 3050 6GB Laptop GPU   0.00%   6017.00   0.00   6144.00   45.00

Benchmark Results
{'CPU Benchmark Time (s)': '0.5434', 'GPU Benchmark Time (s)': '5.0557'}
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

