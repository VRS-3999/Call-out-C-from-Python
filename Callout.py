import os
import subprocess

def executeCpp():
    data, temp = os.pipe()
    os.write(temp, bytes("5 10\n", "utf-8"))
    os.close(temp)
    s = subprocess.check_output("./Hello", stdin = data)  
    print(s.decode("utf-8"))

if __name__ == "__main__":
    executeCpp()
