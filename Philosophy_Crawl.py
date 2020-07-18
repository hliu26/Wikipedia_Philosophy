from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import urllib

from PIL import Image
from io import BytesIO


class Page:
    
    wiki = 'https://en.wikipedia.org'
    
    end = "https://en.wikipedia.org/wiki/Philosophy"
    
    branches = 0
    
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(urlopen(self.url))
        self.title = self.soup.title.string
        
        try:
            self.image = Image.open(BytesIO(urlopen(self.soup.find_all("meta")[-1]["content"]).read()))
        except:
            self.image = None
            
    def remove_table(self):
        self.soup.find("table").extract()
    
    def remove_parentheses(self, body_text):
        """converts body of text from BeautifulSoup Object into String
        then takes the string and filters out all parenthesized strings/ links
        and returns the filtered obj reconverted into BeautifulSoup obj
        """
        
        out = []
        paren = 0
        italic =0

        for i in str(body_text).split(" "):
            #print(i)
            if "(" in i :
                if "href" not in i:
                    for symbol in i:
                        if symbol == "(":
                            paren += 1
                else:
                    if paren != 0:
                        paren += 1
        
            if ")" in i:
                if "href" not in i:
                    for symbol in i:
                        if symbol == ")":
                            paren -= 1
                else:
                    if paren != 0:
                        paren -= 1
                
        
            if "<i>" in i or "<i" in i:
                if "<img" not in i:
                    italic += 1
        
            if "</i>" in i:
                if italic == 0:
                    pass
                else:
                    italic -= 1
        
            #print(paren)    
            #print(italic)
            if paren == 0 and italic == 0:
                if ")" in i:
                    if "href" in i :
                        out.append(i)
                else:
                    out.append(i)

        return BeautifulSoup(' '.join(out))
            
        
    def all_links(self):
        """check_next takes a beautifulsoup object.
        returns all links found in bodies of text (tags "p")
        the result is a list wiki links in each body of text
        """
        self.remove_table()
        
        res = []
        for tags in self.soup.find("body").find_all("p"):
            tags = self.remove_parentheses(tags)
            
            if (any(s in str(tags).split(' ')[0] for s in ["<p>\n<span", "<p><span"]) 
                    or "text-align" in str(tags)):
                continue
            
            if tags.find("a") == None:
                pass
            else:
                for links in tags.find_all('a'):
                    try:
                        if "/wiki/" in links["href"]:
                            res.append(links["href"])
                    except:
                        pass
        return res
    
    

    def get_nexturl(self):
        for link in self.all_links():
            return self.wiki + link
                
    
    def crawl(self):
        """Crawls from current wiki page to next.
        
        Should check for cycles and break if one occurs 
        """
        
        #should Page class be nodes with .next (pointers?)
        
        visited = []
        self.branches = 0
        
        print(self.title + ":", self.url)
        visited.append(self.url)
        
        next_link = self.get_nexturl()
        
        while next_link != self.end:
            self.branches += 1
            
            temp_page = Page(next_link)
            visited.append(next_link)
            
            print(temp_page.title + ":", temp_page.url)
            
            next_link = temp_page.get_nexturl()
            
            if next_link in visited:
                raise Exception("Cycle was discovered. "+ next_link)
            
        self.branches += 1
        print("\033[1m Philosophy Reached! \033[0m", self.wiki+next_link)
    

    
