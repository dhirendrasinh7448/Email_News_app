import requests

api_key = "4f5ac98be0374421b39f56cb1fafd850"

url = ("https://newsapi.org/v2/everything?q=apple&from="
       "2025-02-19&to=2025-02-19&sortBy=popularity&apiKey="
       "4f5ac98be0374421b39f56cb1fafd850")

req = requests.get(url)
content = req.json()
articles = content["articles"]

for article in articles:
    print(article["description"])

