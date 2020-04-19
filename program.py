print('Welcome to this wonderful game')
print("Enter 'E' for EASY, 'M' for MEDIUM and 'H' for HARD")
level = input('Enter your level: ').lower()



while(level!='e' and level!='m' and level!='h'):
    level = input('Enter the required level please: ').lower()
    if(level=='e' or level=='m' or level=='h'):
        break
    

if(level=='e'):
    print('you have just 6 GUESSES')
    magicnumber = 5
    for i in range(1,7):
        number = input('Guess a number between 1-10: ')
        
        if(int(number) == magicnumber):
            
            print('YOU GOT IT RIGHT!')
            break
        else:
            print('THAT WAS WRONG!')
            print('you have '+ str(6-i)+' left')
            if(i==6):
                print('GAME OVER!!!')

if(level=='m'):
    print('you have just 4 GUESSES')
    magicnumber = 14
    for i in range(1,5):
        number = input('Guess a number between 1-20: ')
        

        if(int(number) == magicnumber):
            
            print('YOU GOT IT RIGHT!')
            break
        else:
            print('THAT WAS WRONG!')
            print('you have '+ str(4-i)+' left')
            if(i==4):
                print('GAME OVER!!!')


if(level=='h'):
    magicnumber = 29
    print('you have just 3 GUESSES')
    for i in range(1,4):
        number = input('Guess a number between 1-50: ')
        

        if(int(number) == magicnumber):
            
            print('YOU GOT IT RIGHT!')
            break
        else:
            print('THAT WAS WRONG!')
            print('you have '+ str(3-i)+' left')
            if(i==3):
                print('GAME OVER!!!')

