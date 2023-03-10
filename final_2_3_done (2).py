# -*- coding: utf-8 -*-
"""final 2/3 done.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vxApPn_W3LtiIcyZ--if2ZpwkmJWQpfI
"""

## speech to text - audio FILE input 

# Imports the Google Cloud client library
from google.cloud import speech


# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = input("enter audio file")

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))


# Import the summarizer
from sumy.summarizers.luhn import LuhnSummarizer
ch = 50
## input
original_text = (result.alternatives[0].transcript)
date = input("Enter Date:")
p = input("Enter Patient's Name Here :")
d = input("Enter Doctors Name Here :")
s = input("How many lines of summary?")
# Creating the parser

from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
parser=PlaintextParser.from_string(original_text,Tokenizer('english'))

#  Creating the summarizer
luhn_summarizer=LuhnSummarizer()
luhn_summary=luhn_summarizer(parser.document,sentences_count=s)

# Printing the summary
for sentence in luhn_summary:
  print(sentence)


# Custom class to overwrite the header and footer methods
## text to pdf output  
from fpdf import FPDF
u = str(sentence)

class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        self.set_font('Arial', '', 12)
        pdf.set_fill_color(r= 0, g= 242, b = 247)
        self.cell(0, 10, 'Doctors Advice', 1, 1, 'C', fill=True)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        pdf.set_fill_color(r= 0, g= 242, b = 247)
        self.cell(0, 10, '---end of page---', 1, 0, 'C', fill=True)
pdf = PDF() # Instance of custom class
pdf.add_page()
pdf.set_font('Arial', 'B', 24)
pdf.cell(w=0, h=20, txt="Doctors Advice", ln=1)
pdf.set_font('Arial', '', 16)
pdf.cell(w=20, h=ch, txt="Date: ", ln=0)
pdf.cell(w=30, h=ch, txt= date , ln=1)
pdf.cell(w=40, h=ch, txt="Doctor Name: ", ln=0)
pdf.cell(w=30, h=ch, txt= d, ln=1)
pdf.cell(w=40, h=ch, txt="Patient Name: ", ln=0)
pdf.cell(w=30, h=ch, txt= p, ln=1)
pdf.ln(ch)
pdf.multi_cell(w=0, h=5, txt=u)
pdf.output(f'./doctors_advice.pdf', 'F')

pip install --upgrade google-cloud-speech