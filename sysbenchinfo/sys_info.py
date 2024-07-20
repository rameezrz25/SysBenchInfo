import platform
import psutil
import GPUtil
import timeit
import subprocess
from tabulate import tabulate

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Frequency (MHz)": f"{psutil.cpu_freq().current} MHz" if psutil.cpu_freq() else "N/A"
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load": f"{gpu.load * 100:.2f}%",
            "Free Memory (MB)": f"{gpu.memoryFree / 1024:.2f}",
            "Used Memory (MB)": f"{gpu.memoryUsed / 1024:.2f}",
            "Total Memory (MB)": f"{gpu.memoryTotal / 1024:.2f}",
            "Temperature (C)": gpu.temperature
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (Total) (GB)": f"{virtual_mem.total / (1024 ** 3):.2f}",
        "Virtual Memory (Available) (GB)": f"{virtual_mem.available / (1024 ** 3):.2f}",
        "Swap Memory (Total) (GB)": f"{swap_mem.total / (1024 ** 3):.2f}",
        "Swap Memory (Free) (GB)": f"{swap_mem.free / (1024 ** 3):.2f}",
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_python_version():
    return f"Python {platform.python_version()}"

def get_java_version():
    try:
        result = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
        java_version = result.stderr.split('\n')[0].split('"')[1]
        return f"Java {java_version}"
    except FileNotFoundError:
        return "Java not found"

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark Time (s)": f"{cpu_benchmark():.4f}",
        "GPU Benchmark Time (s)": f"{gpu_benchmark().get('benchmark_time', 'N/A'):.4f}"
    }
    return benchmarks

def cpu_benchmark():
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"gpu_name": "N/A", "benchmark_time": 0}
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return {"gpu_name": "Error", "benchmark_time": str(e)}

def print_table(data, title):
    headers = ["Category", "Details"]
    if isinstance(data, dict):
        table = [(k, v) for k, v in data.items()]
    elif isinstance(data, str):
        table = [("Details", data)]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = data[0].keys()
        table = [list(gpu.values()) for gpu in data]
    else:
        table = []
    
    print(f"\n{title}\n")
    print(tabulate(table, headers, tablefmt="grid"))

def fetch_info(requested_params):
    results = {}
    if 'cpu' in requested_params:
        results['CPU Information'] = get_cpu_info()
    if 'gpu' in requested_params:
        results['GPU Information'] = get_gpu_info()
    if 'memory' in requested_params:
        results['Memory Information'] = get_memory_info()
    if 'os' in requested_params:
        results['Operating System Information'] = get_os_info()
    if 'python' in requested_params:
        results['Python Version'] = get_python_version()
    if 'java' in requested_params:
        results['Java Version'] = get_java_version()
    if 'benchmarks' in requested_params:
        results['Benchmark Results'] = get_benchmarks()
    
    return results

if __name__ == "__main__":
    # Example usage: specify which parameters you want to fetch
    requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
    system_info = fetch_info(requested_params)
    
    # Print the requested system information
    for title, data in system_info.items():
        print_table(data, title)
import platform
import psutil
import GPUtil
import timeit
import subprocess
from tabulate import tabulate

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Frequency (MHz)": f"{psutil.cpu_freq().current} MHz" if psutil.cpu_freq() else "N/A"
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load": f"{gpu.load * 100:.2f}%",
            "Free Memory (MB)": f"{gpu.memoryFree / 1024:.2f}",
            "Used Memory (MB)": f"{gpu.memoryUsed / 1024:.2f}",
            "Total Memory (MB)": f"{gpu.memoryTotal / 1024:.2f}",
            "Temperature (C)": gpu.temperature
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (Total) (GB)": f"{virtual_mem.total / (1024 ** 3):.2f}",
        "Virtual Memory (Available) (GB)": f"{virtual_mem.available / (1024 ** 3):.2f}",
        "Swap Memory (Total) (GB)": f"{swap_mem.total / (1024 ** 3):.2f}",
        "Swap Memory (Free) (GB)": f"{swap_mem.free / (1024 ** 3):.2f}",
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_python_version():
    return f"Python {platform.python_version()}"

