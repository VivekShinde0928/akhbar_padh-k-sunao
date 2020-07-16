import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    print('\n',str)
    speak.Speak(str)

if __name__ == '__main__':
    url = ("https://newsapi.org/v2/top-headlines?country=in&apiKey=f3f91a205cf745edb5dee960b3e93055")
    response = requests.get(url).text
    # print(response)     # it is json string
    x = json.loads(response)   # it converts json string to dictionary
    # print(x)
    arts = x['articles']
    # print(arts)

    for jelly in arts:
        speak(jelly['title'])
        print(jelly['url'],end=' \n')



