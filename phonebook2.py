import csv
file = open('phonebook.csv', 'a')
Name = input('Name: ')
Number = input('Number: ')

writer = csv.writer(file)
writer.writerow([Name, Number])
file.close()
# alternatively, we can use the below code in order to eliminate the error that can rise from forgettin to close the open file. This code will automatically close the file after using it.
# with open('phonebook.csv', "a") as file:
#     Name = input('Name: ')
#     Number = input('Number: ')

#     writer = csv.writer(file)
#     writer.writerow([Name, Number])
