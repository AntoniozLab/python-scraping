from traceback import print_tb
import requests
from lxml import html

# Headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

# URL target
url = "https://github.com/login"

session = requests.Session()

# Get auth token
tokenRequest = session.get(url, headers=headers)
tokenHTML = html.fromstring(tokenRequest.text)
authToken = tokenHTML.xpath("//input[@name='authenticity_token']/@value")[0]

# Start session with credentials
login_url = "https://github.com/session"
login_data = {
    "login": "jcahuana",
    "password": open("./password.txt").readline().strip(),
    "commit": "Sign in",
    "authenticity_token": authToken
}

session.post(login_url, data=login_data, headers=headers)

# Get private data
respositories_url = "https://github.com/jcahuana?tab=repositories"
repoRequest = session.get(respositories_url, headers=headers)
repoHTML = html.fromstring(repoRequest.text)
repoNames = repoHTML.xpath("//h3[@class='wb-break-all']/a/text()")

# Print repo names
for repoName in repoNames:
    print(repoName)
