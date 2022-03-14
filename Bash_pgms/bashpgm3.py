import subprocess
res=subprocess.run(['echo','welcome to india'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
print(res.stdout)