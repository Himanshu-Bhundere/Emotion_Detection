''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the different emotions and its 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions['dominant_emotion'] is None:
        return "Invalid text ! Please Try again."
    response = f"""'anger': {emotions['anger']}, 'disgust': {emotions['disgust']},
    'fear': {emotions['fear']}, 'joy': {emotions['joy']}, 'sadness': {emotions['sadness']}.
    The dominant emotion is {emotions['dominant_emotion']}."""
    return f"For the given statement, the system response is {response}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
