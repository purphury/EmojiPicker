import cv2
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

def find_emoji(image_path=os.getenv('IMAGE_PATH')):
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
        face_count = len(faces)
        if face_count != 1: return {'neutral': 1} #TODO: error handle some other way
        return [face['faceAttributes']['emotion'] for face in faces][0]

    response = response.json()
    emotions = get_emotions(response)

    # Fix to not default to neutral
    if emotions['neutral'] < 0.85:
        del emotions['neutral']

    emotion = max(emotions, key=lambda key: emotions[key])

    with open(os.getenv('EMOJI_MAP_PATH')) as emoji_map_json:
        emoji_map = json.load(emoji_map_json)

    print(emotions)
    print(emotion)
    print(emoji_map[emotion])

def video_parse(stream=0):
    # Argument can be path of video (0 defaults to webcam)
    cap = cv2.VideoCapture(stream)

    frequency = 10     # higher freq, lower still image outputs
    i = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        
        if (i % frequency == 0):
            cv2.imwrite('CLASSIFY_ME.jpg',frame)
            find_emoji()
            print("Parsing emotion:\n")
        
        i += 1

    cap.release()
    cv2.destroyAllWindows()

def get_face_count():
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

    response = response.json()
    face_count = len(response)

if __name__=='__main__':
    find_emoji()
 