
from defines.d_get_keys_from_value import *
from defines.d_make_library import *
from defines.d_judge_game import *
from defines.d_judge_hand import *

library_card = make_library()

hand = [library_card.pop(0) for _ in range(2)]
hand2 = [library_card.pop(0) for _ in range(2)]
field_card = [library_card.pop(0) for _ in range(5)]
kekka = judge_hand(hand+field_card)
kekka2 = judge_hand(hand2+field_card)

print("player0's hand:",hand)
print("player1's hand:",hand2)
print("field card:",field_card)
print("player0's role:",kekka)
print("player1's role:",kekka2)
print("win player:",judge_game([kekka, kekka2]))