def get_java_version():
    try:
        result = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
        java_version = result.stderr.split('\n')[0].split('"')[1]
        return f"Java {java_version}"
    except FileNotFoundError:
        return "Java not found"

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark Time (s)": f"{cpu_benchmark():.4f}",
        "GPU Benchmark Time (s)": f"{gpu_benchmark().get('benchmark_time', 'N/A'):.4f}"
    }
    return benchmarks

def cpu_benchmark():
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"gpu_name": "N/A", "benchmark_time": 0}
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return {"gpu_name": "Error", "benchmark_time": str(e)}

def print_table(data, title):
    headers = ["Category", "Details"]
    if isinstance(data, dict):
        table = [(k, v) for k, v in data.items()]
    elif isinstance(data, str):
        table = [("Details", data)]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = data[0].keys()
        table = [list(gpu.values()) for gpu in data]
    else:
        table = []
    
    print(f"\n{title}\n")
    print(tabulate(table, headers, tablefmt="grid"))

def fetch_info(requested_params):
    results = {}
    if 'cpu' in requested_params:
        results['CPU Information'] = get_cpu_info()
    if 'gpu' in requested_params:
        results['GPU Information'] = get_gpu_info()
    if 'memory' in requested_params:
        results['Memory Information'] = get_memory_info()
    if 'os' in requested_params:
        results['Operating System Information'] = get_os_info()
    if 'python' in requested_params:
        results['Python Version'] = get_python_version()
    if 'java' in requested_params:
        results['Java Version'] = get_java_version()
    if 'benchmarks' in requested_params:
        results['Benchmark Results'] = get_benchmarks()
    
    return results

if __name__ == "__main__":
    # Example usage: specify which parameters you want to fetch
    requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
    system_info = fetch_info(requested_params)
    
    # Print the requested system information
    for title, data in system_info.items():
        print_table(data, title)
import platform
import psutil
import GPUtil
import timeit
import subprocess
from tabulate import tabulate

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Frequency (MHz)": f"{psutil.cpu_freq().current} MHz" if psutil.cpu_freq() else "N/A"
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load": f"{gpu.load * 100:.2f}%",
            "Free Memory (MB)": f"{gpu.memoryFree / 1024:.2f}",
            "Used Memory (MB)": f"{gpu.memoryUsed / 1024:.2f}",
            "Total Memory (MB)": f"{gpu.memoryTotal / 1024:.2f}",
            "Temperature (C)": gpu.temperature
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (Total) (GB)": f"{virtual_mem.total / (1024 ** 3):.2f}",
        "Virtual Memory (Available) (GB)": f"{virtual_mem.available / (1024 ** 3):.2f}",
        "Swap Memory (Total) (GB)": f"{swap_mem.total / (1024 ** 3):.2f}",
        "Swap Memory (Free) (GB)": f"{swap_mem.free / (1024 ** 3):.2f}",
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_python_version():
    return f"Python {platform.python_version()}"

def get_java_version():
    try:
        result = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
        java_version = result.stderr.split('\n')[0].split('"')[1]
        return f"Java {java_version}"
    except FileNotFoundError:
        return "Java not found"

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark Time (s)": f"{cpu_benchmark():.4f}",
        "GPU Benchmark Time (s)": f"{gpu_benchmark().get('benchmark_time', 'N/A'):.4f}"
    }
    return benchmarks

def cpu_benchmark():
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"gpu_name": "N/A", "benchmark_time": 0}
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return {"gpu_name": "Error", "benchmark_time": str(e)}

def print_table(data, title):
    headers = ["Category", "Details"]
    if isinstance(data, dict):
        table = [(k, v) for k, v in data.items()]
    elif isinstance(data, str):
        table = [("Details", data)]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = data[0].keys()
        table = [list(gpu.values()) for gpu in data]
    else:
        table = []
    
    print(f"\n{title}\n")
    print(tabulate(table, headers, tablefmt="grid"))

