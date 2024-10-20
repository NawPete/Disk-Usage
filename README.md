# Disk Usage Monitoring Script

This Python script is designed to monitor the total and free disk space on a Linux system. It retrieves disk usage information using the `os.statvfs()` method, calculates the total and free space, and outputs the results in gigabytes (GB).

## Features

- **Total Disk Space**: The script calculates and displays the total disk space in GB.
- **Free Disk Space**: The script calculates and displays the available free disk space in GB.

## Use Case

This script is useful for system administrators, DevOps engineers, or anyone who needs to monitor disk usage on a server or local machine. It can be integrated into monitoring systems, or used as a standalone script to quickly check disk capacity. It's especially handy in environments where keeping track of available disk space is crucial to prevent system issues caused by running out of storage.

## Prerequisites

- Python 3.x must be installed on your machine.
- The script is primarily designed for Linux-based systems, as it uses the `os.statvfs()` function, which is supported on Unix-like operating systems.

## How to Run the Script

1. **Clone the Repository**

  First, clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/NawPete/Disk-Usage.git
   ```
   
2. **Navigate to the Directory**

  Move into the directory containing the script:

   ```bash
   cd "Disk usage"
   ```

3. **Run the Script**

  To run the disk usage monitoring script, execute the following command:

  ```bash

  python3 disk_usage_monitor.py
  ```
  Output

  After running the script, you will see the following output showing the total and free disk space:

  ```mathematica

  Total Disk Space: XX.XX GB
  Free Disk Space: YY.YY GB
  ```


## Example Usage

This script can be incorporated into a larger system to monitor disk usage over time or triggered periodically with a cron job. For example:

- **Monitoring Servers**: Integrate it into a monitoring dashboard for tracking server disk usage.
- **Alerts**: Set up alerts when free disk space drops below a certain threshold.
- **Automation**: Automate disk space checks as part of your DevOps pipelines to ensure that servers have enough storage to continue running efficiently.
