# In this code , we are importing the built library of python called 'sys' (system), this helps us access alot of system info including the command line arguments
from sys import argv

for i in argv:
    print(f"{i}")
print()
# In case you want to print a portion of the list
# If you want to access the whole of the argv list, you can use the code  " argv[0:]"
for arg in argv[1:2]:
    print(f"{arg}")
