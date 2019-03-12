from bs4 import BeautifulSoup
from urllib.parse import urlparse
import http.client


class ParseReddit:
    def __init__(self, url):
        self.connecter = http.client.HTTPSConnection('www.reddit.com')
        self.url = url
        self.html = ""

    def _parse_url(self):
        result=urlparse(self.url)
        return result.path
    
    def _parse_html(self):
        if self.html:
            return BeautifulSoup(self.html, 'html.parser')
        else:
            return None

    def output(self):
        self.connecter.request("GET", self._parse_url())
        response = self.connecter.getresponse()
        self.html = response.read()

        soup = self._parse_html()
        if soup:
            t = soup.find("div", class_="xvda30-0 camSYk")
            print("Date:", t.find_next_sibling("a").text)
            print("Author:", t.text)
            print("Topic:", soup.find("h2").text)




if __name__ == "__main__":
    t = ParseReddit("https://www.reddit.com/r/worldnews/comments/azxg1s/russia_bans_disrespect_of_government/")
    t.output()