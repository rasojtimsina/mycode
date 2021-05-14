#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget

def main():
    name = input("Please enter the pokemon name you want to search for: ")
    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    picurl = pokeapi["sprites"]["front_default"]
    wget.download(picurl, "/home/student/static/")
    gamecount = len(pokeapi["game_indices"])

    print(f"{name}, has been in {gamecount} games")

    print("Moves:", [item['move']['name'] for item in pokeapi['moves']])

    #print(pokeapi)

main()

