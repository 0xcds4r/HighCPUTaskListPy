# HighCPUTaskListPy

This python program will allow you to view processes hidden from the system task manager, 
the program also finds those processes that affect performance and load your PC.

To kill the process that you think is the source of all the trouble, use the following command in cmd:
```
**taskkill /f /im NAME**
```

For example:
Process with highest CPU usage:
{'name': 'fc.exe', 'memory_percent': 0.014904168830207253, 'cpu_percent': 520.8, 'pid': 4832}

fc.exe is NAME
