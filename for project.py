number_list = []

while True :
    number= int(input('inter a number: '))
    if number != -1 :
        break
    
    number_list.append(number)


of_number = 0
for item in number_list:
    of_number = number_list + item

print(of_number)







