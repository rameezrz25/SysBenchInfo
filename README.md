# System Info

`system_info` is a Python package that provides detailed information about your system's CPU, GPU, memory, and operating system. It also includes simple benchmarks for the CPU and GPU.

## Features

- Retrieve detailed CPU information including architecture, model, count, and frequency.
- Retrieve detailed GPU information including name, load, memory usage, and temperature.
- Retrieve detailed memory information including virtual and swap memory.
- Retrieve detailed OS information including system, node, release, version, machine, and processor.
- Perform simple CPU and GPU benchmarks.

## Installation

You can install the `system_info` package using pip:

```sh
pip install system_info

C:\Users\humai\Downloads\Rameez\SysBenchInfo\dist>python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from sysbenchinfo import get_system_info
>>>
>>> info = get_system_info()
>>> print(info)
{'cpu': {'architecture': 'AMD64', 'model': 'Intel64 Family 6 Model 186 Stepping 2, GenuineIntel', 'count': 12, 'frequency': {'current': 2100.0, 'min': 0.0, 'max': 2100.0}}, 'gpu': [{'id': 0, 'name': 'NVIDIA GeForce RTX 3050 6GB Laptop GPU', 'load': 0.0, 'free_memory': 6017.0, 'used_memory': 0.0, 'total_memory': 6144.0, 'temperature': 45.0}], 'memory': {'virtual_memory': {'total': 16802922496, 'available': 6167236608, 'percent': 63.3, 'used': 10635685888, 'free': 6167236608}, 'swap_memory': {'total': 3087007744, 'used': 100864000, 'free': 2986143744, 'percent': 3.3, 'sin': 0, 'sout': 0}}, 'os': {'system': 'Windows', 'node': 'Victus_HumaiRA', 'release': '11', 'version': '10.0.22631', 'machine': 'AMD64', 'processor': 'Intel64 Family 6 Model 186 Stepping 2, GenuineIntel'}, 'benchmarks': {'cpu_benchmark': 0.5434212000109255, 'gpu_benchmark': {'gpu_name': 'NVIDIA GeForce RTX 3050 6GB Laptop GPU', 'benchmark_time': 5.055665799998678}}}
