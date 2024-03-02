import requests
import json

def emotion_detector(text_to_analyse):
    emotions = {
    'anger': 'anger_score',
    'disgust': 'disgust_score',
    'fear': 'fear_score',
    'joy': 'joy_score',
    'sadness': 'sadness_score',
    'dominant_emotion': '<name of the dominant emotion>'
    }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        emotions_none = {key: None for key in emotions.keys()}
        return emotions_none
    
    emotions_data = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions_data['anger']
    disgust_score = emotions_data['disgust']
    fear_score = emotions_data['fear']
    joy_score = emotions_data['joy']
    sadness_score = emotions_data['sadness']
    dominant_emotion = max(emotions_data, key=emotions_data.get)
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    return emotions