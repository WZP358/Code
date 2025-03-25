from A import Queue
def hotPotato(namelist,num):
    s=Queue()
    for name in namelist:
        s.enqueue(name)
    while s.size()>1:
        for i in range(num-1):
            s.enqueue(s.dequeue())
        s.dequeue()
    return s.dequeue()

namelist=['A','B','C','D','E','F','G','H','I']
print(hotPotato(namelist,7))