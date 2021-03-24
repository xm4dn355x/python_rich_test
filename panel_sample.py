# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from rich import print
from rich.panel import Panel


if __name__ == '__main__':
    panel = Panel.fit(
        renderable='testtesttesttesttesttesttesttesttesttesttesttest',
        # box=Box(),
        title='Заголовок',
        title_align='right',
        # safe_box=
        # style=
        border_style='red',
        width=200,
        padding=(0, 1)
    )
    print(panel)
