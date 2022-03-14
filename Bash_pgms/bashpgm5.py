import subprocess
from sys import stdout
process=subprocess.Popen(['echo','welcome to India'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
res=process.communicate()
print(res)