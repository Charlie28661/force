import requests

times = int(input("Enter a number to try guess flag ==>"))

for i in range(1, times):
    url = 'http://127.0.0.1:8600/{}'.format(i)
    response = requests.get(url).text
    print(response)