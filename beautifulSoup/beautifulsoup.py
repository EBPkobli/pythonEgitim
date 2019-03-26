import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce,'lxml')

#for paragraf in soup.find_all('p'):
#    print(paragraf.text)

#print(soup.get_text())


#pip3 install beautifulsoup4
#pip3 install urllib3

