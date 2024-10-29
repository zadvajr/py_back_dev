#walrus operator - := allows assignment within expression

#without walrus operator :=
num = 5

if(num % 2) == 0:
    print("Your number is even")
else:
    print("Your number is odd")


#with walrus operator
if(mod := (num % 2) == 0):
    print("Your number is even")
else:
    print("Your number is odd")

#end
