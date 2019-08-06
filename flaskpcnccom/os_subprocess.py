import os
myCmd = os.popen('ls -la').read()
print(myCmd)

