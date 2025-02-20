import requests

from send_email import send_email

api_key = "4f5ac98be0374421b39f56cb1fafd850"

url = ("https://newsapi.org/v2/everything?q=apple&from="
       "2025-02-19&to=2025-02-19&sortBy=popularity&apiKey="
       "4f5ac98be0374421b39f56cb1fafd850&"
       "language=en")

req = requests.get(url)
content = req.json()
articles = content["articles"]

body = ""
for article in articles:
    description = article["description"]
    print(article["description"])
    body += article["title"] + 2 *"\n" + article["url"] +"\n" + description
    body = body.encode("utf-8")
send_email(body)

