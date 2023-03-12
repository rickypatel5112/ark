import os
import platform

import psutil


def get_cpu_percent(time_interval = 2):
    return psutil.cpu_percent(time_interval)

def get_cpu_count(): 
    return os.cpu_count()

def get_ram_usage():
    #returns tuple(total, available, percent, used, free)
    return psutil.virtual_memory()

def get_node():
    return platform.uname().node

def get_processor():
    return platform.uname().processor

def get_system():
    return platform.uname().system

def get_machine():
    return platform.uname().machine

# print("CPU Count", get_cpu_count())
# print("CPU percent", get_cpu_percent())
# print("RAM Usage", get_ram_usage())
# print("Node", get_node())
# print("Processor", get_processor())
# print("System", get_system())
# print("Machine", get_machine())
