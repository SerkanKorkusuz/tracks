# tracks

This web application server accepts a music genre type as an input and then picks a random artist associated to that
genre from " genres.json". Later, it filters the most popular 10 tracks (songs) of that artist from the first 50 tracks
obtained from ​ Spotify Search API​.

## Prerequisites

- [Installing Python 3](https://www.python.org/downloads/)
- Getting a ``CLIENT_ID`` and a ``CLIENT_SECRET`` from [Spotify Client Credentials Flow](https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow)
- Open the file ``spotify_api.conf`` and assign your ``CLIENT_ID`` and ``CLIENT_SECRET``.

## Installing the dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r requirements.txt
```
## Starting the app
Run the command:
```bash
python app.py
```
Go to [127.0.0.1:5000](http://127.0.0.1:5000/)
## TODOs

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contact
Pull requests are welcome. You can also email to korkusuzs18@itu.edu.tr

