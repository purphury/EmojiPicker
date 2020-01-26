Creating the world's first emotionally lossless compression algorithm

Execution Instructions:
Run main.py to execute in terminal


## Inspiration
We were really impressed with facial recognition technologies and wanted to see how we could use it to improve lives. When we found the accessibility challenge, we decided to try and use facial emotion recognition to see if we can help people transmit their emotions. 
## What it does
Emojibility unlocks the full capabilities of written communication without the need to interact with a keyboard. Fully hands-free, Emojibility enables seamless communication, regardless of fine motor skills. Not only does Emojibility transcribe audio into typed messages, we use the world's first emotionally lossless compression algorithm to convert human emotion into emoji. Emojibility can also be used to detect emotion in pictures for those who may have difficulty discerning emotions.
## How I built it
We use OpenCV to take a live video/audio stream and send it to Google's Speech API to transcribe the audio, and Microsoft Azure's Face API to detect emotions. We also used the number of faces in the picture to detect when the user looks away, which we used as the input to switch from emoji mode to transcription mode.
## Challenges I ran into
There were issues with credentials on Google Cloud Platform to enable speech transcription, additionally, gaining an endpoint and key were tricky with Azure's APIs. We also had some work to use a live feed through locals files versus using a hosted image URL.
## Accomplishments that I'm proud of
We were able to stitch together some libraries and several APIs into a cohesive product that might actually impact the lives of those who are not able to or simply don't feel like using a keyboard to transmit emotive messages.
## What I learned
We learned about how to use APIs, delving into documentation, andusing OpenCV to work on live audiovisual feeds.
## What's next for Emojibility
We would like to integrate this into the keyboard of major smartphones like Apple iPhones and Android phones, so that Emojibility can be used with any existing messaging platform like Discord or iMessages.