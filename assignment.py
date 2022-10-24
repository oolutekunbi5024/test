#evenNumber for While Loop
evennumber =2
while evennumber<=30:
    print(evennumber)
    evennumber+=2

print("Even Numbers for forLoop")
#evenNumber for forloop
for number in range(1,30,2):
    number+=1
    print(number)

print("Odd Numbers for whileLoop")
#oddNumber for While Loop
evennumber =1
while evennumber<=30:
    print(evennumber)
    evennumber+=2
print("Odd Numbers for forLoop")
#oddNumber for forloop
number=1
for number in range(1,30,2):
    print(number)
    number+=2
    

#Financial Statement of Ahmed

capstoneProject=50000
marketing=0.25 * capstoneProject
operationalExpenses=0.50 * capstoneProject
customerAquisition=0.25*capstoneProject
aquiredCustomers=int(customerAquisition/5)

print("Below is the Financial Statement for Ahmed")


print(f"Capstone Project            ------------------------ {capstoneProject}")
print(f"Marketing Expenses          ------------------------ {marketing}")
print(f"Operational Expenses        ------------------------ {operationalExpenses}")
print(f"Customer Aquisition Exp     ------------------------ {customerAquisition}")

print(f"Customers that can be aquired --------------------- {aquiredCustomers}")