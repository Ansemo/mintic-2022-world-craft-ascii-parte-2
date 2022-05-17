import random
from colorama import Fore, init


def cordenadas_aleatorias():
    filas = [[random.choice([i for i in range(0, 10)]) for i in range(0, 4)] for i in range(0, 4)]
    return filas



def crear_mundo():
    init()
    filas = cordenadas_aleatorias()[0]
    #se ouede resumir en un for
    print(Fore.WHITE +'Filas            ',Fore.GREEN +f'{filas[0]} ', Fore.RED +f'{filas[1]} ' , Fore.BLUE +f'{filas[2]} ', Fore.YELLOW +f'{filas[3]} ')
    columnas = cordenadas_aleatorias()[1]
    print(Fore.WHITE +'Columnas         ',Fore.GREEN +f'{columnas[0]} ', Fore.RED +f'{columnas[1]} ' , Fore.BLUE +f'{columnas[2]} ', Fore.YELLOW +f'{columnas[3]} ')
    anchos = cordenadas_aleatorias()[2]
    print(Fore.WHITE +'Ancho            ',Fore.GREEN +f'{anchos[0]} ', Fore.RED +f'{anchos[1]} ' , Fore.BLUE +f'{anchos[2]} ', Fore.YELLOW +f'{anchos[3]} ')
    largos = cordenadas_aleatorias()[3]
    print(Fore.WHITE +'Largo            ',Fore.GREEN +f'{largos[0]} ', Fore.RED +f'{largos[1]} ' , Fore.BLUE +f'{largos[2]} ', Fore.YELLOW +f'{largos[3]} ')
    #listas
    #
    # filas = [0, 3, 5, 6]
    # columnas = [1, 3, 11, 12]
    # anchos = [2, 9, 1, 4]
    # largos = [5, 2, 2, 1]

    #matriz
    for i in range(0, 18):
        for j in range(0, 18):
            if filas[0] <= i <= filas[0] + (largos[0] - 1) and columnas[0] <= j <= columnas[0] + (anchos[0] - 1):
                print(Fore.GREEN + '#', end='  ')
                # print(Fore.GREEN+ f'({i},{j})', end='  ')
            elif filas[1] <= i <= filas[1] + (largos[1] - 1) and columnas[1] <= j <= columnas[1] + (anchos[1] - 1):
                # print(Fore.RED+ f'({i},{j})', end='  ')
                print(Fore.RED + '#', end='  ')
            elif filas[2] <= i <= filas[2] + (largos[2] - 1) and columnas[2] <= j <= columnas[2] + (anchos[2] - 1):
                # print(Fore.BLUE + f'({i},{j})', end='  ')
                print(Fore.BLUE + '#', end='  ')
            elif filas[3] <= i <= filas[3] + (largos[3] - 1) and columnas[3] <= j <= columnas[3] + (anchos[3] - 1):
                # print(Fore.YELLOW +f'({i},{j})', end='  ')
                print(Fore.YELLOW + '#', end='  ')
            else:
                # print(' ', end='  ')
                print(Fore.WHITE+'-', end='  ')
                # print(Fore.WHITE+f'{i},{j}',end='  ')
        print('')



if __name__ == '__main__':
    # print(cordenadas_aleatorias())
    i = 0
    numero_mundos = int(input('Insertar numero de mundos a crear: '))
    while i < numero_mundos:
        print(Fore.WHITE + f'\nMundo {i + 1}')
        crear_mundo()
        i += 1

