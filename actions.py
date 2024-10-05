from rasa import Action
from language_detection import identificar_idioma_y_transcribir

class ActionDetectLanguage(Action):
    def name(self):
        return "action_detect_language"

    def run(self, dispatcher, tracker, domain):
        # Suponiendo que tienes el archivo de audio en una ubicación accesible
        audio_file_path = "path/to/your/booking_request.wav"
        transcripciones = identificar_idioma_y_transcribir(audio_file_path)

        for idioma, transcripcion in transcripciones.items():
            dispatcher.utter_message(text=f"{idioma}\n{transcripcion}")

        return []
