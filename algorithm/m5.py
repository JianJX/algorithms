#Climbing the Leaderboard
'''
An arcade game player wants to climb to the top of the leaderboard and track 
their ranking. The game uses Dense Ranking, so its leaderboard works like this:
The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the 
next player(s) receive the immediately following ranking number.
'''
def climbingLeaderboard(ranked, player):
    result = [ ]
    r = set(ranked)
    rank_list = []
    for n in r:
        rank_list.append(n)
    rank_list.sort(reverse=True)
    r_index = -1
    p_index = 0
    while p_index < len(player):
        if player[p_index] < rank_list[r_index]:
            result.append(len(r) + r_index + 2)
            p_index += 1
        elif abs(r_index) == len(rank_list):
            result.append(1)
            p_index += 1
        else:
            r_index -= 1
    return result