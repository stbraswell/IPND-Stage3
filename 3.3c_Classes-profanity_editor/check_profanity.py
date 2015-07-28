import urllib

def read_text():
    quotes = open("/Users/Troy/Documents/CODE/3.3c_profanity_editor/profane_text.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("This Shit's got Curse Words!!")
    elif "false" in output:
        print("This document is tame.")
    else:
        print("I can't read this bitch to scan it")
    

read_text()
