t=int(input("Enter thje number of cases="))
for i in range(t):
    n=int(input("ENTER NO OF GUEST="))
    a=int(input("ENTER NO OF FRUITS="))
    b=int(input("ENTER NO OF VEGETABLES="))
    c=int(input("ENTER NO OF FISHES="))
    p=b-1
    s=a+p
    
    f=c+p
    d=s+f
    if(n==d):
        print("YES")

    else:
        print("NO")
    

