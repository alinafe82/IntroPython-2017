import pprint
message='It was a bright cold day in April, and the clock was ticking'
count={}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

print('default print')
print(count)

print('pretty print')
pprint.pprint(count)

rjtext= pprint.pformat(count)
print(rjtext)