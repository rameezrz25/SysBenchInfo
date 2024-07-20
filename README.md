Sure! Here's a rephrased version for `sysbenchinfo`:

---

# SysBenchInfo

`sysbenchinfo` is a Python package designed to provide comprehensive details about your system's CPU, GPU, memory, and operating system. Additionally, it includes basic benchmarks for both the CPU and GPU.

## Features

- Obtain in-depth CPU details such as architecture, model, count, and frequency.
- Get information about GPUs including name, load, memory usage, and temperature.
- Access memory statistics including virtual and swap memory.
- Retrieve OS details including system, node, release, version, machine, and processor.
- Run simple benchmarks to measure CPU and GPU performance.

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
>>> from sysbenchinfo import get_system_info
>>>
>>> info = get_system_info()
>>> print(info)
{'cpu': {'architecture': 'AMD64', 'model': 'Intel64 Family 6 Model 186 Stepping 2, GenuineIntel', 'count': 12, 'frequency': {'current': 2100.0, 'min': 0.0, 'max': 2100.0}}, 'gpu': [{'id': 0, 'name': 'NVIDIA GeForce RTX 3050 6GB Laptop GPU', 'load': 0.0, 'free_memory': 6017.0, 'used_memory': 0.0, 'total_memory': 6144.0, 'temperature': 45.0}], 'memory': {'virtual_memory': {'total': 16802922496, 'available': 6167236608, 'percent': 63.3, 'used': 10635685888, 'free': 6167236608}, 'swap_memory': {'total': 3087007744, 'used': 100864000, 'free': 2986143744, 'percent': 3.3, 'sin': 0, 'sout': 0}}, 'os': {'system': 'Windows', 'node': 'Victus_HumaiRA', 'release': '11', 'version': '10.0.22631', 'machine': 'AMD64', 'processor': 'Intel64 Family 6 Model 186 Stepping 2, GenuineIntel'}, 'benchmarks': {'cpu_benchmark': 0.5434212000109255, 'gpu_benchmark': {'gpu_name': 'NVIDIA GeForce RTX 3050 6GB Laptop GPU', 'benchmark_time': 5.055665799998678}}}
```

---
