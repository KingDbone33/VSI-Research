import requests

server_response = requests.get('https://api.drand.sh/public/latest').json()

round_no = server_response[ 'round' ]
randomness = server_response[ 'randomness' ]

print( round_no, randomness )
