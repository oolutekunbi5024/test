from unicodedata import name


Name="Olamide"
Age=60
Stipend=2000
gender="F"

print(f"Hello my name is {Name} and I am {Age} years old")

print("Hello " + Name + " your age is " + str(Age))

if Name==Age:
    print("The names are the same")

if (Name=="Siri" or gender=="F"):
    print("True")