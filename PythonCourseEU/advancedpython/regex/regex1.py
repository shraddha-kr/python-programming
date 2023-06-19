""" Rules of Regex
# re.search(expr,s) checks a string s for an occurrence of a substring which matches the regular expression expr. The first substring (from left), which satisfies this condition will be returned. If a match has been possible, we get a so-called match object as a result, otherwise the value will be None. This method is already enough to use regular expressions in a basic way in Python programs.
# The syntax of regular expressions supplies a metacharacter ".", which is used like a placeholder for "any character". 
# Square brackets, "[" and "]", are used to include a character class. [xyz] means e.g. either an "x", an "y" or a "z". 
# To manage such character classes, the syntax of regular expressions supplies a metacharacter "-". [a-e] a simplified writing for [abcde] or [0-5] denotes [012345].
# The dash has only a special meaning if it is used within square brackets and in this case only if it isn't positioned directly after an opening or immediately in front of a closing bracket. So the expression [-az] is only the choice between the three characters "-", "a" and "z", but no other characters. The same is true for [az-].
# The only other special character inside square brackets (character class choice) is the caret "^". If it is used directly after an opening sqare bracket, it negates the choice. [^0-9] denotes the choice "any character but a digit". The position of the caret within the square brackets is crucial. If it is not positioned as the first character following the opening square bracket, it has no special meaning. [^abc] means anything but an "a", "b" or "c" [a^bc] means an "a", "b", "c" or a "^"
Predefined character classes
The special sequences consist of "\\" and a character from the following list:
\d  Matches any decimal digit; equivalent to the set [0-9].
\D  The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
\s  Matches any whitespace character; equivalent to [ \t\n\r\f\v].
\S  The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
\w  Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
\W  Matches the complement of \w.
\b  Matches the empty string, but only at the start or end of a word.
\B  Matches the empty string, but not at the start or end of a word.
\\  Matches a literal backslash.
Virtual Matching characters
The caret (^), which is used to mark the beginning of a string, and the dollar sign ($), which is used to mark the end of a string, respectively. \A and \Z, which can also be found in our previous diagram, are very seldom used as alternatives to the caret and the dollar sign.
match(re_str, s) checks for a match of re_str merely at the beginning of the string.
The caret '^' matches the start of the string, and in MULTILINE (will be explained further down) mode also matches immediately after each newline, which the Python method match() doesn't do. The caret has to be the first character of a regular expression:
"""
import re
x = re.search("cat", "A cat and a rat can't be friends.")
print(x)

y = re.search("cow", "A cat and a rat can't be friends.")
print(y)
