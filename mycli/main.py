# main.py
import platform
import psutil
import os
import readline
import logging
from cmd import Cmd
from time import sleep
from tqdm import tqdm
import requests  # Needed for web search functionality

# Set up logging
logging.basicConfig(filename='miniCLI.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class MiniCLI(Cmd):
    intro = 'Welcome to the MiniCLI OS. Type help or ? to list commands.\n'
    prompt = '(miniCLI) '

    # ANSI color codes
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

    # API keys and search engine ID for Google Custom Search
    api_key = 'AIzaSyBYHe1fRbE6x-SfJf_vjrKF6aAVs9Gtjuk'
    cse_id = 'd603aac6adef24e99'

    def preloop(self):
        self.show_welcome_animation()
        self.init_completion()

    def init_completion(self):
        commands = [attr[3:] for attr in dir(self) if attr.startswith('do_')]
        completer = SimpleCompleter(commands)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')

    def show_welcome_animation(self):
        print("Initializing MiniCLI OS...")
        for _ in tqdm(range(50), desc="Loading", ascii=" █"):
            sleep(0.05)
        print("\nWelcome to the MiniCLI OS!\n")

    def postcmd(self, stop, line):
        logging.info(f"Executed command: {line}")
        return stop

    def execute_task(self, task_name, function):
        print(f"{task_name}...")
        sleep(1)  # Simulate processing time
        function()
        print(f"{self.GREEN}Completed {task_name}{self.RESET}\n")

    def do_search(self, query):
        "Search the web using Google Custom Search"
        if not query:
            print("Please provide a search query.")
            return
        print(f"Searching for: {query}...")
        results = self.google_search(query)
        self.display_results(results)

    def google_search(self, query):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {'key': self.api_key, 'cx': self.cse_id, 'q': query}
        response = requests.get(url, params=params)
        results = response.json()
        return results.get('items', [])

    def display_results(self, results):
        if not results:
            print("No results found.")
            return
        for idx, result in enumerate(results, 1):
            print(f"\nResult {idx}: {result['title']}")
            print(result['snippet'])
            print(result['link'])

    def do_system(self, arg):
        "Display basic system information"
        self.execute_task("System Information", self.print_system_info)

    def print_system_info(self):
        print(f"System: {platform.system()}")
        print(f"Node Name: {platform.node()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}")

    def do_memory(self, arg):
        "Display memory information"
        self.execute_task("Memory Information", self.print_memory_info)

    def print_memory_info(self):
        svmem = psutil.virtual_memory()
        print(f"Total: {svmem.total / (1024 ** 3):.2f} GB")
        print(f"Available: {svmem.available / (1024 ** 3):.2f} GB")
        print(f"Used: {svmem.used / (1024 ** 3):.2f} GB")
        print(f"Percentage: {svmem.percent}%")

    def do_cpu(self, arg):
        "Display CPU information"
        self.execute_task("CPU Information", self.print_cpu_info)

    def print_cpu_info(self):
        print(f"Physical cores: {psutil.cpu_count(logical=False)}")
        print(f"Total cores: {psutil.cpu_count(logical=True)}")
        cpu_freq = psutil.cpu_freq()
        print(f"Max Frequency: {cpu_freq.max:.2f}Mhz")
        print(f"Min Frequency: {cpu_freq.min:.2f}Mhz")
        print(f"Current Frequency: {cpu_freq.current:.2f}Mhz")
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    def do_disk(self, arg):
        "Display disk information"
        self.execute_task("Disk Information", self.print_disk_info)

    def print_disk_info(self):
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                print(f"  Total Size: {partition_usage.total / (1024 ** 3):.2f} GB")
                print(f"  Used: {partition_usage.used / (1024 ** 3):.2f} GB")
                print(f"  Free: {partition_usage.free / (1024 ** 3):.2f} GB")
                print(f"  Percentage: {partition_usage.percent}%")
            except PermissionError:
                print("Permission denied to access the mount point")

    def do_network(self, arg):
        "Display network information"
        self.execute_task("Network Information", self.print_network_info)

    def print_network_info(self):
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"=== Interface: {interface_name} ===")
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")

    def do_list_processes(self, arg):
        "List all running processes"
        self.execute_task("Listing Processes", self.print_processes)

    def print_processes(self):
        print("{:<10} {:<40} {:<10}".format('PID', 'Process name', 'Status'))
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                print("{:<10} {:<40} {:<10}".format(proc.info['pid'], proc.info['name'], proc.info['status']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def do_kill_process(self, arg):
        "Kill a process by its PID"
        if not arg.isdigit():
            print("Please provide a valid PID.")
            return
        pid = int(arg)
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()  # Wait for the process to terminate
            print(f"Process {pid} has been terminated.")
        except psutil.NoSuchProcess:
            print("No such process found with PID:", pid)
        except psutil.AccessDenied:
            print("Permission denied to terminate the process with PID:", pid)
        except Exception as e:
            print(f"Error terminating process {pid}: {e}")

    def do_check_security(self, arg):
        "Check files and processes for common security risks"
        self.check_files()
        self.check_processes()

    def check_files(self):
        "Check all files in the current directory for suspicious extensions"
        suspicious_extensions = ['.exe', '.bat', '.cmd', '.vbs', '.js']
        files = os.listdir('.')
        found_suspicious = False
        for file in files:
            if any(file.endswith(ext) for ext in suspicious_extensions):
                print(f"{self.RED}Suspicious file detected: {file}{self.RESET}")
                found_suspicious = True
        if not found_suspicious:
            print(f"{self.GREEN}No suspicious files detected.{self.RESET}")

    def check_processes(self):
        "Check all running processes for names commonly associated with malware"
        suspicious_process_names = ['backdoor', 'keylogger', 'trojan', 'malware']
        found_suspicious = False
        for proc in psutil.process_iter(['name', 'pid']):
            try:
                if any(sus_name in proc.info['name'].lower() for sus_name in suspicious_process_names):
                    print(f"{self.RED}Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']}){self.RESET}")
                    found_suspicious = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        if not found_suspicious:
            print(f"{self.GREEN}No suspicious processes detected.{self.RESET}")

    def do_list_files(self, arg):
        "List files and directories in the current directory or specified path"
        path = arg.strip() if arg else '.'
        try:
            files = os.listdir(path)
            if not files:
                print("The directory is empty.")
            for file in files:
                full_path = os.path.join(path, file)
                if os.path.isdir(full_path):
                    print(f"{file}/")
                else:
                    print(file)
        except FileNotFoundError:
            print("The specified directory does not exist")
        except PermissionError:
            print("Permission denied")

    def do_cd(self, arg):
        "Change the current working directory"
        try:
            os.chdir(arg)
            print(f"Changed current directory to {os.getcwd()}")
        except Exception as e:
            print(e)

    def do_create_file(self, arg):
        "Create a new file"
        if not arg:
            print("Please specify the file name")
            return
        try:
            with open(arg, 'x') as f:
                print(f"File created: {arg}")
        except FileExistsError:
            print("File already exists")

    def do_delete_file(self, arg):
        "Delete a specified file"
        if not arg:
            print("Please specify the file name")
            return
        try:
            os.remove(arg)
            print(f"File deleted: {arg}")
        except FileNotFoundError:
            print("File does not exist")

def main():
    cli = MiniCLI()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print("\nInterrupt received, exiting...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

class SimpleCompleter(object):
    """Simple tab completer for commands."""
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None

if __name__ == '__main__':
    main()
