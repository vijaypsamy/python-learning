import os, random, States, pprint

l = []
states = list(States.capitals.values())


def choice(states, answer):

    c = None
    
    while c == None or c == answer:
        c = random.choice(states)

    return c

def shuffleAndWriteToFile(l):
    
    for i in range(35):
        s = open(os.path.join("H:\\Software\\Code\\QuizesGenerated", "Quiz"+str(i)), 'w')
        random.shuffle(l)
        s.write(pprint.pformat(l))
        s.close()

for i in States.capitals.items():

    c = [i[1], choice(states, i[1]),choice(states, i[1]),choice(states, i[1])]
    random.shuffle(c)
    
    print(c)
    
    q = {i[0]: c}
    l.append(q)



pprint.pprint(l)

shuffleAndWriteToFile(l)

        
