import os


disk_usage = os.statvfs("/")
disk_total = disk_usage.f_frsize * disk_usage.f_blocks / (1024 * 1024 * 1024)
disk_free = disk_usage.f_frsize * disk_usage.f_bfree / (1024 * 1024 * 1024)

print(f"Total Disk Space: {disk_total:.2f} GB")
print(f"Free Disk Space: {disk_free:.2f} GB")