def fetch_info(requested_params):
    results = {}
    if 'cpu' in requested_params:
        results['CPU Information'] = get_cpu_info()
    if 'gpu' in requested_params:
        results['GPU Information'] = get_gpu_info()
    if 'memory' in requested_params:
        results['Memory Information'] = get_memory_info()
    if 'os' in requested_params:
        results['Operating System Information'] = get_os_info()
    if 'python' in requested_params:
        results['Python Version'] = get_python_version()
    if 'java' in requested_params:
        results['Java Version'] = get_java_version()
    if 'benchmarks' in requested_params:
        results['Benchmark Results'] = get_benchmarks()
    
    return results

if __name__ == "__main__":
    # Example usage: specify which parameters you want to fetch
    requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
    system_info = fetch_info(requested_params)
    
    # Print the requested system information
    for title, data in system_info.items():
        print_table(data, title)
import platform
import psutil
import GPUtil
import timeit
import subprocess
from tabulate import tabulate

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Frequency (MHz)": f"{psutil.cpu_freq().current} MHz" if psutil.cpu_freq() else "N/A"
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load": f"{gpu.load * 100:.2f}%",
            "Free Memory (MB)": f"{gpu.memoryFree / 1024:.2f}",
            "Used Memory (MB)": f"{gpu.memoryUsed / 1024:.2f}",
            "Total Memory (MB)": f"{gpu.memoryTotal / 1024:.2f}",
            "Temperature (C)": gpu.temperature
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (Total) (GB)": f"{virtual_mem.total / (1024 ** 3):.2f}",
        "Virtual Memory (Available) (GB)": f"{virtual_mem.available / (1024 ** 3):.2f}",
        "Swap Memory (Total) (GB)": f"{swap_mem.total / (1024 ** 3):.2f}",
        "Swap Memory (Free) (GB)": f"{swap_mem.free / (1024 ** 3):.2f}",
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_python_version():
    return f"Python {platform.python_version()}"

def get_java_version():
    try:
        result = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
        java_version = result.stderr.split('\n')[0].split('"')[1]
        return f"Java {java_version}"
    except FileNotFoundError:
        return "Java not found"

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark Time (s)": f"{cpu_benchmark():.4f}",
        "GPU Benchmark Time (s)": f"{gpu_benchmark().get('benchmark_time', 'N/A'):.4f}"
    }
    return benchmarks

def cpu_benchmark():
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"gpu_name": "N/A", "benchmark_time": 0}
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return {"gpu_name": "Error", "benchmark_time": str(e)}

def print_table(data, title):
    headers = ["Category", "Details"]
    if isinstance(data, dict):
        table = [(k, v) for k, v in data.items()]
    elif isinstance(data, str):
        table = [("Details", data)]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = data[0].keys()
        table = [list(gpu.values()) for gpu in data]
    else:
        table = []
    
    print(f"\n{title}\n")
    print(tabulate(table, headers, tablefmt="grid"))

def fetch_info(requested_params):
    results = {}
    if 'cpu' in requested_params:
        results['CPU Information'] = get_cpu_info()
    if 'gpu' in requested_params:
        results['GPU Information'] = get_gpu_info()
    if 'memory' in requested_params:
        results['Memory Information'] = get_memory_info()
    if 'os' in requested_params:
        results['Operating System Information'] = get_os_info()
    if 'python' in requested_params:
        results['Python Version'] = get_python_version()
    if 'java' in requested_params:
        results['Java Version'] = get_java_version()
    if 'benchmarks' in requested_params:
        results['Benchmark Results'] = get_benchmarks()
    
    return results

if __name__ == "__main__":
    # Example usage: specify which parameters you want to fetch
    requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
    system_info = fetch_info(requested_params)
    
    # Print the requested system information
    for title, data in system_info.items():
        print_table(data, title)
import platform
import psutil
import GPUtil
import timeit
import subprocess
from tabulate import tabulate

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Frequency (MHz)": f"{psutil.cpu_freq().current} MHz" if psutil.cpu_freq() else "N/A"
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load": f"{gpu.load * 100:.2f}%",
            "Free Memory (MB)": f"{gpu.memoryFree / 1024:.2f}",
            "Used Memory (MB)": f"{gpu.memoryUsed / 1024:.2f}",
            "Total Memory (MB)": f"{gpu.memoryTotal / 1024:.2f}",
            "Temperature (C)": gpu.temperature
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (Total) (GB)": f"{virtual_mem.total / (1024 ** 3):.2f}",
        "Virtual Memory (Available) (GB)": f"{virtual_mem.available / (1024 ** 3):.2f}",
        "Swap Memory (Total) (GB)": f"{swap_mem.total / (1024 ** 3):.2f}",
        "Swap Memory (Free) (GB)": f"{swap_mem.free / (1024 ** 3):.2f}",
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_python_version():
    return f"Python {platform.python_version()}"

