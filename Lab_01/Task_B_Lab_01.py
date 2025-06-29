for i in range(int(input())):
    s=input()
    res=s[10:]
    a=res.split()
    num1=float(a[0])
    sign=a[1]
    num2=float(a[2])

    if sign == '+': 
        print(num1+num2)
    
    elif sign == '-':
        print(num1-num2)

    elif sign == '*':
        print(num1*num2)

    else:
        print(num1/num2)

