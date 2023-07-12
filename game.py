import random
javab = random.randint (1,99)


hads = int(input('geuss my number...'))

while hads != javab :

    if hads > javab :
        input('baraa man koochaiktareh..')  
        hads = int(input('geuss my number...'))
    elif hads < javab :
        input('baraa man bozorgtareh..')
        hads = int(input('geuss my number...'))
    else :
        print('exactly... dorost bood...')
        
        
print('...finish...')








