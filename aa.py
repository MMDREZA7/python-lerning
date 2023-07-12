list = []
print('Hi','dar khedmatam')

khast = input('chi mighay?')
list.append(khast)

print(list)

for shopping_list in list :
    khast = input('digeh chi mighay?')
    list.append(khast)
    print(list,' done')

    if khast == '' :
        break

print(shopping_list)  

print('alaan miram milharam')



