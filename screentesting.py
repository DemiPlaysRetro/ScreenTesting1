if __name__ != '__main__':
    print('Screentesting was not meant to be run as an import!')
    exit()
a = 'X'
b = 'X'
c = 'X'
d = 'X'
e = 'X'
f = 'X'
g = 'X'
h = 'X'
i = 'X'
ROW1 = (f'{a}{b}{c}')
ROW2 = (f'{d}{e}{f}')
ROW3 = (f'{g}{h}{i}')
def printscreen():
    ROW1 = (f'{a}{b}{c}')
    ROW2 = (f'{d}{e}{f}')
    ROW3 = (f'{g}{h}{i}')
    print(ROW1)
    print(ROW2)
    print(ROW3)
printscreen()
while 1 < 2:
    try:
        while 1 < 2:
            print('')
            print('Choose which pixel to edit. (1-9)')
            print('')
            pixel = int(input('>_'))
            if pixel == 1:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    a = (newvalue)
            if pixel == 2:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    b = (newvalue)
            if pixel == 3:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    c = (newvalue)
            if pixel == 4:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    d = (newvalue)
            if pixel == 5:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    e = (newvalue)
            if pixel == 6:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    f = (newvalue)
            if pixel == 7:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    g = (newvalue)
            if pixel == 8:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    h = (newvalue)
            if pixel == 9:
                print('')
                print('Choose new value.')
                print('')
                newvalue = input('>_')
                if (len(newvalue)) != 1:
                    print('')
                    print('only one value may be issued.')
                if (len(newvalue)) == 1:
                    i = (newvalue)
            print('')
            printscreen()
    except ValueError:
            print('')
            print('ERR: Value Error')
            continue
print('A fatal error has occured!')
exit()
