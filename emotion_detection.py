# Import requests library to handle HTTP requests.
import requests

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

    #Return the response from the API.
    return response.text