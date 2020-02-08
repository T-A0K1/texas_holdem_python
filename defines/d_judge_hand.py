#streat_flash:8, 4card:7,  full_house:6, flash:5, streat:4,
#3card:3, 2pair:2, 1pair:1, gomi:0

##
import numpy as np
import collections

##
#from defines.d_get_keys_from_value import *

def get_keys_from_value(d_, val_):
    return [k for k, v in d_.items() if v == val_]

def judge_hand(hand_):
    # hand_ from make_library()
    num_ = [i//10 for i in hand_]
    mark_ = [int(str(i)[-1]) for i in hand_]
    flash_ = 0
    
    #(1)flash_judge
    mark_colle_ = collections.Counter(mark_)
    max_mark_num_ = max(mark_colle_.values())
    if max_mark_num_ >= 5:
        flash_=1
    
    num_uniq_ = sorted(list(set(num_)))
    #(2)streat_judge
    def judge_streat_(num_uniq__):
        f__ = num_uniq__[0]
        st_tmp__ = ''
        for i in num_uniq__[1:]:
            st_tmp__ += str(i - f__)
            f__ = i
        if ( '1111' in st_tmp__) or (set(num_uniq__) >= set([2,3,4,5,14])):
            return 1
        else:
            return 0
    streat_ = judge_streat_(num_uniq_)
    
    #(3)return streat_hand's max card
    def make_streat_max_val_(num_uniq__):
        i_before__ = num_uniq__[0]
        strat_num__ = [num_uniq__[0]]
        for i in num_uniq__[1:]:
            if (i - i_before__)==1:
                strat_num__.append(i)
            elif len(strat_num__) >= 5:
                break
            else:
                strat_num__ = [i]
            i_before__ = i
        if len(strat_num__) < 5:
            strat_num__ = [5,4,3,2,1]#when top 5 streat
        return max(strat_num__)
    
    #streat flash
    if (flash_ ==1) & (streat_==1):
        #streat cards and flash cards are same or not
        flash_num_ = []
        max_mark_ = get_keys_from_value(mark_colle_, max(mark_colle_.values()))[0]
        for i in range(7):
            if mark_[i] == max_mark_:
                flash_num_.append(num_[i])
        flash_num_uniq_ = sorted(list(set(flash_num_)))
        streat_2_ = judge_streat_(flash_num_uniq_)
        if streat_2_==1:
            return [8,make_streat_max_val_(flash_num_uniq_)]
    
    #how many same cards
    num_colle_ = collections.Counter(num_)
    num_max_count_ = max(num_colle_.values())
    
    #4card
    if num_max_count_ ==4:
        #4card's num
        num_4_ = get_keys_from_value(num_colle_, 4)[0]
        #kicker
        num_uniq_.remove(num_4_)
        kikkar_4_ = max(num_uniq_)
        return [7, num_4_, kikkar_4_]
    
    #full_house, 3card
    if num_max_count_ ==3:
        num_3_ = get_keys_from_value(num_colle_, 3)
        if (2 in num_colle_.values()):
            return [6, max(num_3_), max(get_keys_from_value(num_colle_, 2))]
        #when two 3cards in hand
        elif len(get_keys_from_value(num_colle_, 3)) == 2:
            return [6, max(num_3_), min(num_3_)]
        elif (flash_ ==0) & (streat_==0):
            num_uniq_.remove(max(num_3_))
            return [3, max(num_3_), num_uniq_[-1], num_uniq_[-2]]
    
    #flash
    if flash_==1:
        flash_mark_ = get_keys_from_value(mark_colle_, max_mark_num_)[0]
        flash_num_ = []
        for i in range(7):
            if mark_[i] == flash_mark_:
                flash_num_.append(num_[i])
        flash_num_.sort()
        return [5, flash_num_[-1], flash_num_[-2], flash_num_[-3], flash_num_[-4], flash_num_[-5]]
    
    #streat
    if streat_ == 1:
        i_before_ = num_uniq_[0]
        strat_num_ = [num_uniq_[0]]
        for i in num_uniq_[1:]:
            if (i_before_-i)==1:
                strat_num_.append(i)
            else:
                strat_num_ = [i]
            i_before = i
        if len(strat_num_) < 5:
            strat_num_ = [5,4,3,2,1]#top5 streat
            #return [4, max(strat_num_)]
        return [4, make_streat_max_val_(num_uniq_)]
        
    #2pair, 1pair
    if num_max_count_ ==2:
        num_2_list_ = get_keys_from_value(num_colle_, 2)
        num_2_ = sorted(num_2_list_)[::-1]
        kikkar_2_ = sorted(get_keys_from_value(num_colle_, 1))[::-1]
        if len(num_2_list_) > 1:    
            return [2, num_2_[0], num_2_[1], kikkar_2_[0]]
        else:
            return [1, num_2_[0], kikkar_2_[0], kikkar_2_[1], kikkar_2_[2]]
    
    # gomi
    if (num_max_count_==1) & (streat_ == 0) & (flash_==0):
        kikkar_1_ = sorted(get_keys_from_value(num_colle_, 1))[::-1]
        return [0, kikkar_1_[0], kikkar_1_[1], kikkar_1_[2], kikkar_1_[3], kikkar_1_[4]]
