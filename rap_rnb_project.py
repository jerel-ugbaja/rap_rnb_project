#Rap & R&B Song Recommender Project

# Function to get user's favourite genre
def get_genre():
    valid_genres = ['rap', 'r&b', 'neo soul', 'indie', 'afrobeats']
    while True:
        genre = input("enter your favourite genre(rap, r&b, neo soul, indie, afrobeats): ").lower()
        if genre in valid_genres:
            print(f"you selected: {genre.title()}")
            return genre
        else:
            print("Invalid genre, please try again.")

# Function to get user's 3 favourite artists
def get_artists():
    artists = []
    while len(artists) < 3:
        artist = input(f"enter your favourite artists {len(artists)+1}: ").title()
        if artist.isalpha() or " " in artist: # Simple validation
            artists.append(artist)
        else: 
            print("invalid artist name, please try again.")
    return artists

# Function to recommend songs
def recommend_songs (genre, artists):
    # recommendations based on genre
    song_db = {
        'rap': ['Freddie Gibbs - Soul Right', 'Kendrick Lamar - ADHD', 'Drake - Weston Road Flows', 'Westside Gunn - Elizabeth', 'Gunna - 200FORLUNCH'],
        'r&b': ['SZA - No More Hiding', 'Brent Faiyaz - GHETTO GASTBY', 'Frank Ocean - Seigfried', 'Jhene Aiko - Spotless Mind', 'Daniel Caesar - Valentina'],
        'neo soul': ['Erykah Badu - Orange Moon', 'Cleo Sol - Desire', 'Anderson Paak - Come Home', 'Outkast - Prototype', 'Sade - No Ordinary Love'],
        'indie': ['Steve Lacy - Basement Jack', 'Tame Impala - Past Life', 'Faye Webster - I Know You', 'Arctic Monkeys - 505', 'N.E.R.D - Run To The Sun'],
        'afrobeats': ['Burna Boy - Secret', 'Wizkid - Ojuelegba', 'Black Sherif - Run', 'Tiwa Savage - You4Me', 'ODUMODUBLVCK - DECLAN RICE']  
    }

    print("\n Here are 5 song recommendations for you:\n")
    songs = song_db[genre]
    for idx, song in enumerate(songs, start=1):
         print(f"{idx}. {song}")

# Main program
print("Welcome to the Rap & R&B Song Recommender!")

name = input("Enter your name: ").title()
print(f"Hello, {name}!")

genre = get_genre()
artists = get_artists()

print("\nYour favourite artists are:")
for artist in artists:
    print(f"- {artist} ({len(artist)} letters)")

recommend_songs(genre, artists)

print("\nEnjoy your listening session!")