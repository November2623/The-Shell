        read
process <= terminal character  device file
        =>
        write

process command: program-name arguments
                 ls           -laR    
                 ls           -l -a -R
#####################################################33

There are *4* cases:
    + don't have any slash "/" on the command => program-name arguments:
        find in path variables
            + if math => excute
            + else => raise error "command not found"
        Case:
            + foo
            + ls -l
            + wc file3.txt
            + head file1.txt
            .......

    + _START WITH the slash "/"_ in command => the *ABSOLUTE* path to an executable file
        look for that file
            + if don't exists => no such file or directory
            + if it is a directory => return message "Is a directory"
            + if it is a file:
                  + check, the content in file be "list of command"
                         + if can be execute line by line
                                => run process
                         + else: (file .txt)
                                => each line : return message "command not found"

    + The slash - "/" exists in the command, but not at the start => the *RELATIVE* path to an executable file
        ``ALL CASES ARE SAME WITH CASE 2``
        look for that file in the ``CURRENT WORKING DIRECTORY``
        pay attention : *ABSOLUTE path* => /........ (tức là đi từ root mà đi ra)
                        *RELATIVE path* => ...../..../../ (đi từ dir hiện tại sang chỗ khác)


    + _START WITH the slash "."_ in command => equivalent with case 3
        look for that file in the ``CURRENT WORKING DIRECTORY``

###############################################
1. shell forks itself
2. parent waits for child
3. child exec's the command, passing the argument


###
character with special meaning:
' " \ $ ` ` * ~ ? < > ( ) ! | & ; # space newline
disable the special meaning ~~ escape character: \ (vo hieu hoa)
quotes every enclosed Metachracter: ''
quotes enclosed Metachracter except $ ` ` \ ! * @: ""
foo=4
echo "$foo" => 4 => fail in some exception $ ` ` \ ! * @: ""
echo '$foo' => $foo => escape character
####################################################

every command returns a numberric _exit status_
    + 0 means *OKE* => the command completed successfully without error
    + non-0 means *Error*
###
=> The way to get the numberic return is "echo $?""



###################################################

commandA && commmandB
    if last command of A returns 0, then run B
commandA || commmandB
    if last command of A return non-0, then run B

###################################################
_write a function_
function foo {
  ls
  cat file*
  pwd /
}
call : foo

The order:
1. function call
2. built-in command
3. process command

########################################################
shell ====== "subshell" ========= command process
       fork             fork, exec, wait

###
subshel with *()* parentheses: ngoặc đơn => (command-list) => execute in a subshell
      + (  pwd  ;   ls -l )
      + (  cd /  ;   ls -l; ) => lệnh cd ko có tác dụng ở prompt main shell vì nó là subshell
Note: khoảng cách ko quan trọng

###
{command-list} => execute in the current shell
      + {pwd ; ls-l;}
      + { cd ; pwd  ;   ls -l  ; } => current working directory đã thay đổi theo cd
Note: khoảng cách không quan trọng
      nhưng phải có ";" liền kề trái sau mỗi command
      command đầu tiên ko dc sát "{"

###
*&* - terminated pipeline runs "in background"
1. shell doesn't wait for the pipeline
2. pipeline run in a subshell
3. the pipeline may not read the terminal
4. the pipeline may (or may not) write to the terminal
        + (cd /; ls -l;) & => thực hiện subshell trong () sau đó chờ command tiếp theo
        + { cd /; ls -l;} & => same ở trên


##########################################3
### JOB CONTROL => BONUS
