# Search-file-for-matches-and-perform-an-operation
Search file for matches and perform an operation

This script takes a filename, a regular expression, and an action as input. The script
searches the file for occurrences that match the regular expressions and perform some
action, see usage for more information.

Usage:
search.py [-h] --pattern PATTERN [--list] [--list-lines] [--number] [--count] [--delete-lines] 
[--replace REPLACE] [--cipher CIPHER] [--out OUT] file


Search a file for patterns and perform different operations

positional arguments:
file    input file

optional arguments:
-h, --help            show this help message and exit
--pattern PATTERN, -p PATTERN
                      regular expression to match file content
to
--list, -l            list matches in the file
--list-lines          print lines that contain matches
--number              print line numbers before matches
--count, -c           only count matches in the file
--delete-lines        delete lines that contain matches from
input file
--replace REPLACE, -r REPLACE
                      string to replace matches with
--mask MASK           a character to mask matches with (e.g: word
becomes **** if mask is *)

--out OUT, -o OUT     output file to write changes to instead
of applying them to input file
