import pyttsx3
import PyPDF2
from gtts import gTTS
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
for num in range(0,pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    player.setProperty('voice', en_voice_id)
    rate = player.getProperty('rate')
    player.setProperty('rate', rate-30)
    player.say(text)
    player.runAndWait()