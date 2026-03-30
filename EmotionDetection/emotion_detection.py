#Import requests library to handle HTTP requests.
import requests
#Import json library to hand JSON parsing.
import json

#Function to detect emotion of input text.
def emotion_detector(text_to_analyze):
    #URL of Watson emotion detection service.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #Create a dictonary with the text to be analyzed.
    input_text = { "raw_document": { "text": text_to_analyze } }

    #Set headers needed for emotion detection service API request.
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

    #Send a POST request to the API with the text for analysis and headers.
    response = requests.post(url, json = input_text, headers = header)

    #Parse the JSON response from the API call.
    formatted_response = json.loads(response.text)

    #Extract emotion scores.
    emotion_predictions = formatted_response['emotionPredictions'][0]
    anger_score = emotion_predictions['emotion']['anger']
    disgust_score = emotion_predictions['emotion']['disgust']
    fear_score = emotion_predictions['emotion']['fear']
    joy_score = emotion_predictions['emotion']['joy']
    sadness_score = emotion_predictions['emotion']['sadness']

    #Calculate dominant emotion.
    dominant_emotion = max(emotion_predictions['emotion'], key=emotion_predictions['emotion'].get)

    #Return a dictonary with the emotions, their scores, and the dominant emotion.
    return {'anger' : anger_score,
    'disgust' : disgust_score,
    'fear' : fear_score,
    'joy' : joy_score,
    'sadness' : sadness_score,
    'dominant_emotion' : dominant_emotion}