import os, time

class values:
    localUsername = ''
    fileLocation = ''
    fileName = ''
    fileDestination = ''
    reEnter = ''
    roundTwo = ''
    

def init():
    values.localUsername = input('Please enter your local username: ')
    main()

def main():
    x = ''
    values.fileLocation = input('Please enter the location of the file: ')
    values.fileName = input('Please enter the name of the file: ')
    if '.' not in values.fileName:
        print('Did you forget a file extension?')
        x = input('Y/N: ')
        if x.upper() == 'Y':
            print('Retype it now please')
            values.fileName = input('Please enter the name of the file: ')
        
    values.fileDestination = input('Please type the destination to move the file: ')
    mover()

def mover():
    try:
        os.rename("/Users/" + values.localUsername.capitalize() + "/" + values.fileLocation.capitalize() + "/" + values.fileName , "/Users/" + values.localUsername.capitalize() + "/" + values.fileDestination.capitalize() + "/" + values.fileName)
        end()
    except:
        print('An error occured, please check spelling, make sure you put a file extension.')
        print('These were your Inputs:')
        print(values.localUsername)
        print(values.fileLocation)
        print(values.fileName)
        print(values.fileDestination)
        print('Would you like to re-enter your local username?')
        print('You will still re-enter directory names if you answer no.')
        values.reEnter = input('Y/N: ')
        if values.reEnter.upper() == 'Y':
            init()
        else:
            main()
        main()

def end():
    print('Wanna go for round 2?')
    values.roundTwo = input('Y/N: ')
    if values.roundTwo.upper() == 'Y':
        main()
    else:
        print('See ya!')
        time.sleep(2)


init()
