p = 'py'; t = 'th'; o = 'on'
print(p + t + o) #'python'

print(p * 4) # pypypypy
print(4 * p) # pypypypy


print('Python' in 'I love Python.') # True
print('Python' in 'I love Java.') # False

print('Python' not in 'I love Java.') # True
print('Java' not in 'I love Java.') # False

print(r'верн\ёт \n') # верн\ёт \n 
print(R'верн\ёт \n') # верн\ёт \n

print(F"{'foobar'[-1]} {'foobar'[-2]} {'foobar'[-3]}")

print('python'[2:5])  # tho

'python'[:4] # pyth
'python'[0:4] # pyth

s = 'python'
s[2:] # thon
s[2:len(s)] # thon

s[:4] + s[4:] # 'python'
s[:4] + s[4:] == s # True


t = s[:]
id(s)
id(t)
s is t # True

s[2:2]
s[4:2]

s[-5:-2] # 'yth'
s[1:4] # 'yth'
s[-5:-2] == s[1:4] # True

foo = 'foobar'
foo[0:6:2] # 'foa'
foo[1:6:2] # 'obr'


print(s[5:0:-2]) #'nhy'

gup = "─┌┐└┘├┤┬┴┼│"
print(gup) # ─┌┐└┘├┤┬┴┼│
print(gup[:: -1]) # │┼┴┬┤├┘└┐┌─

print(gup[1:2], end='')
print(gup[0] * 50, end='')
print(gup[2:3])


ord('a') # 97
ord('#') # 35

print(ord('€')) # 8364
print(ord('∑')) # 8721

chr(97) # 'a'
chr(35) # '#'

print(chr(8364)) # '€'
print(chr(8721)) # '∑'

# len(gup)

str(49.2) # '49.2'
str(3+4j) # '(3+4j)'
str(3 + 29) # '32'
str('py') # 'py'

# s = s[:3] + 'x' + s[4:] # 'pytton'
# s = s.replace('h', 't')

# s = 'everyTHing yoU Can IMaGine is rEAl'
# s.capitalize() # 'Everything you can imagine is real'

# s = 'follow us @PYTHON'
# s.capitalize() # 'Follow us @python'

# 'everyTHing yoU Can IMaGine is rEAl'.lower() #'everything you can imagine is real'
# 'everyTHing yoU Can IMaGine is rEAl'.swapcase() # 'EVERYthING YOu cAN imAgINE IS ReaL'

# 'the sun also rises'.title() # 'The Sun Also Rises'
# 'follow us @PYTHON'.title() # 'Follow Us @Python'
# 'follow us @PYTHON'.upper() # 'FOLLOW US @PYTHON'

# 'foo goo moo'.count('oo') # 3
# 'foo goo moo'.count('oo', 0, 8) # 2

# 'python'.endswith('on') # True
# 'python'.endswith('or') # False

# 'python'.endswith('yt', 0, 4) # True
# 'python'.endswith('yt', 2, 4) # False

# 'Follow Us @Python'.find('Us') # 7
# 'Follow Us @Python'.find('you') # -1

# 'Follow Us @Python'.find('Us', 4) # 7
# 'Follow Us @Python'.find('Us', 4, 7) # -1


# 'Follow Us @Python'.rfind('o') # 15
# 'Follow Us @Python'.rfind('a') # -1

# 'Follow Us @Python'.rfind('Us', 0, 14) # 7
# 'Follow Us @Python'.rfind('Us', 9, 14) # -1


# 'Follow Us @Python'.startswith('Fol') # True
# 'Follow Us @Python'.startswith('Go') # False

# 'Follow Us @Python'.startswith('Us', 7) # True
# 'Follow Us @Python'.startswith('Us', 8, 16) # False


# 'abc123'.isalnum() # True
# 'abc$123'.isalnum() # False
# ''.isalnum() # False

# 'ABCabc'.isalpha() # True
# 'abc123'.isalpha() # False

# '123'.isdigit() # True
# '123abc'.isdigit() # False

# 'foo32'.isidentifier() # True
# '32foo'.isidentifier() # False
# 'foo$32'.isidentifier() # False

# 'and'.isidentifier() # True

# from keyword import iskeyword
# iskeyword('and') # True

# 'abc'.islower() # True
# 'abc1$d'.islower() # True
# 'Abc1$D'.islower() # False

# 'a\tb'.isprintable() # \t - символ табуляции # False
# 'a b'.isprintable() # True
# ''.isprintable() # True
# 'a\nb'.isprintable() # \n - символ перевода строки # False

