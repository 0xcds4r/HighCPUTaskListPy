import psutil

def search_processes():
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        yield proc.info

def find_max_cpu_process():
    max_cpu_percent = 0
    max_cpu_process = None
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        cpu_percent = proc.info['cpu_percent']
        if cpu_percent > max_cpu_percent and proc.info['name'] != 'Idle':
            max_cpu_percent = cpu_percent
            max_cpu_process = proc.info
    return max_cpu_process

def main():
    processes = list(search_processes())
    max_cpu_process = find_max_cpu_process()

    print("All processes:")
    for proc in processes:
        print(proc)

    print("\nProcess with highest CPU usage:")
    print(max_cpu_process)

if __name__ == '__main__':
    main()
