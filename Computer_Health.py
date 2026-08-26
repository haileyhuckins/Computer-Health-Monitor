# Computer_Health.py by Hailey Huckins

# Import needed modules
import shutil
import psutil
import platform
from datetime import datetime

# Check disk space and return true if > 20% free
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

# Check CPU usage for 1 sec.
# Healthy machine if CPU usage is < 75%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

# Convert data into readable format for user
def get_size(bytes, suffix="B"):
    factor = 1024

    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("=" * 40, "Computer Health", "=" * 40)

# Check if disk space and CPU usage are healthy
if not check_disk_usage("/") or not check_cpu_usage():
    print("Machine Health: ERROR!")
else:
    print("Machine Health: HEALTHY!")

# Print disk usage
du = shutil.disk_usage("/")

print()
print("Disk Usage:")
print("Total:", get_size(du.total))
print("Used:", get_size(du.used))
print("Free:", get_size(du.free))
print("Disk Usage:", round(du.used / du.total * 100, 2), "%")

# Print CPU %
print()
print("CPU Percentage:")
print(psutil.cpu_percent(1), "%")

#Print security updates
print()
print("Security Updates:")
print("Check system settings for the latest security updates.")

# Print any running proccesses
print()
print("Services Running:")
print("Number of running processes:", len(psutil.pids()))

# Sys info
print()
print("=" * 40, "System Information", "=" * 40)

uname = platform.uname()

print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# Boot time
print()
print("=" * 40, "Boot Time", "=" * 40)

boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)

print(f"Boot Time: {bt.month}-{bt.day}-{bt.year} "
      f"{bt.hour}:{bt.minute}:{bt.second}")

# Print CPU Info
print()
print("=" * 40, "CPU Info", "=" * 40)

# Cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

#CPU Stats
print()
print("CPU Statistics:")
print(psutil.cpu_stats())

# CPU frequency
print()
print("CPU frequency:")
print(psutil.cpu_freq())

# CPU Usage per core
print()
print("CPU Usage Per Core:")

for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")

#Memory info
print()
print("=" * 40, "Memory Information", "=" * 40)
# Details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")

# Swap memory info
print()
print("=" * 20, "SWAP", "=" * 20)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")

#Disk INFO
print()
print("=" * 40, "Disk Information", "=" * 40)
print("Partitions and Usage:")

# Disk partition
partitions = psutil.disk_partitions()

for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"Mountpoint: {partition.mountpoint}")
    print(f"File system type: {partition.fstype}")

    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue

    print(f"Total Size: {get_size(partition_usage.total)}")
    print(f"Used: {get_size(partition_usage.used)}")
    print(f"Free: {get_size(partition_usage.free)}")
    print(f"Percentage: {partition_usage.percent}%")

#Disk I/O stats since bootup
disk_io = psutil.disk_io_counters()

print()
print("Disk I/O Statistics Since Boot:")
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

#Network info
print()
print("=" * 40, "Network Information", "=" * 40)
# All interfaces
if_addrs = psutil.net_if_addrs()

for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ====")
        #IP Address
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"IP Address: {address.address}")
            print(f"Netmask: {address.netmask}")
            print(f"Brodcast IP: {address.broadcast}")
        # Display MAC address
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"MAC Address: {address.address}")
            print(f"Netmask: {address.netmask}")
            print(f"Broadcast MAC: {address.broadcast}")

# Network I/O Stats since bootup
net_io = psutil.net_io_counters()
print()
print("I/O Statistics Since Boot:")
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")