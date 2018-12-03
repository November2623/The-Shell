
_MAIN STRUCTURE_
Special case:
    1.
    2.

Usual Case:
    1. PATH


    menu.bash
    check.sh
    shell.py
    => "name" command not found => IT IS NOT KNOWN AS A PATH => bUILTIN

    ./menu.bash => denied
    ./check.sh => denied
    ./shell.py => denied
    => check permission

    . menu.bash => success
    . check.sh => success
    . shell.py => error
    => run as a binary file

2. COMMAND-NAME [ARGUMENTS]




_FEATURE 1: GLOBBING_


###########################
1. check external file => open path
2. check bUILTIN => create a list contains name-builtin
