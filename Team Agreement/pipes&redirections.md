1. https://www.ceos3c.com/open-source/pipes-and-redirection-in-linux-explained/
2. https://ss64.com/bash/syntax-redirection.html
3. https://www.tutorialspoint.com/unix/unix-io-redirections.htm
4. https://www.maketecheasier.com/pipes-redirection-for-linux-command-line/
5. http://homepages.uc.edu/~thomam/Intro_Unix_Text/IO_Redir_Pipes.html
6. https://askubuntu.com/questions/172982/what-is-the-difference-between-redirection-and-pipe
7. https://developer.ibm.com/tutorials/l-lpic1-103-4/
8. https://www.youtube.com/watch?v=xHu7qI1gDPA&list=PLX1h5Ah4_XcfL2NCX9Tw4Hm9RcHhC14vs => Unix system calls (1/2) maybe
9. https://www.youtube.com/watch?v=2DrjQBL5FMU => Unix system calls (2/2) bài cũ
10. https://www.youtube.com/watch?v=jbzrz0aSgEY
11. https://www.youtube.com/watch?v=EL4hCQc7KXY

##########################################################################

_REDIRECTION_
1. program forks itself
2. child closed stdin and/or stdout
3. child opens file(s)
4. child exec's new program

STDIN file descriptor 0
STDOUT file descriptor 1

*<* close fd 0 and open file for reading
*>* close fd 1 and open file for writing

; => ngăn cách từng commmand cùng 1 dòng
ví dụ
      - whoami ; pwd ; ls và (whoami ; pwd ; ls) là như nhau
            => output lần lượt hết trên screen
      - whoami ; pwd ; ls > file4.txt
            => cách cmd độc lập, whoami và pwd in trên screen, còn kết quả của ls ghi vào file4.txt
      - ( whoami ; pwd ; ls ) >> file4.txt
            => append (>>) hết kết quả của 3 cmd trên vào file4.txt


##########################################################################

Output redirection
- '>' => The '>' symbol is used for output (STDOUT) redirection.
      - chèn đè(nếu có sẵn), viết vào file mới chưa có
- '>>' => add more content to an existing file, then you should use '>>' operator.
      - thêm vào sau (append)

test case:
      - cat file1.txt file2.txt > file3.txt
            => file3.txt dc tạo mới với nội dung file1.txt trước và sau là file2.txt
      - cat file1.txt >> file2.txt
            =>  file2.txt sẽ thêm nội dung file1.txt vào sau
      - ls ..... > ..... 2>&1
#############################
Input redirection
- '<' => The '<' symbol is used for input(STDIN) redirection


#############################
pipes: | lấy kết quả của phía trước, bỏ vào phía sau
