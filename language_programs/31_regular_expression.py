import re


'''
Finding / searching pattern in text


search using relugar expression
'''
'''
patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print('Looking for "%s" in "%s" -> ' % (pattern, text))
    
    print(re.search(pattern,text))

    if re.search(pattern,  text):
        print('found a match!')
    else:
        print('no match')

'''
'''
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e]))

'''
'''

#finding searching in compiled expression


# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that',
                                     ]
            ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print('Looking for "%s" in "%s" ->' % (regex.pattern, text))

    if regex.search(text):
        print('found a match!')
    else:
        print('no match')

'''

text = 'abbaaabbbbaaaaabab'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found "%s"' % match)