THERE ARE 4 MAIN BASIC CASE:
Only "."
1. "=" in command:
    => STORE VARIABLE
2. IF PATH: contain "/" in command, esxist in current working directory
    2.1. Handle PATH: return PATH
        - 2.1.1 Case 1: START with the slash "/"
                => the *ABSOLUTE* PATH
        - 2.1.2 Case 2: START with the slash "."
                - Sub Case 1: ". "
                    + phia sau bat dau bang "/...." => 2.1.1
                    + phia sau la script => binary run file
                        get after "."
                        "menu.sh" => sh menu.sh
                        "menu.bash" => bash menu.bash
                - Sub Case 2: "./" =>  check permission
                => CURRENT WORKING DIRECTORY
        - 2.1.3 Case 3: else
                => *RELATIVE* PATH
    2.2. Check PATH:
        - Case 1: PATH don't exists
                => message "No such file or directory"
        - Case 2: PATH is a directory
                => message "Is a directory"
                case:
                    . dir-sub/
                    . dir-sub
                    dir-sub => nope PATH
                    dir-sub/
        - Case 3: PATH is a file/script
                (???? handle permission, catch Error ?????? like minish)
                - if script can be executed line by line
                (NOTE: 2 types of file can be executed: .sh(like system) or .py .cpp .java) !!!???
                        => run subprocess.run()
                - else: (like test.txt team.md)
                        => message "Command not found"
3. IF [bultin-name or external-file] [arguments]:  Don't have any slash - /" in bultin-name or external-file:
    3.1. Bultin- create by out team - and import as a module
    3.2. External-file:
            3.1.1 handle variables environment => split PATH by ":" => done
            3.1.2 Check matching with path or not
            - Case 1: If matching with PATH variables environment
                    => Call Builtin
            - Case 2: else:
                    => message "Command not found"
    3.3. Script:
            run subprocess
 
