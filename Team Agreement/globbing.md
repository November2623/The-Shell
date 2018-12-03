**Bash does not support native regular expressions like some other standard programming languages.
The Bash shell feature that is used for matching or expanding specific types of patterns is called globbing.
Globbing is mainly used to match filenames or searching for content in a file.
Globbing uses wildcard characters to create the pattern.
The most common wildcard characters that are used for creating globbing patterns are described below.**

-------------------------------------------------------------------
RESOURCE:
1. https://linuxhint.com/bash_globbing_tutorial/
2. https://www.linuxnix.com/regular-expressions-linux-i/
3. http://www.tldp.org/LDP/abs/html/

FOR IMLEMMENTING:
1. https://docs.python.org/3.5/library/glob.html
2. https://docs.python.org/3.5/library/fnmatch.html#module-fnmatch
3. https://www.youtube.com/watch?v=qnWqJqV6mtY => Ex about module glob
4. https://www.youtube.com/watch?v=K8L6KVGG-7o => re module
5. https://www.youtube.com/watch?v=hgFBRZmwpSM => 5 PARTS IN SERIES done
#######################################################################

Giả sử trong directory có các file:
    + file1.txt
    + file2.txt
    + dir1
    + dir2
    + shell.py
    + globbing.md

#######################################################################

###
BASIC

? - 0 or exactly 1 character
* – 0 or more characters
[] – Range of character
\ - "escape" character
-----------------
^ –>Caret/Power symbol to match a starting at the beginning of line.
$ –>To match end of the line
. –>To match any character
[^char] –>negate of occurrence of a character set
! ->reverses the condition : none of
+ -> 1 or more characters : at least 1 of
@ -> only 1 character : 1 of

- Globbing làm việc trong thư mục hiện tại, ko đi vào thư mục con,
  phải truyền đường dẫn tùy ý nếu muốn thư mục khác
        + ls ../../hello.txt
###
1. Question mark – (?):
đúng số lượng ký tự, trước sau hay ở giữa đều dc
(?) is used to match any single character.
You can use ‘?’ for multiple times for matching multiple character

Test case:
    - ls ?????.txt => file1.txt  file2.txt
    - ls ?????.py => shell.py
    - ls ???? => dir1 dir2
    - ls file????? => file1.txt  file2.txt
    - ls fi?????xt => file1.txt  file2.txt

###
2. Asterisk – (*):không cần đúng số lượng kỹ tự, vị trí ko thành vấn đề (đầu, cuối, giữa)
(*) is used to match zero or more characters.
If you have less information to search any file or information
then you can use ‘*’ in globbing pattern

Test case:
    - ls *1* => file1.txt dir1
    - ls *file* => file1.txt  file2.txt
    - ls d* => dir1 dir2
    - ls *md => globbing.md(*)

###
3. Square Bracket – ([]) match với 1 trong những ký tự trong []
‘[]’ is used to match the character from the range.
Some of the mostly used range declarations are mentioned below.
[[:upper:]] or [A-Z]
[[:lower:]] or [a-z].
[[:digit]] or [0-9]
[[:alpha:]] or [a-zA-z]
[[:alnum:]] or [a-zA-Z0-9]
[[:space:]] whitespace (spaces, tabs, newlines)
[[:graph:]] printable characters excluding space
[[:print:]] printable characters including space
[[:punct:]] punctuation characters
[[:class:]] - any character that is a memnber of the class [:class:]

Test case:
      - files and folders whose name starts with any character f->s : ls [f-s]*
            => file1.txt  file2.txt  globbing.md  shell.py
      - ls *[d-i]* => dir1 dir2
      - ls *[e-g]* => check.sh  file1.txt  file2.txt  globbing.md  shell.py
            (tìm trong chuỗi có bất kỳ kí tự nào từ e->g ở đâu cũng lấy)
      - ls [f-l]*[e-g]* => file1.txt  file2.txt  globbing.md
            (chuỗi có có 1 ký tự trong khoảng f->l sau đó là 1 ký tự từ e-g)
      - ls *[uioea]??.* => atest.txt  check.sh  list.txt  menu.bash  shell.py
      - ls *[[:digit:]]*
          => file1.txt  file2.txt  file3.txt dir1:

+ Given ['a.js', 'b.js', 'c.js', 'd.js', 'E.js']
      - [ac].js: matches both a and c, returning ['a.js', 'c.js']
      - [b-d].js: matches from b to d, returning ['b.js', 'c.js', 'd.js']
      - [b-d].js: matches from b to d, returning ['b.js', 'c.js', 'd.js']
      - a/[A-Z].js: matches and uppercase letter, returning ['a/E.md']
+ work the same way as the logical OR operator.
  For example, (a|b) will achieve the same result as {a,b}.
      - (a|c).js: would match either a or c, returning ['a.js', 'c.js']
      - (b|d).js: would match either b or d, returning ['b.js', 'd.js']
      - (b|[A-Z]).js: would match either b or an uppercase letter, returning ['b.js', 'E.js']

###
4. Caret – (^)
bắt buộc phải bắt đầu với gì đó phái sau

[^abc]* match all EXCEPT what is in the brackets
      => tức là ko được có a hay b hay c ở đầu, sau đó là * thì tùy ý


###
5. Exclamatory Sign – (!) các kí tự bắt đầu sau dấu ! ko được có mặt
You can use ‘!’ inside the range pattern.
It works same as the use of ‘^’ symbol outside the range pattern.
Some examples of using ‘!’ sign are given below

$ grep [!P-R] list.txt
$ grep [!4-8] list.txt

###
6. Dollar Sign – ($) - search bằng ký tự cuối cùng

      - $ grep 50$ list.txt
      - $ grep live$ list.txt

###
7. Curly bracket – ({})
  - ‘{}’ can be used to match filenames with more than one globbing patterns.
    Each pattern is separated by ‘,’ in curly bracket without any space.
  - work the same way as the logical OR operator.
    For example, (a|b) will achieve the same result as {a,b}.

      - ls -l {?????.sh,*.txt}
      - wc {*.txt,* .md} nhớ xóa dấu cách đi
      - range expansion: a{1..3}b/*.js expands to: ['a1b/*.js', 'a2b/*.js', 'a3b/*.js']
      - nesting: a{c,{d,e}}b/*.js expands to: ['acb/*.js', 'adb/*.js', 'aeb/*.js']

###
8. Pipe– ( | ) - LOGIC OR
‘|’ sign is also used for applying more than one condition on globbing pattern. Each pattern is separated by ‘|’ symbol in the command.

      - ls a*+(.bash|.sh)
        => ko có, vì trong dir hiện tại ko có file nào bắt đầu bằng "a"
          (Run the following command to search those filenames which are starting with character ‘a’ and has the extension ‘bash’ OR ‘sh)
      - ls [a-h] * +(.bash|.sh|.txt) => check.sh  file1.txt  file2.txt
           - kí tự đầu là từ a->h
           - tiếp theo tùy ý vì có *
           - sau đó là có đuôi .bash hay .sh hay .txt

###
9. '\' escape character: để bỏ qua, giữ nó đúng như nó, treat a Metachracter as a literal

==================================
String Literal ?
Metachracter ?
Search Expression ?
Escape Sequence => treat a Metachracter as a literal
Subtitution
Widcard expansion
Joker
====================================
