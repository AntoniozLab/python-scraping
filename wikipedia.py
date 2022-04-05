from traceback import print_tb
import requests
from lxml import html

# Headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

# URL semilla
url = "https://www.wikipedia.org"

# Get HTML tree
response = requests.get(url, headers=headers)

parser = html.fromstring(response.text)

text = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
print(text)

# englishText = parser.get_element_by_id("js-link-box-en")
# print(englishText)
