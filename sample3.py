from defines.d_get_keys_from_value import *
from defines.d_make_library import *
from defines.d_judge_game import *
from defines.d_judge_hand import *

hand0 = [21,72] #set player0's hand

# save results
win_player_list = []
win_player_dic = {0:0, 1:0, 2:0} #each player's win count
# (if 2 players win, each player get half point. 3 players are even, get 1/3 point)

for _ in range(10000):
    library_card = make_library()

    for pref_ in hand0: 
        library_card.remove(pref_)
    hand1 = [library_card.pop(0) for _ in range(2)]
    hand2 = [library_card.pop(0) for _ in range(2)]
    field_card = [library_card.pop(0) for _ in range(5)]
    
    kekka0 = judge_hand(hand0+field_card) # player0
    kekka1 = judge_hand(hand1+field_card) # player1
    kekka2 = judge_hand(hand2+field_card) # player2
    
    tmp_result = judge_game([kekka0, kekka1, kekka2])
    
    # save result
    if len(tmp_result)>1: #draw
        win_player_list.append(99) 
    else:
        win_player_list.append(tmp_result[0])
    for p_ in tmp_result:
        win_player_dic[p_] += 1/(len(tmp_result)) #
    
win_player_list_np = np.array(win_player_list)
print('player0 win: ', np.sum(win_player_list_np==0)/len(win_player_list_np),
      ', player1 win: ',np.sum(win_player_list_np==1)/len(win_player_list_np),
      ', player2 win: ', np.sum(win_player_list_np==2)/len(win_player_list_np),
      ', draw(include 2 players win): ', np.sum(win_player_list_np==99)/len(win_player_list_np))
print(win_player_dic)