numbers_list = []

while True:
    number = input('Enter number (number>0): ')
    
    
    if number == '':
        break
    numbers_list.append(int(number))
    

# print(sum(numbers_list))

sum_of_numbers = 0
for item in numbers_list:
    sum_of_numbers += item

print(sum_of_numbers)

