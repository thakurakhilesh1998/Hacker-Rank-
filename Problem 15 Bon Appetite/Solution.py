def bonAppetit(bill, k, b):
    count=0
    for i in range(len(bill)):
        if(i!=k):
            count+=bill[i]
    pay = count//2
    if(pay != b):
        print(b-pay)
    else:
        print("Bon Appetite")def bonAppetit(bill, k, b):
    count=0
    for i in range(len(bill)):
        if(i!=k):
            count+=bill[i]
    pay = count//2
    if(pay != b):
        print(b-pay)
    else:
        print("Bon Appetite")