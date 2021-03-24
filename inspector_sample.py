# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from rich import inspect
from rich.color import Color


if __name__ == '__main__':
    color = Color.parse("red")
    inspect(color, methods=True)    # Выводит всю инфу по классу в удобочитаемом виде
