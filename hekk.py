def subtract():
    x = input("enter numbers you want to subtract:").split('-')
    sum =0
    for i in x:
        sum = int(i)-sum
    print(-sum)
    return sum
subtract()

def divide():
    x = input("enter numbers you want to divide:").split('/')
    sum = 1
    for i in x:
        sum = int(i)/sum
    print(1/sum)
    return sum
divide()