def get_java_version():
    try:
        result = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
        java_version = result.stderr.split('\n')[0].split('"')[1]
        return f"Java {java_version}"
    except FileNotFoundError:
        return "Java not found"

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark Time (s)": f"{cpu_benchmark():.4f}",
        "GPU Benchmark Time (s)": f"{gpu_benchmark().get('benchmark_time', 'N/A'):.4f}"
    }
    return benchmarks

def cpu_benchmark():
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"gpu_name": "N/A", "benchmark_time": 0}
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return {"gpu_name": "Error", "benchmark_time": str(e)}

def print_table(data, title):
    headers = ["Category", "Details"]
    if isinstance(data, dict):
        table = [(k, v) for k, v in data.items()]
    elif isinstance(data, str):
        table = [("Details", data)]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = data[0].keys()
        table = [list(gpu.values()) for gpu in data]
    else:
        table = []
    
    print(f"\n{title}\n")
    print(tabulate(table, headers, tablefmt="grid"))

def fetch_info(requested_params):
    results = {}
    if 'cpu' in requested_params:
        results['CPU Information'] = get_cpu_info()
    if 'gpu' in requested_params:
        results['GPU Information'] = get_gpu_info()
    if 'memory' in requested_params:
        results['Memory Information'] = get_memory_info()
    if 'os' in requested_params:
        results['Operating System Information'] = get_os_info()
    if 'python' in requested_params:
        results['Python Version'] = get_python_version()
    if 'java' in requested_params:
        results['Java Version'] = get_java_version()
    if 'benchmarks' in requested_params:
        results['Benchmark Results'] = get_benchmarks()
    
    return results

if __name__ == "__main__":
    # Example usage: specify which parameters you want to fetch
    requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
    system_info = fetch_info(requested_params)
    
    # Print the requested system information
    for title, data in system_info.items():
        print_table(data, title)
import platform
import psutil
import GPUtil
import timeit
import subprocess
from tabulate import tabulate

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Frequency (MHz)": f"{psutil.cpu_freq().current} MHz" if psutil.cpu_freq() else "N/A"
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load": f"{gpu.load * 100:.2f}%",
            "Free Memory (MB)": f"{gpu.memoryFree / 1024:.2f}",
            "Used Memory (MB)": f"{gpu.memoryUsed / 1024:.2f}",
            "Total Memory (MB)": f"{gpu.memoryTotal / 1024:.2f}",
            "Temperature (C)": gpu.temperature
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (Total) (GB)": f"{virtual_mem.total / (1024 ** 3):.2f}",
        "Virtual Memory (Available) (GB)": f"{virtual_mem.available / (1024 ** 3):.2f}",
        "Swap Memory (Total) (GB)": f"{swap_mem.total / (1024 ** 3):.2f}",
        "Swap Memory (Free) (GB)": f"{swap_mem.free / (1024 ** 3):.2f}",
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_python_version():
    return f"Python {platform.python_version()}"

def get_java_version():
    try:
        result = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
        java_version = result.stderr.split('\n')[0].split('"')[1]
        return f"Java {java_version}"
    except FileNotFoundError:
        return "Java not found"

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark Time (s)": f"{cpu_benchmark():.4f}",
        "GPU Benchmark Time (s)": f"{gpu_benchmark().get('benchmark_time', 'N/A'):.4f}"
    }
    return benchmarks

def cpu_benchmark():
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"gpu_name": "N/A", "benchmark_time": 0}
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return {"gpu_name": "Error", "benchmark_time": str(e)}

def print_table(data, title):
    headers = ["Category", "Details"]
    if isinstance(data, dict):
        table = [(k, v) for k, v in data.items()]
    elif isinstance(data, str):
        table = [("Details", data)]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = data[0].keys()
        table = [list(gpu.values()) for gpu in data]
    else:
        table = []
    
    print(f"\n{title}\n")
    print(tabulate(table, headers, tablefmt="grid"))

