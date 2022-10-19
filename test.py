import subprocess
import random
import os

counter = 0;

result1 = subprocess.run(['make'])
if (result1.returncode != 0):
    print("Compile error! Stopping here!")
    exit(0)
    
while (True):
    num_employee = random.randrange(100)
    num_customer = random.randrange(2000)
    num_wash_bays = random.randrange(1000)
    
    if os.path.exists("output.txt"):
        os.remove("output.txt")

    print("running...[" + str(counter)+ ']')
    with open('output.txt', 'w') as f:
        result2 = subprocess.run(['./carwash', str(num_employee), str(num_customer), str(num_wash_bays)], stdout=f)
        if (result2.returncode != 0):
            print("Error occured! Returncode: " + str(result2.returncode))
            print("Parameter: " + str(num_employee) + ' ' + str(num_customer) + ' ' + str(num_wash_bays))
            print(result2.stderr)
            break;
        else:
            print("worked :-)")
            counter = counter + 1