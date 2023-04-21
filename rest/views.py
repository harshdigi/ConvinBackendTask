from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import os

#Setting OAUTHLIB_INSECURE_TRANSPORT
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

#This used to get the file provided by google for client id and token
GOOGLE_CREDENTIALS_FILE = "credentials.json"

#Permissions we want from user 
SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/userinfo.profile',
          'openid']

#Url to which user will be redirected when user completes signin, this should be same as specified in Google Console
REDIRECT_URL = 'http://127.0.0.1:8080/rest/v1/calendar/redirect'
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

#This function is used to provide authorization url using which user can login"
@api_view(['GET'])
def GoogleCalendarInitView(request):
    #this is used to get the user authorization url
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
    flow.redirect_uri = REDIRECT_URL

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    request.session['state'] = state

    return Response({"authorization_url": authorization_url})

#this view is used get the event list response, this is automatically called after user signin
@api_view(['GET'])
def GoogleCalendarRedirectView(request):
   
    state = request.session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        GOOGLE_CREDENTIALS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = REDIRECT_URL

   
    authorization_response = request.get_full_path()
    flow.fetch_token(authorization_response=authorization_response)


    
    credentials = flow.credentials
    request.session['credentials'] = {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

  
    if 'credentials' not in request.session:
        return redirect('v1/calendar/init')

    credentials = google.oauth2.credentials.Credentials(
        **request.session['credentials'])

    service = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

   
    calendar_list = service.calendarList().list().execute()

    
    calendar_id = calendar_list['items'][0]['id']

   
    events  = service.events().list(calendarId=calendar_id).execute()

    events_list_append = []
    if not events['items']:
        print('No data found.')
        return Response({"message": "No data found or user credentials invalid."})
    else:
        for events_list in events['items']:
            events_list_append.append(events_list)
            return Response({"events": events_list_append})
    return Response({"error": "calendar event aren't here"})

