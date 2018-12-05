#!/usr/bin/env python3
from shell import handle_rough_command, identify_command, handle_execute_command

def main():
    """
    THOSE STEP PROCESSING:
    1. loop input command
    2. handle main processing
    3. handle the rough/hard command
    4. handle identification/expansion/parse command (argumuents/path)
            =>  features are here
    5. handle execute command

    """
    run_minish = True
    while run_minish:
        # 1. loop input command
        try:
            print("\033[1;32mintek-sh$ ", end='')
            rough_commands = input('\033[1;37m')
        except EOFError:
            return
        # 2. handle main processing

        # if rough_commands[0] == "exit":
        #     => handle later

        if rough_commands != '':
            list_command = handle_rough_command(rough_commands) # 3
            for command in list_command:
                # print(command)
                ########## using it when you implement the features
                # handled_command = identify_command(command) # 4
                # handle_execute_command(handled_command) # 5
                handle_execute_command(command)



main()
