import os
import speech_recognition as sr
from my_client import blender_bot
from rich.console import Console

console = Console()

input_lang = 'en'
output_lang='en'

from googletrans import Translator
translator = Translator()

def trans_bot(mytext):
    result = translator.translate(mytext,dest="en")
    return str(result.text)                                  
r = sr.Recognizer()

# print("Start talking: \n")
console.print("Start talking: \n",style="bold red")
while(1):	
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2,language=input_lang)
            MyText = MyText.lower()
            console.print(f"[bold blue]YOU:[/bold blue] {MyText}",style="yellow")
            # print("You: "+MyText)
            trans_text_bot=trans_bot(MyText)
            if len(MyText)>=2:
                blender_bot(trans_text_bot,output_lang)
            
  
            
            
    except sr.RequestError as e:
        pass
        
    except sr.UnknownValueError:
        pass
       
