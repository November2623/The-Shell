#!/usr/bin/env python3
import os

def handle_cd(command):
    # got to HOME

    if len(command) == 1 or command[1] == "~":
        if "HOME" in os.environ.keys():
            os.environ.update({"OLDPWD": os.getcwd()})
            os.chdir(os.environ["HOME"])
        else:
            print("intek-sh: cd: HOME not set")
    elif command[1] == "-":
        os.environ.update({"OLDPWD": os.getcwd()})
        os.chdir(os.environ["OLDPWD"])
    elif os.path.isfile(command[1]) is True:
        print("bash: cd: %s: Not a directory" % command[1])
    elif os.path.isdir(command[1]) is False:
        print("bash: cd: %s: No such file or directory" % command[1])
    else:
        os.environ.update({"OLDPWD": os.getcwd()})
        os.chdir(command[1])
    os.environ.update({"PWD": os.getcwd()})


def handle_export(command):
    list_export = command[1:]
    for item in list_export:
        if "=" in item:
            key = item.split("=")[0]
            value = item.split("=")[1]
            os.environ.update({key: value})
        else:
            os.environ.update({item: ''})


def handle_unset(command):
    list_unset = command[1:]
    for key in list_unset:
        if key in os.environ.keys():
            del os.environ[key]


def handle_exit(command): ## need to rebuilt
    print("exit")
    
