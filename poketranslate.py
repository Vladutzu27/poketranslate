import urllib.request
import urllib.error
import urllib.parse
import json
import sys
import os
import time
import datetime
rec = 0
spaces = []
record = 0
print("                                  ,'\ ")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("                _                       _       _       ")
print("               | |                     | |     | |      ")
print("               | |_ _ __ __ _ _ __  ___| | __ _| |_ ___ ")
print("               | __|  __/ _  |  _ \/ __| |/ _  | __/ _ \ ")
print("               | |_| | | (_| | | | \__ \ | (_| | ||  __/")
print("                \__|_|  \__,_|_| |_|___/_|\__,_|\__\___|")
print("")
print("                                 made by Vladuztu27 v0.1")

def translate(text, lang_from, lang_to):
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=%s&tl=%s&dt=t&q=%s' % (lang_from, lang_to, text)
    result = urllib.request.urlopen(url).read()
    result = json.loads(result.decode('utf-8-sig'))
    return result[0][0][0]
def removeDia(romanianText):
    romanianText = romanianText.replace("ă", "a")
    romanianText = romanianText.replace("â", "a")
    romanianText = romanianText.replace("î", "i")
    romanianText = romanianText.replace("ș", "s")
    romanianText = romanianText.replace("ț", "t")
    romanianText = romanianText.replace("ş", "s")
    romanianText = romanianText.replace("ţ", "t")
    return romanianText
def removePokemonFormats(string):
    string = string.replace("\v0200\x0001\x0000", "[dk]")
    string = string.replace("\v0101ぁ\x0000\x0000", "Tom")
    string = string.replace("\v0103ぁ\x0000\x0000", "Paul")
    return string
def putBackPokemonFormats(string):
    string = string.replace("[dk]", "\v0200\x0001\x0000")
    string = string.replace("Tom", "\v0101ぁ\x0000\x0000")
    string = string.replace("Paul", "\v0103ぁ\x0000\x0000")
    return string
def scanForBreaks(string):
    spaces.clear()
    for i in range(0, len(string)):
        if string[i] == " ":
            spaces.append(i)
    for i in range(0, len(spaces)):
        record = 0
        if spaces[i] <= 30 & spaces[i] > record:
            record = spaces[i]
    return record




text = input("enter text to translate: ")
lang_from = input("enter language to translate from: ")
lang_to = input("enter language to translate to: ")
text = text.replace(" ", "%20")
text = text.replace("\n", "")
text = removePokemonFormats(text)
print(putBackPokemonFormats(removeDia(translate(text, lang_from, lang_to))))
