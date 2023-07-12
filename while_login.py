name = input('please enter your name: ')
password = int(input('please enter your passcode: '))



while (name != 'mmd' or password != 123) and (name != 'habib' or password != 321) and (name != 'mojtaba' or password != 111) :
    print('your name or passcode is false: ')
    name = input('please enter your name: ')
    password = int(input('please enter your passcode: '))

print()
print(f'wellcom back: {name}')
print()
print('informations')
print()

print(f'Name: {name}')
print(f'passcode: {password}')
if name == 'mmd':
    print('sen: ' '18')
    print()
    print()
    print('ghad: ' '188')

elif name == 'habib' :
    print('sen: ' '25')
    print()
    print()
    print('ghad: ' '175')

else:
    print('sen: ' '19')
    print()
    print()

    print('ghad: ' '183')


input()