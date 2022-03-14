from concurrent.futures import process
import subprocess
process=subprocess.Popen(['ping','-c 5','google.com'],stdout=subprocess.PIPE,text=True)
while True:
    output=process.stdout.readline()
    if output:
        print(output.strip())
    result=process.poll()
    if result is not None:
        break
