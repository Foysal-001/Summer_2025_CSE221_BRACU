for i in range(int(input())):
    n=int(input())
    if n%2 == 0:
        print(n,'is an Even number.')
    
    else:
        print(n,'is an Odd number.')

#more fun one 
for i in range(int(input())):
    n=int(input())
    hehe=['is an Even number.', 'is an Odd number.']
    print(n, hehe[n%2])
    

