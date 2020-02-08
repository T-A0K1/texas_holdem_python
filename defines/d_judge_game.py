#return the winner player's number
#kekka_list_: all player's hand by list form(from judge_hand())
def judge_game(kekka_list_):
    n_ = len(kekka_list_)
    win_ = 0
    draw_player_ = []
    
    for i in range(1,n_):
        if kekka_list_[i][0] > kekka_list_[win_][0]:
            win_ = i
        #when same role
        elif kekka_list_[i][0] == kekka_list_[win_][0]:
            for j in range(len(kekka_list_[i])):
                if kekka_list_[i][j] > kekka_list_[win_][j]:
                    win_ = i
                    break
                elif kekka_list_[i][j] < kekka_list_[win_][j]:
                    break
            if j == (len(kekka_list_[i])-1):
                draw_player_.append(win_)
                draw_player_.append(i)
    #if draw, return draw player's number
    #so, if draw, len(return_val)>1, else len(return_val)==1 
    if len(draw_player_) > 1:
        return draw_player_
    else:
        return [win_]
