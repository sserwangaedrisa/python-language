# In this code , we are importing the built library of python called 'sys' (system), this helps us access alot of system info including the command line arguments
from sys import argv

for i in argv:
    print(f"{i}")
print()
# In case you want to print a portion of the list
for arg in argv[1:2]:
    print(f"{arg}")
