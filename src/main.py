from api_fetcher_spotify import fetch_artist_info_spotify

def main():
    artist_name = input("Enter artist name: ")
    artist_info = fetch_artist_info_spotify(artist_name)

    if artist_info:
        print(f"\nArtist Name: {artist_info['name']}")
        print(f"Followers: {artist_info['followers']}")
        print(f"Genres: {artist_info['genres']}")
        print(f"Image URL: {artist_info['image_url']}")
    else:
        print("Could not retrieve artist info.")
        
if __name__ == "__main__":
    main()

