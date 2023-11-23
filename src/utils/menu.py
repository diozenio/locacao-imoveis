import os
from utils.divider import divider

def menu(title, options):
    choice = None
    while choice != 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        divider()
        print(title)
        divider()
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt['name']}")
        print("0. Voltar")
        divider()
        try:
            choice = int(input("Selecione: "))
        except ValueError:
            choice = None

        if choice is not None and 0 < choice <= len(options):
            os.system('cls' if os.name == 'nt' else 'clear')
            if options[choice - 1]['params'] is None:
                options[choice - 1]['function']()
            else:
                options[choice - 1]['function'](options[choice - 1]['params'])
            input("Pressione ENTER para continuar...")