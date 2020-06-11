from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import random

app = Flask(__name__)


# access_token
def get_access_token(CLIENT_ID, CLIENT_SECRET):
    auth_response = requests.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']


# filtering the most 10 popular tracks
def max_popular(list):
    final_list = []
    for i in range(0, 10):
        max1 = 0
        for j in range(len(list)):
            if list[j]['popularity'] > max1:
                max1 = list[j]['popularity']
                max_item = list[j]
        if max1 != 0:
            list.remove(max_item);
            final_list.append(max_item)
    return final_list


# in case no proper input is putted
@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/')
def search():
    return render_template('index.html')


# user input is sent to here
@app.route('/genre', methods=['GET'])
def genre_input():
    genre = request.args.get('genre').lower()
    with open('genres.json') as file:
        data = json.load(file)
    if genre in data.keys():
        random_index = random.randint(1, len(data[genre]))
        global artist
        artist = 'artist2'
        artist = data[genre][random_index - 1]
        return redirect(url_for('.track_list', genre=genre))
    else:
        error_msg = ['Your input is not a music genre we know! Please ', 'reenter', ' your genre.']
        return render_template('error.html', error_msg=error_msg)


@app.route('/tracks/<string:genre>')
def track_list(genre):
    access_token = get_access_token(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'])
    headers = {
        'Authorization': 'Bearer {access_token}'.format(access_token=access_token)
    }
    global artist
    artist_info = requests.get(
        'https://api.spotify.com/v1/search',
        headers=headers,
        params={'q': genre + ' ' + artist, 'type': 'track', 'limit': 50})
    tracks = artist_info.json()['tracks']['items']
    tracks_popular = max_popular(tracks)
    track_items = []
    table_columns = ['Artist Name', 'Track Name', 'Album Cover', 'Preview Url']
    artist_names = []
    track_names = []
    album_covers = []
    preview_urls = []
    for track_popular in tracks_popular:
        track_artists = track_popular['artists']  # filtering according to the popularity
        #        print(any((artist.title()==track_artist['name'] for track_artist in track_artists))) #DEBUGGING
        for track_artist in track_artists:
            if track_artist['name'] == artist.title():
                artist = track_artist['name']
        artist_names.append(artist)
        track_names.append(track_popular['name'])
        album_covers.append(track_popular['album']['images'][0]['url'])
        preview_urls.append(track_popular['preview_url'])
    return render_template('tracks.html', table_columns=table_columns, artist_names=artist_names,
                           track_names=track_names, album_covers=album_covers, preview_urls=preview_urls)


if __name__ == '__main__':
    app.debug = False
    app.config.from_pyfile('spotify_api.conf')
    app.run()
