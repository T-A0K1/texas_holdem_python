import numpy as np
import random
import collections

from defines.d_get_keys_from_value import *
from defines.d_make_library import *
from defines.d_judge_game import *
from defines.d_judge_hand import *

hand = make_library()[:7]
hand2 = make_library()[:7]
kekka = judge_hand(hand)
kekka2 = judge_hand(hand2)
print(hand)
print(hand2)
print(kekka)
print(kekka2)
print(judge_game([kekka, kekka2]))

