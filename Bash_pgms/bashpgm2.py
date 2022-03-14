import subprocess
res=subprocess.run(['cat','Jenny.txt'],stderr=subprocess.PIPE,text=True)
print(res.stderr)