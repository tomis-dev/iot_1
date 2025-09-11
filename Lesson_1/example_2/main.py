import time
time.sleep(0.1) # Wait for USB to become ready

print("Input test starting")
pname = input("Tell me your name: ")
if pname == "Clark Kent":
    print("Hello Superman!")
else:
    print("Hello ", pname)
