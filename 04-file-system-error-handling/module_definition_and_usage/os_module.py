import os

print(f"OS name: {os.name}")
print("OS system():")
os.system('ifconfig lo0')
print(f"OS getcwd(): {os.getcwd()}")
os.chdir('../')
print(f"OS getcwd(): {os.getcwd()}")
