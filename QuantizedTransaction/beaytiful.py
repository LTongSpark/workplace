from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

class showHtml(object):
    @staticmethod
    def src_html():
        return "tong"
    def __init__(self):
        self.html_doc = """
                        <html><head><title>The Dormouse's story</title></head>
                        <body>
                        
                        <p class="story">Once upon a time there were three little sisters; and their names were
                        <a href="qwe" class="sister" id="link1">Elsie</a>
                        <a href="http://example.com/lacie" class="tong" id="link2">Lacie</a>
                        <a href="http://example.com/tillie" class="liu" id="link3">Tillie</a></p>
                        """
        self.show()
# soup=BeautifulSoup(html_doc, "html5lib")
# # print(soup.prettify())
# # print(soup.title.string)
# # print(soup.title.parent.name)
# # print(soup.find("a").get("class"))
# # print(soup.p["class"])
# #
# for links in soup.find_all("a"):
#     print(links.get("href"))
#
# print(soup.find(id='link1'))

# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

    def show(self):
        doc = pq(self.html_doc)
        print(self.html_doc)
        items = doc(".story a").attr.href
        items = doc(".story a.sister").text()
        return items

# soup = BeautifulSoup(str(items), "html5lib")
# for links in soup.find_all("a"):
#     print(links.get("href"))
if __name__ == '__main__':

   show = showHtml()
   show.show()
   print(show.src_html())
