import os
import time

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = r"C:\Users\manik\Downloads\client_secret_72424185993-r3f4e2nc2sfehrp288sk5cmu4rskji6m.apps.googleusercontent.com.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

def addToPlaylist(video_id):
    """Add a video to a specified playlist

    Parameters
    ----------
    video_id : string
        The target video id to be added to the playlist.
    
    playlist_id : string
        The playlist to add the video to.
    """
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": "PLPE3jYWp3YNKZZ0Ry4W-Z02SBC3ulY-kF",
            "resourceId": {
              "kind": "youtube#video",
              "videoId": video_id
            }
          }
        }
    )
    response = request.execute()

    print(response)

def search(topic):
    """Search the most relevant result of a certain topic

    Parameters
    ----------
    topic : string
        The topic that will be searched up
    """
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=topic,
        type="youtube#video",
        order='relevance'
    )
    response = request.execute()

    id = response['items'][0]['id']['videoId']

    return id

def main():

    input = open("input.txt", "r")

    for line in input.readlines():
        print(line)
        id = search(line)
        addToPlaylist(id)
        time.sleep(0.5)
    
    input.close()

if __name__ == "__main__":
    main()

