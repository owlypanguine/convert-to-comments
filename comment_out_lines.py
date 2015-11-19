#This program takes text and outputs it as a series of short comments that you can place in a .py or .R file. 
#The original content should be preserved, just re-formatted as comments limited to a specific length.

import textwrap
import urllib

def comment_out(text, line_length = 100):
    split_text = text.split("\n")

    short_lines = []
    extract_short_lines = []
    new_lines = []

    line_length = 100

    for item in split_text:
        short_lines.append(textwrap.wrap(item, line_length))
        
    for i in range(len(short_lines)):
        count = 0
        if short_lines[i] != []:
            while count < len(short_lines[i]):
                new_lines.append("#" + short_lines[i][count])
                count += 1
        else:
            new_lines.append("")
        
    commented_text = "\n".join(new_lines)

    print commented_text

text_option = raw_input('Option menu:''\n''\n''[1] I want to paste the text into the console.''\n''[2] I want to open a local file.''\n''[3] I want to connect to a web page.''\n''\n''Select an option - ')

if text_option == '1':
    text = raw_input('Enter text: ')
    try:
        comment_out(text)
    except:
        print 'Something is not right. Re-run and try the other options, or try re-formatting the text.'
elif text_option == '2':
    file_name = raw_input('Enter file name: ')
    try:
        text = open(file_name).read()
        comment_out(text)
    except:
        print 'File cannot be opened or no such file:', file_name
elif text_option == '3':
#Only grabs accessible source code and returns it as string. Does not parse code or bypass security measures.
    url = raw_input('Enter url: ')
    try:
        text = urllib.urlopen(url).read()
        comment_out(text)
    except:
        print 'Invalid url'
else:
    print "Invalid option. Re-run and enter 1, 2, or 3."