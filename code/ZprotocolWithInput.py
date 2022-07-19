import secrets
import random
import hashlib
import requests

# Stuff for defining and tracking winning
win = 0
interactive_win = 0
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



#appendfile
FileF = open('NumberReport.txt', 'w')
FileF.write(str(macro) + "\n")
FileF.write(str(win_prob) + "\n")
FileF.write(str(x) + "\n")
FileF.write(str(y) + "\n")

#Hashed 30000 times
x_hashed_array = []
y_hashed_array = []
hashed_counter = 0
x_hash = x
y_hash = y 
while hashed_counter < 30000:
#makes hash
  x_hash = str(hashlib.sha256(x_hash.encode()).hexdigest()) 
  y_hash = str(hashlib.sha256(y_hash.encode()).hexdigest())    
  #puts hash into array
  x_hashed_array.append(x_hash)
  y_hashed_array.append(y_hash)
  hashed_counter += 1

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
        current_round = randomness_round* 300 + lottery_round 
        current_total_micropayment = macro * win_prob * current_round
        current_total_macropayment = win * macro
        # if round_count == 11:
        #     round_count = round_count - 10
        round_count = round_count + 1
        print('To win this round you need to match the last three hash characters which are, ' + str(combinedHash_decimal % win_prob_denom) +
              ' to ' + str(win_decimal) + '. ' + str(round_count))
        
        #Win function 
        if win_decimal == combinedHash_decimal % win_prob_denom:
            win = win + 1
            print('Congrats that is a win right there!!!/n')
        else:
           print('You did not win this round.')

        #Interactive win check
        interactive_combined = int(x_hashed_array[current_round], 16) ^ int(y_hashed_array[current_round], 16)
        if win_decimal == interactive_combined % win_prob_denom:
            interactive_win += 1

        print('Current Lottery Round  is ' + str(current_round) + '.')
        print('Current total micropayment is worth $' + str(current_total_micropayment) + ' dollars.')
        print('Current total macropayment is worth $' + str(current_total_macropayment) + '.0 dollars.')
        print('Current total interactive macropayment is worth $' + str(interactive_win*macro) + '.0 dollars.')
        print(' ')
        FileF.write(str(current_round) + ' ' + str(current_total_micropayment) + ' ' + str(current_total_macropayment) + ' ' +
                    str(interactive_win*macro) + "\n")

        lottery_round = lottery_round + 1        
        #Hashes the previousely hashed value
        combinedHash = str(hashlib.sha256(combinedHash.encode()).hexdigest())
        
    randomness_round = randomness_round + 1
    
total_prize = macro * win
print(' ')
print('You won a total of ' + str(win) + ' times and as such...')
print('Your total prize is worth $' + str(total_prize) + '.0 over '+ str(round_count) +  ' rounds of gameplay!')
print(' ')

FileF.close()
