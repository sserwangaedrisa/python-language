# initializing a dictionary
person ={}
# or 
# person = dict()

person = {
   'Eddie': 756429788,
    'Emma': 756483838
}
Name = input('Name: ')
if Name in person:
    print(f"Number: {person[Name]}")

