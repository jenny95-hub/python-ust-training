import subprocess
process=subprocess.Popen(['ls','-la'])
print('complete') 


process=subprocess.Popen(['ls','-la'])
process.wait()
print('complete') 