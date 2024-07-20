import platform
import psutil
import GPUtil
import timeit
from tabulate import tabulate

def get_system_info():
    info = {
        "CPU": get_cpu_info(),
        "GPU": get_gpu_info(),
        "Memory": get_memory_info(),
        "OS": get_os_info(),
        "Benchmarks": get_benchmarks(),
    }
    return info

def get_cpu_info():
    cpu_info = {
        "Architecture": platform.machine(),
        "Model": platform.processor(),
        "Count": psutil.cpu_count(logical=True),
        "Frequency (GHz)": psutil.cpu_freq().current / 1000 if psutil.cpu_freq() else None,
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "ID": gpu.id,
            "Name": gpu.name,
            "Load (%)": gpu.load * 100,
            "Free Memory (MB)": gpu.memoryFree / 1024,
            "Used Memory (MB)": gpu.memoryUsed / 1024,
            "Total Memory (MB)": gpu.memoryTotal / 1024,
            "Temperature (°C)": gpu.temperature,
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "Virtual Memory (GB)": virtual_mem.total / (1024**3),
        "Used Virtual Memory (GB)": virtual_mem.used / (1024**3),
        "Available Virtual Memory (GB)": virtual_mem.available / (1024**3),
        "Total Swap Memory (GB)": swap_mem.total / (1024**3),
        "Used Swap Memory (GB)": swap_mem.used / (1024**3),
        "Free Swap Memory (GB)": swap_mem.free / (1024**3),
    }
    return memory_info

def get_os_info():
    os_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return os_info

def get_benchmarks():
    benchmarks = {
        "CPU Benchmark (s)": cpu_benchmark(),
        "GPU Benchmark (s)": gpu_benchmark(),
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
            return "No GPU found"
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return load_time
    except Exception as e:
        return str(e)

def print_system_info():
    info = get_system_info()
    
    print("CPU Information")
    print(tabulate([info["CPU"]], headers="keys", tablefmt="grid"))
    print("\nGPU Information")
    if info["GPU"]:
        print(tabulate(info["GPU"], headers="keys", tablefmt="grid"))
    else:
        print("No GPU found")
    print("\nMemory Information")
    print(tabulate([info["Memory"]], headers="keys", tablefmt="grid"))
    print("\nOS Information")
    print(tabulate([info["OS"]], headers="keys", tablefmt="grid"))
    print("\nBenchmarks")
    print(tabulate([info["Benchmarks"]], headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    print_system_info()
