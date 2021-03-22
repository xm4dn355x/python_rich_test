# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# First demo script for testing rich library                           #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from rich import print


if __name__ == '__main__':
    print('[black on white]Hello World![/black on white]')
    print("[bold yellow on red blink]Блинк в винде не работает")
    print("[bold yellow on red]Зато ярко понятно читается")
    warn_b = "[bold yellow on red]"
    warn_e = "[/bold yellow on red]"
    print(f'{warn_b}Тестируем F-строки{warn_e} Не закрашенный')  # Работает!
