# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from rich import pretty


pretty.install()    # Beautifuliser for python syntax and etc ONLY IN REPL MODE!


if __name__ == '__main__':
    print('["Rich and pretty", True]')
    print(locals())
