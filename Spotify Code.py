#Python code for Spotify

import spotipy
import requests


#CLIENT_ID = "31d5368953f44b589bc9e1394c65e39f"
#CLIENT_SECRET = "20d026cc6015423f83b2cbd4fd03537f"
oAuthToken = "Bearer BQA-QXXAB7QTyh2f5nJgDGXdIsP8Up0VBdhiA4k1y6bHvytUoUZelBrwlfCdKB21lhurRB8pzQ9ugRyp9v778xmcB3jS4W0LRkQW7u5MXX73lHpq6lXAi1alhZfrKz6EovjopzcDbYMAthVwyoj8GqEgTAdsSUItEKDBaKmkTgxz2YwgWYCjih9rivOxUpBUk8W8b1f20mPyiq_I--OHWQNonjTKsJLUwqil7y7rCvXEXE1U_VoSDAPSMuUV4xYSx-s2JNl6"
url = "https://api.spotify.com/v1/me/player/next"
#USER = "klealcal"


headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': oAuthToken,
    }

#{'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': oAuthToken}

response = requests.post(url, headers=headers)


# data=payload, json={"Content-Type": "application/json"} , )
# data=payload, headers=headers)



#curl -X 
#"POST" 
#"https://api.spotify.com/v1/me/player/next" 
#-H "Accept: application/json" 
#-H "Content-Type: application/json" 
#-H "Authorization: Bearer BQA8dhvkKD1cwhw3qX6psckkBjseuWCCzZtzJfXMRxY-1KbRBO3HiXcj4fur1Le0z28ofyDLf__2al2kpiwhXJbzF5O4srw4zAQ7u_OvuKnWH9DigmSkOCdJmNeVDw6rNBbEcUaRpbYJ47CaZ6Teqs9KdLNUN4ry54D8YzjnbA5vn0Z8TQcC1Fn3oldcrFeLahwHHNAJ8ebJLRh6bZ-pv1J-d7ldmj5vY_Enrp8qSONWXDhOJHgSGWroVE1Zc-GvsBqSP-vb"