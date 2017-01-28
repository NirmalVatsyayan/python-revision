Regular Expression Modifiers: Option Flags


re.I   -   Performs case-insensitive matching.

re.M   -   Makes $ match the end of a line (not just the end of the string) 
           and makes ^ match the start of any line (not just the start of the string).

re.S   -   Makes a period (dot) match any character, including a newline.

re.U   -   Interprets letters according to the Unicode character set. 
           This flag affects the behavior of \w, \W, \b, \B.



Regular Expression Patterns

^          -   Matches beginning of line.
$          -   Matches end of line.
.          -   Matches any single character except newline. 
               Using m option allows it to match newline as well.
[...]      -   Matches any single character in brackets.
[^...]     -   Matches any single character not in brackets
re*        -   Matches 0 or more occurrences of preceding expression.
re+        -   Matches 1 or more occurrence of preceding expression.
re?        -   Matches 0 or 1 occurrence of preceding expression.
re{ n}     -   Matches exactly n number of occurrences of preceding expression.
re{ n,}    -   Matches n or more occurrences of preceding expression.
re{ n, m}  -   Matches at least n and at most m occurrences of preceding expression.
a| b       -   Matches either a or b.
(?= re)    -   Specifies position using a pattern. Doesn't have a range.
#\w        -   Matches word characters.
#\W	       -   Matches nonword characters.
#\s	       -   Matches whitespace. Equivalent to [\t\n\r\f].
#\S	       -   Matches nonwhitespace.
#\d	       -   Matches digits. Equivalent to [0-9].
#\D	       -   Matches nondigits.
#\A	       -   Matches beginning of string.
#\Z	       -   Matches end of string. If a newline exists, it matches just before newline.
#\z	       -   Matches end of string.
#\G	       -   Matches point where last match finished.
#\b	       -   Matches word boundaries when outside brackets. 
               #Matches backspace (0x08) when inside brackets.
#\n,\t,etc -   Matches newlines, carriage returns, tabs, etc.



EXAMPLES

[Pp]ython	   -     Match "Python" or "python"
rub[ye]	       -     Match "ruby" or "rube"
[aeiou]	       -     Match any one lowercase vowel
[0-9]	       -     Match any digit; same as [0123456789]
[a-z]	       -     Match any lowercase ASCII letter
[A-Z]	       -     Match any uppercase ASCII letter
[a-zA-Z0-9]	   -     Match any of the above
[^aeiou]	   -     Match anything other than a lowercase vowel
[^0-9]	       -     Match anything other than a digit
ruby?	       -     Match "rub" or "ruby": the y is optional
ruby*	       -     Match "rub" plus 0 or more ys
ruby+	       -     Match "rub" plus 1 or more ys
#\d{3}	       -     Match exactly 3 digits
#\d{3,}	       -     Match 3 or more digits
#\d{3,5}	   -     Match 3, 4, or 5 digits



