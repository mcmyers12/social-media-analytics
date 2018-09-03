'''
Select a YouTube channel for a product or service.
Use the data API collect information about the channel such as subscriber count and view count.
Collect data on two competitors to this product or service and provide comparison data.
'''

import os
import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def get_channel_statistics(service, file, **kwargs):
    results = service.channels().list(
        **kwargs
    ).execute()

    file.write('--' + results['items'][0]['snippet']['title'] + '\n')
    file.write('\tSubscribers: ' + results['items'][0]['statistics']['subscriberCount'] + '\n')
    file.write('\tVideos: ' + results['items'][0]['statistics']['videoCount'] + '\n')
    file.write('\tViews: ' + results['items'][0]['statistics']['viewCount'] + '\n')



if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()

    file = open('youtube-ski-channel-comparison.txt', 'w')

    file.write('YouTube channel for skis:\n')
    get_channel_statistics(service,
                           file,
                           part='snippet,contentDetails,statistics',
                           forUsername='LineSkisYo')

    file.write('\nCompetitors:\n')
    get_channel_statistics(service,
                           file,
                           part='snippet,contentDetails,statistics',
                           forUsername='ISKIK2')

    get_channel_statistics(service,
                           file,
                           part='snippet,contentDetails,statistics',
                           forUsername='rossignolchannel')