# ' \t  \n '.isspace() # True
# ' a '.isspace() # False
# '\f\u2005\r'.isspace() # True

# 'This Is A Title'.istitle() # True
# 'This is a title'.istitle() # False
# 'Give Me The #$#@ Ball!'.istitle() # True

# 'ABC'.isupper() # True
# 'ABC1$D'.isupper() # True
# 'Abc1$D'.isupper() # False

# 'py'.center(10) # '    py    '
# 'py'.center(10, '-') # '----py----'
# 'python'.center(2) # 'python'


# 'a\tb\tc'.expandtabs() # 'a       b       c'
# 'aaa\tbbb\tc'.expandtabs() # 'aaa     bbb     c'

# 'a\tb\tc'.expandtabs(4) # 'a   b   c'
# 'aaa\tbbb\tc'.expandtabs(tabsize=4) # 'aaa bbb c'

# 'python'.ljust(10) # 'python    '
# 'python'.ljust(10, '-') # 'python----'
# 'python'.ljust(2) # 'python'


# '   foo bar baz   '.lstrip() # 'foo bar baz   '
# '\t\nfoo\t\nbar\t\nbaz'.lstrip() # 'foo\t\nbar\t\nbaz'
# 'https://www.python.com'.lstrip('/:pths') # 'www.python.com'

# 'I hate python! I hate python! I hate python!'.replace('hate', 'love') # 'I love python! I love python! I love python!'
# 'I hate python! I hate python! I hate python!'.replace('hate', 'love', 2) # 'I love python! I love python! I hate python!'

# 'python'.rjust(10) # '    python'
# 'python'.rjust(10, '-') # '----python'
# 'python'.rjust(2) # 'python'

# '   foo bar baz   '.rstrip() # '   foo bar baz'
# 'foo\t\nbar\t\nbaz\t\n'.rstrip() # 'foo\t\nbar\t\nbaz'
# 'foo.$$$;'.rstrip(';$.') # 'foo'


# s = '   foo bar baz\t\t\t' 
# s = s.lstrip()
# s.rstrip() # 'foo bar baz'

# 'www.python.com'.strip('w.moc') # 'python'


# ', '.join(['foo', 'bar', 'baz', 'qux']) # 'foo, bar, baz, qux'

# list('corge') # ['c', 'o', 'r', 'g', 'e']
# ':'.join('corge') # 'c:o:r:g:e'

# 'foo.bar'.partition('.') # ('foo', '.', 'bar')
# 'foo@@bar@@baz'.partition('@@') # ('foo', '@@', 'bar@@baz')
# 'foo.bar'.partition('@@') # ('foo.bar', '', '')


# 'foo@@bar@@baz'.partition('@@') # ('foo', '@@', 'bar@@baz')
# 'foo@@bar@@baz'.rpartition('@@') # ('foo@@bar', '@@', 'baz')

# 'foo bar baz qux'.rsplit() # ['foo', 'bar', 'baz', 'qux']
# 'foo\n\tbar   baz\r\fqux'.rsplit() # ['foo', 'bar', 'baz', 'qux']
# 'foo.bar.baz.qux'.rsplit(sep='.') # ['foo', 'bar', 'baz', 'qux']
# 'foo...bar'.rsplit(sep='.') # ['foo', '', '', 'bar']
# 'foo\t\t\tbar'.rsplit() # ['foo', 'bar']
# 'www.python.com'.rsplit(sep='.', maxsplit=1) # ['www.python', 'com']

# 'www.python.com'.rsplit(sep='.', maxsplit=-1) # ['www', 'python', 'com']
# 'www.python.com'.rsplit(sep='.') # ['www', 'python', 'com']


# 'www.python.com'.split('.', maxsplit=1) # ['www', 'python.com']
# 'www.python.com'.rsplit('.', maxsplit=1) # ['www.python', 'com']

# 'foo\nbar\r\nbaz\fqux\u2028quux'.splitlines() # ['foo', 'bar', 'baz', 'qux', 'quux']
# 'foo\f\f\fbar'.splitlines() # ['foo', '', '', 'bar']

# 'foo\nbar\nbaz\nqux'.splitlines(True) # ['foo\n', 'bar\n', 'baz\n', 'qux']
# 'foo\nbar\nbaz\nqux'.splitlines(8) # ['foo\n', 'bar\n', 'baz\n', 'qux']
