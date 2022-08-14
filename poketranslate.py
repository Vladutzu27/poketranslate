import urllib.request
import urllib.error
import urllib.parse
import json
import sys
import os
import time
import datetime
import textwrap
import pyperclip
rec = 0
spaces = []
record = 0
lang = "en"
langTo = "ro"
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
print("")
print("Do you wanna translate from English to Romanian? (y/n)")
if input() == "n":
    print("Do you want to see the avalible languages? (y/n)")
    if input() == "y":
        print("Available languages:")
        print("Language Name	Language Code")
        print("Afrikaans	af")
        print("Irish	ga")
        print("Albanian	sq")
        print("Italian	it")
        print("Arabic	ar")
        print("Japanese	ja")
        print("Azerbaijani	az")
        print("Kannada	kn")
        print("Basque	eu")
        print("Korean	ko")
        print("Bengali	bn")
        print("Latin	la")
        print("Belarusian	be")
        print("Latvian	lv")
        print("Bulgarian	bg")
        print("Lithuanian	lt")
        print("Catalan	ca")
        print("Macedonian	mk")
        print("Chinese Simplified	zh-CN")
        print("Malay	ms")
        print("Chinese Traditional	zh-TW")
        print("Maltese	mt")
        print("Croatian	hr")
        print("Norwegian	no")
        print("Czech	cs")
        print("Persian	fa")
        print("Danish	da")
        print("Polish	pl")
        print("Dutch	nl")
        print("Portuguese	pt")
        print("English	en")
        print("Romanian	ro")
        print("Esperanto	eo")
        print("Russian	ru")
        print("Estonian	et")
        print("Serbian	sr")
        print("Filipino	tl")
        print("Slovak	sk")
        print("Finnish	fi")
        print("Slovenian	sl")
        print("French	fr")
        print("Spanish	es")
        print("Galician	gl")
        print("Swahili	sw")
        print("Georgian	ka")
        print("Swedish	sv")
        print("German	de")
        print("Tamil	ta")
        print("Greek	el")
        print("Telugu	te")
        print("Gujarati	gu")
        print("Thai	th")
        print("Haitian Creole	ht")
        print("Turkish	tr")
        print("Hebrew	iw")
        print("Ukrainian	uk")
        print("Hindi	hi")
        print("Urdu	ur")
        print("Hungarian	hu")
        print("Vietnamese	vi")
        print("Icelandic	is")
        print("Welsh	cy")
        print("Indonesian	id")
        print("Yiddish	yi")
    print("Then enter the language you want to translate from: (e.g. 'en').")
    lang = input()
        
    print("Enter the language you want to translate to:")
    langTo = input()

    
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
#use textwrap to wrap the text to a certain width
def wrap(string, width):
    #replace newlines with "\n"
    croco = textwrap.fill(string, width).replace("\n", "\\n")
    return croco


text = input("enter text to translate: ")
text = text.replace(" ", "%20")
text = text.replace("\n", "")
text = removePokemonFormats(text)
print("is '", wrap(putBackPokemonFormats(removeDia(translate(text, lang, langTo))), 30), "' ok?")
if input() == "y":
    #copy the text to the clipboard
    pyperclip.copy(wrap(putBackPokemonFormats(removeDia(translate(text, lang, langTo))), 30))
    print("Text copied to clipboard.")
else:
    print("then enter YOUR translation:")
    translation = input()
    translation = translation.replace(" ", "%20")
    translation = translation.replace("\n", "")
    translation = putBackPokemonFormats(translation)
    print("is '", wrap(putBackPokemonFormats(removeDia(translation)), 30), "' ok?")
    if input() == "y":
        #copy the text to the clipboard
        pyperclip.copy(wrap(putBackPokemonFormats(removeDia(translation)), 30))
        print("Text copied to clipboard.")
    else:
        print("damn youre BAD at translating.")
