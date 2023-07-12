numbers_of_student = []
question_2 = int(input('How much student: '))

print(question_2)
print(numbers_of_student)

majmoo = 0

Number_list = int(input('give me her/his number: '))
numbers_of_student.append(Number_list)
majmoo = majmoo + Number_list
print('jam kol =' , majmoo)

print(numbers_of_student)

while Number_list != question_2 :
    
    question_2 = int(input('plaese enter her/his number: '))
    numbers_of_student.append(question_2)
    print(numbers_of_student)
    majmoo = majmoo + Number_list
    print('jam kol =' , majmoo)

    if Number_list == question_2 :

        print('you tell me',question_2,'nmber')
        
        break


    
print()
print(numbers_of_student)
print()
moadel = majmoo / len(numbers_of_student)
print()
print()
print('moadele your students is', moadel)