def fetch_info(requested_params):
    results = {}
    if 'cpu' in requested_params:
        results['CPU Information'] = get_cpu_info()
    if 'gpu' in requested_params:
        results['GPU Information'] = get_gpu_info()
    if 'memory' in requested_params:
        results['Memory Information'] = get_memory_info()
    if 'os' in requested_params:
        results['Operating System Information'] = get_os_info()
    if 'python' in requested_params:
        results['Python Version'] = get_python_version()
    if 'java' in requested_params:
        results['Java Version'] = get_java_version()
    if 'benchmarks' in requested_params:
        results['Benchmark Results'] = get_benchmarks()
    
    return results

if __name__ == "__main__":
    # Example usage: specify which parameters you want to fetch
    requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
    system_info = fetch_info(requested_params)
    
    # Print the requested system information
    for title, data in system_info.items():
        print_table(data, title)
import platform
import psutil
import GPUtil
import timeit
import subprocess
from tabulate import tabulate

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Logical Cores": psutil.cpu_count(logical=True),
        "Frequency (MHz)": f"{psutil.cpu_freq().current} MHz" if psutil.cpu_freq() else "N/A"
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load": f"{gpu.load * 100:.2f}%",
            "Free Memory (MB)": f"{gpu.memoryFree / 1024:.2f}",
            "Used Memory (MB)": f"{gpu.memoryUsed / 1024:.2f}",
            "Total Memory (MB)": f"{gpu.memoryTotal / 1024:.2f}",
            "Temperature (C)": gpu.temperature
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (Total) (GB)": f"{virtual_mem.total / (1024 ** 3):.2f}",
        "Virtual Memory (Available) (GB)": f"{virtual_mem.available / (1024 ** 3):.2f}",
        "Swap Memory (Total) (GB)": f"{swap_mem.total / (1024 ** 3):.2f}",
        "Swap Memory (Free) (GB)": f"{swap_mem.free / (1024 ** 3):.2f}",
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_python_version():
    return f"Python {platform.python_version()}"

def get_java_version():
    try:
        result = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
        java_version = result.stderr.split('\n')[0].split('"')[1]
        return f"Java {java_version}"
    except FileNotFoundError:
        return "Java not found"

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark Time (s)": f"{cpu_benchmark():.4f}",
        "GPU Benchmark Time (s)": f"{gpu_benchmark().get('benchmark_time', 'N/A'):.4f}"
    }
    return benchmarks

def cpu_benchmark():
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"gpu_name": "N/A", "benchmark_time": 0}
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return {"gpu_name": "Error", "benchmark_time": str(e)}

def print_table(data, title):
    headers = ["Category", "Details"]
    if isinstance(data, dict):
        table = [(k, v) for k, v in data.items()]
    elif isinstance(data, str):
        table = [("Details", data)]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = data[0].keys()
        table = [list(gpu.values()) for gpu in data]
    else:
        table = []
    
    print(f"\n{title}\n")
    print(tabulate(table, headers, tablefmt="grid"))

def fetch_info(requested_params):
    results = {}
    if 'cpu' in requested_params:
        results['CPU Information'] = get_cpu_info()
    if 'gpu' in requested_params:
        results['GPU Information'] = get_gpu_info()
    if 'memory' in requested_params:
        results['Memory Information'] = get_memory_info()
    if 'os' in requested_params:
        results['Operating System Information'] = get_os_info()
    if 'python' in requested_params:
        results['Python Version'] = get_python_version()
    if 'java' in requested_params:
        results['Java Version'] = get_java_version()
    if 'benchmarks' in requested_params:
        results['Benchmark Results'] = get_benchmarks()
    
    return results

if __name__ == "__main__":
    # Example usage: specify which parameters you want to fetch
    requested_params = ['cpu', 'gpu', 'memory', 'os', 'python', 'java', 'benchmarks']
    system_info = fetch_info(requested_params)
    
    # Print the requested system information
    for title, data in system_info.items():
        print_table(data, title)
