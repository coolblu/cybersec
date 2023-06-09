import urllib.request, urllib.error, urllib.parse

link = "http://www.chiquitooenterprise.com/password"
# Missing a whole chunk of code here!
revString = urllib.request.urlopen(link)
revString = revString.read()
revString = revString.decode('utf-8') [: :-1]


answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib.request.urlopen(answer)
response = response.read()
print(response.decode('utf-8'))
