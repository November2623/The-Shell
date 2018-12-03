#!/usr/bin/env python3
import os, subprocess


def handle_rough_command(rough_commands):
    """
    1. split line by "\n" in command
    2. plit program-name and argument by " " in command
    """
    result_command = []
    rough_commands = rough_commands.split("\\n") # 1
    for command in rough_commands:
        command = command.split() # 2
        result_command.append(command)
    return result_command



def identify_command():
    pass


def handle_execute_command(command):
    dic_var = {}
    # only dot "."
    if len(command) == 1 and command[0] == ".":
        print("bash: .: filename argument required\n.: usage: . filename [arguments]")

    # 1 VARIABLE
    elif "=" in command[0]:
        print(command[0])
        key = command[0].split("=")[0]
        value = command[0].split("=")[1]
        dic_var.update({key: value})

    # 2 PATH
    elif "/" in command[0] or command[0].startswith("."):
        path = handle_path(command)
        check_path(path, command)

    # 3 bultin-name or external-file or script
    else:
        if check_exists_command(command[0]) == "non_PATH":
            print("intek-sh: " + command[0] + ": No such file or directory")
        elif check_exists_command(command[0]) == "notfound":
            print("intek-sh: %s: command not found" % command[0])
        elif check_exists_command(command[0]) == "buildin":
            process_commands(command)
        else:
            if(len(command) == 1):
                subprocess.run(command[0])
            else:
                for arg in command[1:]:
                    subprocess.run([command[0], arg])



def handle_path(command):
    if command[0] == ".":
        if not command[1].startswith("/") or not command[1].startswith("./"):
            path = os.getcwd() + "/" + command[1]
    else:
        path = command[0]
    return path


def check_path(path, command):
    name = command[0]
    if command[0] == ".":
        name = ".: " + command[1]
    if os.path.exists(path) is False:
        print("bash: " + name + ": No such file or directory")
    elif os.path.isdir(path) is True:
        print("bash: " + name + ": Is a directory")
    elif os.path.isfile(path) is True:
        if os.access(path, os.X_OK) is False:
            if command[0] == ".":
                os.chmod(path, 0o755)
                subprocess.run(path)
            else:
                print("bash: " + name + ": Permission denied")
        else:
            subprocess.run(path)
    else:
        print("bash: %s: command not found" % name)


def check_exists_command(command):
    """
    if non-exists PATH -> False
    if non-exists command -> True
    exists command -> return where command
    """
    if command in ["cd", "unset", "export", "exit"]:
        return "buildin"
    if 'PATH' not in os.environ:
        return "non_PATH"
    PATH = os.environ['PATH'].split(':')
    for path in PATH:
        if(os.path.exists(path)):
            if command in os.listdir(path):
                return path
    return "notfound"


def process_commands(command):
    from builtin import handle_cd, handle_export, handle_unset, handle_exit
    processing = {'cd': handle_cd,
                  'unset': handle_unset,
                  'export': handle_export,
                  'exit': handle_exit }
    return processing[command[0]](command)
