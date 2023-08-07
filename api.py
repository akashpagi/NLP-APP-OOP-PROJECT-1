import paralleldots

class API:
    
    def __init__(self) -> None:
        # Setting your API key
        paralleldots.set_api_key('pBoHKHLKuiVnxdnRAjCiiJk09ckBG0vyhExSJIz3RqQ')
    
    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response
    
    def name_entity_recognition(self, text):
        ner_response = paralleldots.ner(text)
        return ner_response
    
    def emotion_analysis(self, text):
        emotion_response = paralleldots.emotion(text)
        return emotion_response