import secrets
import random
import hashlib
import requests

# Stuff for defining and tracking winning
win = 0
round_count = 0

# Definition of x, y, and b
x = secrets.token_hex(16)
y = secrets.token_hex(16)

# Obtain randomness values
server_response = requests.get('https://api.drand.sh/public/latest').json()
cur_round = server_response[ 'round' ]
randomness = []
for i in range( 100 ):
    server_response = requests.get( 'https://api.drand.sh/public/' + str( cur_round - i ) ).json()
    randomness.append( server_response[ 'randomness' ] )

# Start
macro = int(input('What is your macropayment for your transaction today? '))
win_prob = float(input('What is your desired win probability today, .1, .01, or .001? '))

win_prob_denom = int( 1 / win_prob )
win_decimal = random.randint(0, win_prob_denom - 1 )
micropayment_per_lottery = macro * win_prob

#The loop
randomness_round = 0
while randomness_round < 100:
    lottery_round = 0
    cur_randomness = randomness[ randomness_round ]

    #Defining, combining, and hashing strings x, y, and randomness
    B = x + y + cur_randomness
    combinedHash = str(hashlib.sha256(B.encode()).hexdigest())

    #Loop
    while lottery_round < 300:
        combinedHash_decimal = int(combinedHash, 16)

        round_count = round_count + 1
        print('To win this round you need to match the last three hash characters which are, ' + str(combinedHash_decimal % win_prob_denom) +
              ' to ' + str(win_decimal) + '. ' + str(round_count))
        
        #Win function 
        if win_decimal == combinedHash_decimal % win_prob_denom:
            win = win + 1
        lottery_round = lottery_round + 1        
        #Hashes the previousely hashed value
        combinedHash = str(hashlib.sha256(combinedHash.encode()).hexdigest())
    randomness_round = randomness_round + 1
    
total_prize = macro * win
print('Good job!')
print('You won a total of ' + str(win) + ' times and as such...')
print('Your total prize is worth $' + str(total_prize) + ' over '+ str(round_count) +  ' rounds of gameplay!')
