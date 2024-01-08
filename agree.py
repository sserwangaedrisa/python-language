s = input("Do you agree: ")
s = s.lower
if s in ['y', 'Y']:
    print('Yes you have agreed')
elif s in ['n', 'N']:
    print("No you don't agree")
else:
    print("You haven't decided")