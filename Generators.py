def firstn(n) :
    num = 0 
    while num <= n :
        yield num
        num += 1


for i in  firstn(20) :
    print(i)



