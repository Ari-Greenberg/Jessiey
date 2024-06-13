import random
from itertools import permutations

# Rules:

# The bishops must be on opposite square colors 
# The king must be placed on a square between the two rooks 

def fischer_var(board_state):
	home_rank = 'KQBbRrNn'


	#Uses a set for the possible permutations at that position  
	home_rank_possible = {''.join(p).upper() for p in permutations(home_rank)
								if p.index('B') %2 != p.index('b') %2 
									and (p.index('R') < p.index('K') < p.index('r')
										or p.index('r') < p.index('K') < p.index('R'))}

	white_random_home = random.choice(list(home_rank_possible))
	black_random_home = random.choice(list(home_rank_possible))

	for i in range(8):
		board_state[56 + i ] = white_random_home[i]
		board_state[i] = black_random_home.lower()[i]

	
	return board_state

