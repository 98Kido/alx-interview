#!/usr/bin/node
import requests
import sys

def get_movie_data(movie_id):
    """Fetch movie data from Star Wars API based on movie ID."""
    # Base URL for Star Wars API
    url = f"https://swapi.dev/api/films/{movie_id}/"

    # Send request to get the movie data
    response = requests.get(url)

    # If the response status is not 200, return None (movie doesn't exist)
    if response.status_code != 200:
        print(f"Error: Movie with ID {movie_id} not found")
        return None

    return response.json()

def get_character_name(character_url):
    """Fetch character name from the given character URL."""
    # Send request to get the character data
    response = requests.get(character_url)

    # Return the character name if request is successful
    if response.status_code == 200:
        return response.json().get("name")
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: ./0-starwars_characters.js <movie_id>")
        sys.exit(1)

    # Get the movie ID from the first argument
    movie_id = sys.argv[1]

    # Get movie data from SWAPI
    movie_data = get_movie_data(movie_id)

    # If movie data is None, exit
    if movie_data is None:
        sys.exit(1)

    # Get list of character URLs from the movie data
    character_urls = movie_data.get("characters", [])

    # Print each character name
    for character_url in character_urls:
        character_name = get_character_name(character_url)
        if character_name:
            print(character_name)

if _name_ == "_main_":
    main()
