from defines.d_get_keys_from_value import *
from defines.d_make_library import *
from defines.d_judge_game import *
from defines.d_judge_hand import *

import collections

hand_all = []
kekka_all = []
kekka_1 = []
for _ in range(10000):
    hand = make_library()[:7]
    hand_all.append(hand)
    tmp = judge_hand(hand)
    kekka_all.append(tmp)
    kekka_1.append(tmp[0])
kekka_1_colle = collections.Counter(kekka_1)
print(kekka_1_colle)
