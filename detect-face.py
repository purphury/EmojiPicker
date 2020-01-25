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
image_url = os.getenv('IMAGE_URL')
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion', #'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})

def get_emotions(faces):
    return [face['faceAttributes']['emotion'] for face in faces][0]

response = response.json()
emotions = get_emotions(response)
emotion = max(emotions, key=lambda key: emotions[key])

with open('emojis.json') as emoji_map_json:
    emoji_map = json.load(emoji_map_json)

print(emotions)
print(emotion)
print(emoji_map[emotion])
