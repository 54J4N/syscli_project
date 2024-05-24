# SysCLI Project

![SysCLI Screenshot](images/screenshot.png)

SysCLI is a command-line tool for displaying system information and managing system processes. It provides various functionalities such as checking system information, managing processes, running security checks, performing web searches, and more.

Features
Display System Information
Shows basic details about the system such as the operating system, node name, release, version, machine, and processor.

Command:

sh
Copy code
system
Display CPU Information
Provides details about the CPU, including the number of physical and logical cores, frequency, and usage per core.

Command:

sh
Copy code
cpu
Example Output:

yaml
Copy code
Physical cores: 4
Total cores: 8
Max Frequency: 3400.0Mhz
Min Frequency: 800.0Mhz
Current Frequency: 2800.0Mhz
CPU Usage Per Core:
Core 0: 23%
Core 1: 15%
Core 2: 10%
Core 3: 30%
Total CPU Usage: 20%
Display Memory Information
Shows information about the system's memory, including total, available, and used memory, along with the memory usage percentage.

Command:

sh
Copy code
memory
Example Output:

makefile
Copy code
Total: 16.0 GB
Available: 8.5 GB
Used: 7.0 GB
Percentage: 55%
Display Disk Information
Lists disk partitions and their usage statistics, including total size, used space, free space, and usage percentage.

Command:

sh
Copy code
disk
Example Output:

yaml
Copy code
=== Device: C: ===
Mountpoint: /
File system type: NTFS
Total Size: 500.0 GB
Used: 200.0 GB
Free: 300.0 GB
Percentage: 40%
Display Network Information
Displays information about network interfaces, including IP addresses and MAC addresses.

Command:

sh
Copy code
network
Example Output:

yaml
Copy code
=== Interface: Ethernet ===
IP Address: 192.168.1.100
Netmask: 255.255.255.0
Broadcast IP: 192.168.1.255
MAC Address: 00:1A:2B:3C:4D:5E
List All Running Processes
Lists all running processes along with their PID, name, and status.

Command:

sh
Copy code
list_processes
Example Output:

arduino
Copy code
PID       Process name                           Status
1234      python.exe                             running
5678      explorer.exe                           running
91011     notepad.exe                            running
Kill a Process by its PID
Allows you to terminate a process by specifying its PID.

Command:

sh
Copy code
kill_process <PID>
Example Usage:

sh
Copy code
kill_process 1234
Check Files and Processes for Common Security Risks
Scans the system for suspicious files and processes that may indicate security issues, such as malware or unauthorized scripts.

Command:

sh
Copy code
check_security
Example Output:

yaml
Copy code
No suspicious files detected.
No suspicious processes detected.
List Files and Directories
Lists files and directories in the current directory or a specified path.

Command:

sh
Copy code
list_files <path>
Example Usage:

sh
Copy code
list_files /home/user/documents
Change the Current Working Directory
Changes the current working directory to a specified path.

Command:

sh
Copy code
cd <path>
Example Usage:

sh
Copy code
cd /home/user/documents
Create and Delete Files
Provides commands to create and delete files easily from the CLI.

Commands:

sh
Copy code
create_file <filename>
delete_file <filename>
Example Usage:

sh
Copy code
create_file new_document.txt
delete_file old_document.txt
Perform Web Searches
Uses Google Custom Search to perform web searches directly from the CLI.

Command:

sh
Copy code
search <query>
Example Usage:

sh
Copy code
search Python tutorials
Logging
Command executions are logged in the miniCLI.log file for auditing and troubleshooting purposes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Created by 54J4N.

perl
Copy code

This `README.md` file includes detailed descriptions and example outputs for each feature, m






## Installation

To install the package, use:

```sh
pip install .
Usage
After installation, you can run the CLI tool using:

sh
Copy code
mycli
If running directly from the source code, use:

sh
Copy code
python main.py
Features
Display System Information
Shows basic details about the system such as OS, node name, release, version, machine, and processor.

Command:

sh
Copy code
system
Display CPU Information
Provides details about the CPU, including physical cores, total cores, frequency, and usage per core.

Command:

sh
Copy code
cpu
Display Memory Information
Shows information about total, available, used memory, and memory percentage.

Command:

sh
Copy code
memory
Display Disk Information
Lists disk partitions and usage statistics.

Command:

sh
Copy code
disk
Display Network Information
Displays network interfaces and their associated IP addresses and MAC addresses.

Command:

sh
Copy code
network
List All Running Processes
Lists all running processes with their PID, name, and status.

Command:

sh
Copy code
list_processes
Kill a Process by its PID
Allows termination of a process by specifying its PID.

Command:

sh
Copy code
kill_process <PID>
Check Files and Processes for Common Security Risks
Scans for suspicious files and processes that may indicate security issues.

Command:

sh
Copy code
check_security
List Files and Directories
Lists files and directories in the current directory or specified path.

Command:

sh
Copy code
list_files <path>
Change the Current Working Directory
Changes the current working directory to a specified path.

Command:

sh
Copy code
cd <path>
Create and Delete Files
Provides commands to create and delete files.

Commands:

sh
Copy code
create_file <filename>
delete_file <filename>
Perform Web Searches
Uses Google Custom Search to perform web searches from the CLI.

Command:

sh
Copy code
search <query>
Logging
Command executions are logged in the miniCLI.log file for auditing and troubleshooting purposes.