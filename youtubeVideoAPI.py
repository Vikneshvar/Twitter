import google.oauth2.credentials
import os
import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import jsonpickle
import json


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():

    # # Disable OAuthlib's HTTPS verification when running locally.
    # # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # api_service_name = "youtube"
    # api_version = "v3"
    # client_secrets_file = "client_secret_google.json"

    # # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    # request = youtube.search().list(
    #     part="snippet",
    #     maxResults=25,
    #     q="surfing",
    #     type="videos"
    # )
    # response = request.execute()
    # print('response>>>>>>>>',response)

    videoIds = []
    with open("C:/Users/vikneshvar.chandraha/Dev/Twitter/youtubeRes.json",encoding="utf8") as f:
        data=json.load(f)
        video_items = data.get('items')

        for each_video in video_items:
            videoIds.append(each_video.get('id').get('videoId'))
    
    print('videoIds>>>>>>',videoIds)


if __name__ == "__main__":
    main()