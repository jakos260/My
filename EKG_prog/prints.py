from colorama import Fore, Back, Style

def message(tekst):
    print(Fore.BLUE + '__________' + '_'*len(tekst))
    print('    ' + tekst + '\n' + Style.RESET_ALL)
    # print('__________' + '_'*len(tekst) + '\n' )

def question(tekst):
    print(Back.WHITE + Fore.BLACK + tekst + Style.RESET_ALL)

def error(tekst):
    print(Fore.RED + tekst + Style.RESET_ALL)

def p(num):
    print('_____________________________')
    print(Fore.YELLOW + f'{num} % ' + Style.RESET_ALL + 'colected...')