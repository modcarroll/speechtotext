"""
Author: Morgan Carroll, IBM
Description: Combines the "transcript" fields from the JSON output of a Watson Text-to-Speech request, 'input-text.txt',
and prints it to a text file, "Text-to-Speech-Output.txt"
"""

import json

# Creates a new text file to save transcribed text
f = open('Text-to-Speech-Output.txt','w')

# Opens file with text-to-speech data to be transcribed
with open('input-text.txt', 'rb') as fin:
    content = json.load(fin)

finalText = ''
for someThing in content['results']:
	finalText += someThing['alternatives'][0]['transcript']

f.write(finalText)
f.close()
