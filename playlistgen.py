import google.auth
import os
import google.auth.transport.requests
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\manik\Downloads\playlist-generator-378301-2f08825762f9.json"
# Set up the API client
#credentials, project = google.auth.default()
#api_key = 'AIzaSyCoJCdcyut7evw2jEqjzfCWR2Sbrw1HzwQ'
#youtube = build('youtube', 'v3', credentials=credentials)

credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
if credentials is None or credentials.expired:
    credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

youtube = build('youtube', 'v3', credentials=credentials)  

# Define the playlist parameters
playlist_params = {
    'snippet': {
        'title': 'My Awesome Playlist',
        'description': 'A playlist of programming tutorials.'
    },
    'status': {
        'privacyStatus': 'public'
    }
}

# Create the playlist
playlist_response = youtube.playlists().insert(
    part='snippet,status',
    body=playlist_params
).execute()

playlist_id = playlist_response['id']
print(f'Playlist created with ID: {playlist_id}')

# Add videos to the playlist
video_ids = ['VIDEO_ID_1', 'VIDEO_ID_2', 'VIDEO_ID_3']

for video_id in video_ids:
    playlist_item_params = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id
            }
        }
    }

    playlist_item_response = youtube.playlistItems().insert(
        part='snippet',
        body=playlist_item_params
    ).execute()

    print(f'Added video with ID {video_id} to playlist with ID {playlist_id}')