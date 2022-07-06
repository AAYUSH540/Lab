n1 = int(input("Number 1 : "))
n2 = int(input("Number 2 : "))

i=0
ans=0
while i<n2:
    ans+=n1
    i+=1

print(f"\nMultiplicarion of {n1} , {n2} Without * operator is ----> {ans}")