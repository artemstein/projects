from colorama import Fore, Back, Style, init

# Fore - цвет текста, Back - фон строки, Style - сама строка (грубо говоря)

print(Fore.RED + 'Красный текст')
print(Back.BLACK + 'Черный фон')

print(Style.RESET_ALL + 'Нормальный текст\n') # Возвращает текст в нормальное состояние

# Основные команды:
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

# Есть также дополнительные:
# Fore: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
# Back: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX


init(autoreset=True)
print(Fore.GREEN + 'Зеленый текст')
print('Нормальный') # Автоматически меняется на нормальный благодаря init(autoreset)

