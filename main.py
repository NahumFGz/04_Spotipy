import pandas as pd

creds = pd.read_json('./creds.json', lines=True)
client = creds['client_id'][0]
secret = creds['client_secret'][0]

def main():   
    import spotipy 
    from spotipy.oauth2 import SpotifyClientCredentials
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client,client_secret=secret))
    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
    

if __name__ == '__main__':
    main()
    