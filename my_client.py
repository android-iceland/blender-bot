app_url="https://58822.gradio.app/"
blender_bot_app_url="https://25058.gradio.app/"
from urllib.request import urlopen
import urllib
import json
from cryptography.fernet import Fernet
from rich.console import Console
console = Console()
secrect_key=b'jNi5mVP1u_y3ffNmh4NZMCqv3zWSWrr1SWv3VNeD0BU='
def encrypt_chat(msg):
  a = Fernet(secrect_key)
  encode_chat = a.encrypt(msg.encode())
  encode_chat=encode_chat.decode("utf-8")
  return encode_chat 

def decrypt_chat(endoce_msg):
  b = Fernet(secrect_key)
  endoce_msg=endoce_msg.encode("utf-8")
  decoded_chat = b.decrypt(endoce_msg).decode()
  return decoded_chat


def blender_bot(msg,output_lang):
    msg=encrypt_chat(msg)
    r = requests.post(url=blender_bot_app_url+"api/predict/",
    json={"data":
    [msg]})
    reply_data=r.json()
    english_chat=decrypt_chat(reply_data["data"][0])
    # print(f"Bot: {english_chat}")
    console.print(f"[bold green]BOT:[/bold green] {english_chat}\n",style="yellow")
    SpeakText(english_chat)
    return english_chat


from time import sleep
import pyglet
import os


import requests
import base64

file_name="temp.wav"
def SpeakText(mytext):
    r = requests.post(url=app_url+"api/predict/",
    json={"data":
    [mytext]})
    audio_data=r.json()
    raw_data=audio_data["data"][0].replace("data:audio/wav;base64,","")
    wav_file = open(file_name, "wb")
    decode_string = base64.b64decode(raw_data)
    wav_file.write(decode_string)
    music = pyglet.media.load(file_name, streaming=False)
    music.play()
    sleep(music.duration)
    # os.remove(file_name) 
