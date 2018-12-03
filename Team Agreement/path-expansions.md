RESOURCE:
1. https://guide.bash.academy/expansions/ => USEFULL
2. http://www.linuxcommand.org/lc3_lts0080.php => basic
3. https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html#Tilde-Expansion
4. https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html#Shell-Parameter-Expansion => need read more
5. http://wiki.bash-hackers.org/syntax/pe =>> provide good test case
6. https://bash.cyberciti.biz/bash-reference-manual/Directory-Stack-Builtins.html#Directory-Stack-Builtins

FOR IMPLEMENTING
os.path.expanduser() and expandvars()
os.path....


#########################################################################

The order:
1. brace expansion
2. *tilde expansion*
3. *parameter expansions*, variable expansion, arithmetic expansion, command substitution
4. Word splitting
5. Pathname expansion


#########################################################################

1. brace expansion {}
      + echo abc{1,2,3}def => abc1def abc2def abc3def
      + echo {1,2,3}nhu{4,5,6} => 1nhu4 1nhu5 1nhu6 2nhu4 2nhu5 2nhu6 3nhu4 3nhu5 3nhu6


2. _tilde expansion_ ~ mean: /home/dnhu => home directory
      + ~ => /home/dnhu
      + ~/dir1 => /home/dnhu/dir1
      + ~+/foo => $PWD/foo
      + ~-/foo => ${OLDPWD-'~-'}/foo
      + ~N hay ~+N => The string that would be displayed by ‘dirs +N’
      + ~-N => The string that would be displayed by ‘dirs -N’


3. command substitution_ $(command) or `command` sẽ run trước
      + echo 'Hello world.' > hello.txt
        cat hello.txt
          => Hello world.
      + echo "The file <hello.txt> contains: $(cat hello.txt)"
          => The file <hello.txt> contains: Hello world.
      + echo "hello $(ls -l; pwd)"
          => trong $(ls -l; pwd) sẽ run trước


4. arithmetic substitution $((expression))
(bieu thuc toan)

5. filename expansion * (0 or more) ? (only 1) go to globbing

6. _parameter expansions_ 2 cases
      + $PARAMETER
      + ${PARAMETER}
Ex:
      + name=Britta time=23.73
        echo $name $time
            => Britta 23.73
      + echo "$name's current record is ${time}s."
            => Britta's current record is 23.73s.
      + echo "$name's current record is ${time%.*} seconds and ${time#*.} hundredths."
            => Britta's current record is 23 seconds and 73 hundredths.
                (% để xóa dấu . và các số phía sau, hay là lấy phần phía trc dấu .)
                (# để lấy phần phía sau dấu . )
      + echo "PATH currently contains: ${PATH//:/, }"
            => PATH currently contains: /Users/lhunath/.bin, /usr/local/bin, /usr/bin, /bin, /usr/libexec
                (// dùng để thay thế : trong PATH thành dấu , => //:/, )      
      + url='https://guide.bash.academy/variables.html'

            ${parameter#pattern} "${url#*/}"

            ${parameter##pattern} "${url##*/}"

            ${parameter%pattern} "${url%/*}"

            ${parameter%%pattern} "${url%%/*}"

            ${parameter/pattern/replacement} "${url/./-}"

            ${parameter//pattern/replacement} "${url//./-}"

            ${parameter/#pattern/replacement} "${url/#*:/https:}"

            ${parameter/%pattern/replacement} "${url/%.html/.jpg}"

            ${#parameter} "${#url}"

            ${parameter:start[:length]} "${url:7}"

            ${parameter[^|^^|,|,,][pattern]} "${url^^[ht]}"
