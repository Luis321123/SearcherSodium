import speech_recognition as sr
import webbrowser
import re
import os

def ejecutar_comando(comando):
    comando = comando.lower()
        
    if "busca en youtube" in comando:
        busqueda = comando.split("youtube")[-1].strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={busqueda}&sp=EgIQAQ%3D%3D")
    
    elif "busca en google" in comando:
        busqueda = comando.split("google")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={busqueda}")
    
    elif "abre" in comando:
        pagina = comando.split("abre")[-1].strip()
        if "youtube" in pagina:
            webbrowser.open("https://www.youtube.com")
        elif "facebook" in pagina:
            webbrowser.open("https://www.facebook.com/")
        
        elif "abre pinterest" in comando:
            webbrowser.open("https://www.pinterest.com/")
        elif "abre instagram" in comando:
            webbrowser.open("https://www.instagram.com/")
    
    else:
        webbrowser.open(f"https://www.google.com/search?q={comando}")
    

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Di tu comando (ej: 'busca')...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)
try:
    texto = recognizer.recognize_google(audio, language="es-ES")
    print(f"Comando reconocido: {texto}")
    ejecutar_comando(texto)
except sr.UnknownValueError:
    print("No se entendió el audio.")
except sr.RequestError:
    print("Error en la api e de voz.")