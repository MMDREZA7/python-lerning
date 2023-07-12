numbers_list = []

while True:
    number = int(input('Enter number (>0): '))

    if number < 0:
        break
    
    numbers_list.append(number)

# print(sum(numbers_list))

sum_of_numbers = 0
for item in numbers_list:
    sum_of_numbers += item

print(sum_of_numbers)