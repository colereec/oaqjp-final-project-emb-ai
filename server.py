#Import flask library to handle web functions.
from flask import Flask, render_template, request 
#Import emotion_detector function from EmotionDetection package for web use.
from EmotionDetection.emotion_detection import emotion_detector

#Initalize and name Flask app.
app = Flask("Emotion Detector")

#Emotion Detector app route.
@app.route("/emotionDetector") 
def emotion_analyzer(): 
    #Get the text to analyze from the request arguments.
    text_to_analyze = request.args.get('textToAnalyze')

    #Pass the text to the emotion_detector function and store the response.
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion value is None, if true, throw error (empty input). 
    if response['dominant_emotion'] is None: 
        return "Invalid text! Please try again!" 

    #Return the results of the emotion_detector in the proper format.
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(response['anger'],response['disgust'],response['fear'],response['joy'],response['sadness'],response['dominant_emotion'])

#Route for root page without arguements.
@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

#Configure app for port 5000.
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)