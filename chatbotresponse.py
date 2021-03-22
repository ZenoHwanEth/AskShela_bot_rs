import requests
url = 'https://askshelabot.herokuapp.com/webhooks/rest/webhook'
myobj = {
"message": "main menu",
"sender": "2",
}
x = requests.post(url, json = myobj)
print(x.text)