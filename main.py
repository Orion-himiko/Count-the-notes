money=int(input("Amount Withdrawn: "))

notes1000=money//1000
notes100=(money%1000)//100
notes10=((money%1000)%100)//10

print("1000 notes:",notes1000)
print("100 notes:",notes100)
print("10 notes:",notes10)