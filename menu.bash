#!/bin/bash
echo "Select any option from the menu:"
read answer
case $answer in
1 | S )  echo "Searching text";;
2 | R )  echo "Replacing text";;
3 | D )  echo "Deleting text";;
*) echo "Try again.";;
esac
