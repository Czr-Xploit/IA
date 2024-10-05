import speech_recognition as sr

def identificar_idioma_y_transcribir(audio_file):
    idiomas = {
        'ar-SA': 'Árabe (Arabia Saudita)',
        'zh-CN': 'Chino (Mandarín, simplificado)',
        'en-GB': 'Inglés (Reino Unido)',
        'fr-FR': 'Francés (Francia)',
        'de-DE': 'Alemán (Alemania)',
        'ja-JP': 'Japonés (Japón)',
        'ko-KR': 'Coreano (Corea)',
        'ro-RO': 'Rumano (Rumania)',
        'es-ES': 'Español (España)',
        'uk-UA': 'Ucraniano (Ucrania)'
    }
    
    recognizer = sr.Recognizer()
    transcripciones = {}

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        
        for lang_code, lang_name in idiomas.items():
            try:
                text = recognizer.recognize_google(audio_data, language=lang_code)
                transcripciones[lang_name] = text
            except sr.UnknownValueError:
                continue

    return transcripciones
