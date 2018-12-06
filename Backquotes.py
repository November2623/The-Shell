# from shell import handle_execute_command, handle_rough_command
from subprocess import PIPE, run
import os, subprocess
# command = ['cat', 'File1']
# result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
# a = result.stdout

# def handle_exucute_command_substitution(command):

def handle_rough_command(rough_commands):
    """
    1. split line by "\n" in command
    2. plit program-name and argument by " " in command
    """
    result_command = []
    rough_commands = rough_commands.split("\\n") # 1
    for command in rough_commands:
        if command.startswith('`') and command.endswith('`'):
            result_command.append(command)
        else:
            command = command.split() # 2
            for i in command:
                result_command.append(i)
    return result_command


def check_command_substitution(command):
    for i in command:
        if i.startswith('`') and i.endswith('`'):
            return True
    return False


def command_substitution(command):
    # if len(command) == 1:
    #     result = run([command[0][1:-1]], stdout=PIPE, universal_newlines=True)
    #     if os.path.isdir((result.stdout).strip()):
    #         print('bash: ' + result.stdout.strip() + ": Is a directory")
    #
    for i in range(len(command)):
        if check_command_substitution(command[i]):
            list = handle_rough_command(command[i][1:-1])
            command_substitution(list)
        else:
            print(1)

command_substitution("`pwd`")