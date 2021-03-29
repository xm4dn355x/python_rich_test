# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from rich.console import Console


console = Console(
    color_system='standard',
    force_terminal=True,
    force_jupyter=False,
    force_interactive=True,
    # soft_wrap=,
    # theme=,
    stderr=False,
    file=None,
    quiet=False,
    width=400,
    height=1000,
    style=None,
    no_color=False,
    tab_size=8,
    record=False,
    markup=True,
    emoji=True,
    highlight=True,
    log_time=True,
    log_path=True,
    log_time_format="[%X]",
    # highlighter=,
    legacy_windows=None,
    safe_box=True,
    get_datetime=None,
    get_time=None,
    _environ=None
)


if __name__ == '__main__':
    console.print('[bold yellow on red]HELLO WORLD!!!')
