import os
import subprocess
import socket
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def kill_process_using_port(port):
    result = subprocess.run(['lsof', '-t', f'-i:{port}'], capture_output=True, text=True)
    if result.stdout:
        pid = result.stdout.strip()
        subprocess.run(['kill', '-9', pid])

ports = [5173, 5174]
for port in ports:
    if is_port_in_use(port):
        kill_process_using_port(port)


os.chdir('/home/chait/Desktop/proj/backend/')
subprocess.Popen(['sudo', '/home/chait/myeve/bin/python3.11', '-m', 'uvicorn', 'app:app', '--reload'])
os.chdir('/home/chait/Desktop/proj/dental/')
subprocess.Popen(['npm', 'run', 'dev'])
os.system("xhost +")
os.environ["DISPLAY"] = ":0"
subprocess.run(["chromium-browser", "--no-sandbox", "http://localhost:5173/"])
print(os.getcwd())