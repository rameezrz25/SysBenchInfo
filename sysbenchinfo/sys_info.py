import platform
import psutil
import GPUtil
import timeit

def get_system_info():
    info = {
        "cpu": get_cpu_info(),
        "gpu": get_gpu_info(),
        "memory": get_memory_info(),
        "os": get_os_info(),
        "benchmarks": get_benchmarks(),
    }
    return info

def get_cpu_info():
    cpu_info = {
        "architecture": platform.machine(),
        "model": platform.processor(),
        "count": psutil.cpu_count(logical=True),
        "frequency": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "id": gpu.id,
            "name": gpu.name,
            "load": gpu.load,
            "free_memory": gpu.memoryFree,
            "used_memory": gpu.memoryUsed,
            "total_memory": gpu.memoryTotal,
            "temperature": gpu.temperature,
        })
    return gpu_info

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    memory_info = {
        "virtual_memory": virtual_mem._asdict(),
        "swap_memory": swap_mem._asdict(),
    }
    return memory_info

def get_os_info():
    os_info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
    return os_info

def get_benchmarks():
    benchmarks = {
        "cpu_benchmark": cpu_benchmark(),
        "gpu_benchmark": gpu_benchmark(),
    }
    return benchmarks

def cpu_benchmark():
    # A simple CPU benchmark: calculating the sum of squares from 1 to 100,000
    stmt = "sum(x*x for x in range(100000))"
    cpu_time = timeit.timeit(stmt, number=100)
    return cpu_time

def gpu_benchmark():
    # A simple GPU benchmark (this is a placeholder as GPU benchmarking typically requires more complex setup)
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return "No GPU found"
        
        gpu = gpus[0]
        load_time = timeit.timeit("GPUtil.getGPUs()", globals=globals(), number=100)
        return {"gpu_name": gpu.name, "benchmark_time": load_time}
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(get_system_info())
