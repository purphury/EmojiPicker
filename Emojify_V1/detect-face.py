import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

# set to your own subscription key value
subscription_key = os.getenv('KEY')
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = os.getenv('API_URL')
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream',
    }
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion', #'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

with open(os.getenv('IMAGE_PATH'), 'rb') as data:
    data = data.read()
    response = requests.post(face_api_url, params=params, headers=headers, data=data)

def get_emotions(faces):
    return [face['faceAttributes']['emotion'] for face in faces][0]

response = response.json()
emotions = get_emotions(response)

# Fix to not default to neutral
if emotions['neutral'] < 0.85:
    del emotions['neutral']

emotion = max(emotions, key=lambda key: emotions[key])

with open('emojis.json') as emoji_map_json:
    emoji_map = json.load(emoji_map_json)

print(emotions)
print(emotion)
print(emoji_map[emotion])
