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

After installing the `sysbenchinfo` package, you can use it to gather and display system information.

### Using `get_system_info`

You can retrieve and print system information with the following code:

```python
from sysbenchinfo import get_system_info

# Get system information
info = get_system_info()

# Print system information
print(info)
