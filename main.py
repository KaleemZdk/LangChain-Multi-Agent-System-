from src.tools.tools import web_search , scrape_url

# output = web_search("Capital of kazakistan")

# print(output)

result = scrape_url.invoke("https://en.wikipedia.org/wiki/Kazakhstan")
print(result)