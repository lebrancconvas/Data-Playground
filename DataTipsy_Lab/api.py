import requests

print("Type your pokemon: ")
pokemon = input() 
pokemon_url = pokemon.lower() 
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_url  
data = requests.get(url).json() 
pokemon_abilities = data["abilities"]
pokemon_ability_list = []
for i in pokemon_abilities: 
	pokemon_ability_list.append(i["ability"]["name"])     
print(pokemon_ability_list) 

pokemon_move = data["moves"]
pokemon_move_list = []
for j in pokemon_move:
  pokemon_move_list.append(j["move"]["name"])   
print(pokemon_move_list)  