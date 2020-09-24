def cypher(str, num):
  encrypt = ''
  abc = 'abcdefghijklmnopqrstuvwxyz'
  ABC = abc.upper()
  for i in range(len(str)):
    char = str[i]
    if char.isupper():
      index = ABC.find(char)
      rotated = (index + num) % 26
      letter = ABC[rotated]
    elif char.islower():
      index = abc.find(str[i])
      rotated = (index + num) % 26
      letter = abc[rotated]
    else:
      letter = str[i]
    encrypt = encrypt + letter
  return encrypt
print(cypher(cypher('heLLo woRLd!', 13),13))