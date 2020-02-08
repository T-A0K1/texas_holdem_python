import random
def make_library():
    cards_ = []
    for i in range(2,15):
        for j in [1,2,3,4]:
            cards_.append(int(str(i) + str(j)))
    random.shuffle(cards_)
    return cards_
