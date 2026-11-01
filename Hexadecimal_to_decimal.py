a = 0x17bbe
b=0x13
'''c=0x12g # gives Syntax error :
print(c)    # invalid hexadecimal literals
print(type(c))
'''
print(b,type(b), "address of b =" ,id(b))
print(a,type(a),id(a))
'''z = 0243 # SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
print(z)'''