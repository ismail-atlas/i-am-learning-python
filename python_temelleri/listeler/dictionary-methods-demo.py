'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1

players = {
    '1': 
        {
            'name': 'cristiano ronaldo', 'yearofbirth': '1985', 'nationality': 'Portugal', 'current_team': 'Portugal', 'history': 'Juventus,Real Madrid,Portugal'
        }, 
    '2': 
        {
            'name': 'Lionel Messi', 'yearofbirth': '1987', 'nationality': 'Argentina', 'current_team': 'Barcelona', 'history': 'Barcelona,Argentina,Portugal'
        }
    }
          

"""
id = input("id: ")
name = input("ad: ")
yearofbirth = input("year of birth: ")
nationality = input("nationality: ")
current_team = input("current team: ")
history = input("history: ")

players.update({
    id: {
        "name":name,
        "yearofbirth":yearofbirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history
    }
})

id = input("id: ")
name = input("ad: ")
yearofbirth = input("year of birth: ")
nationality = input("nationality: ")
current_team = input("current team: ")
history = input("history: ")

players.update({
    id: {
        "name":name,
        "yearofbirth":yearofbirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history
    }
})
"""

# print(players)

# 2
"""
id = input("aramak istediğiniz oyuncu id: ")
player = players.get(id)
print(f"name: {player.get('name')}, yearofbirth: {player.get('yearofbirth')}, nationality: {player.get('nationality')}, current team: {player.get('current_team')}, history: {player.get('history')}")
"""

# 3
id = input("silmek istediğiniz oyuncu id: ")
players.pop(id)

print(players)