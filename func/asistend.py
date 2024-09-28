import speech_recognition as sr
import webbrowser
import pyttsx3


def talk():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    mic = sr.Microphone()
    with mic as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es")
        print(f"Has dicho: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))
        return ""


text = talk()
if "amazon" in text:
    engine = pyttsx3.init()
    engine.say("¿Qué quieres comprar en Amazon?")
    engine.runAndWait()

    text = talk()
    webbrowser.open(f"https://www.amazon.com/s?k={text}")
elif "ebbay" in text:
    engine = pyttsx3.init()
    engine.say("¿Qué quieres comprar en ebbay?")
    engine.runAndWait()

    text = talk()
    webbrowser.open(
        f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw={text}")
elif "mercado libre" in text:
    engine = pyttsx3.init()
    engine.say("¿Qué quieres comprar en mercado libre?")
    engine.runAndWait()

    text = talk()
    webbrowser.open(f"https://listado.mercadolibre.com.co/{text}")
elif "youtube" in text:
    engine = pyttsx3.init()
    engine.say("¿Qué quieres buscar en youtube ?")
    engine.runAndWait()

    text = talk()
    webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
elif "que es" or " " in text:
    engine = pyttsx3.init()
    engine.say("¿por favor indicame lo que quieres buscar ?")
    engine.runAndWait()

    text = talk()
    webbrowser.open(f"https://www.google.com/search?q={text}")
