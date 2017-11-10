cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

cnt
Out[17]: Counter({'blue': 3, 'green': 1, 'red': 2})


import re
words = re.findall(r'\w+', open('test.txt').read().lower())
Counter(words).most_common(10)

Out[20]:
[('the', 37),
 ('and', 22),
 ('of', 19),
 ('in', 19),
 ('a', 18),
 ('to', 18),
 ('hamlet', 15),
 ('is', 12),
 ('as', 12),
 ('play', 10)]


from collections import deque
d = deque('Alinafe')             # make a new deque with seven items
for elem in d:                   # iterate over the deque's elements
     print(elem.upper())

def tail(filename, n=10):
    #Return the last n lines of a file
    with open(filename) as f:
        return deque(f, n)

tail('test.txt')
Out[26]:
deque(['Dramatic structure[edit]\n',
       'Hamlet departed from contemporary dramatic convention in several ways. For example, in Shakespeare\'s day, plays were usually expected to follow the advice of Aristotle in his Poetics: that a drama should focus on action, not character. In Hamlet, Shakespeare reverses this so that it is through the soliloquies, not the action, that the audience learns Hamlet\'s motives and thoughts. The play is full of seeming discontinuities and irregularities of action, except in the "bad" quarto. At one point, as in the Gravedigger scene,[a] Hamlet seems resolved to kill Claudius: in the next scene, however, when Claudius appears, he is suddenly tame. Scholars still debate whether these twists are mistakes or intentional additions to add to the play\'s themes of confusion and duality.[79] Hamlet also contains a recurrent Shakespearean device, a play within the play, a literary device or conceit in which one story is told during the action of another story.[g]\n',
       '\n',
       'Length[edit]\n',
       "Hamlet is Shakespeare's longest play. The Riverside edition constitutes 4,042 lines totaling 29,551 words, typically requiring over four hours to stage.[81][h] It is rare that the play is performed without some abridgments, and only one film adaptation has used a full-text conflation: Kenneth Branagh's 1996 version, which runs slightly more than four hours.\n",
       '\n',
       'Language[edit]\n',
       '\n',
       "Hamlet's statement that his dark clothes are the outer sign of his inner grief demonstrates strong rhetorical skill (artist: Eugène Delacroix 1834).\n",
       "Much of Hamlet'"])
