import requests
from bs4 import BeautifulSoup
import re
import random

firstPage = 1
lastPage = 152

fileToPutDataIn = open("myfile.txt" + str(random.randint(1,9999999)), "x")

def filterOutHref(string):
    inHrefTag = False
    chars = ["1", "2", "3", "4", "5", "6"] #sample list to store the recent word in
    finalString = ""
    for char in string:
        del chars[0]
        chars.append(char)
        if inHrefTag == True:
            if char != "\"":
                finalString += char
            else:
                inHrefTag = False
                finalString += "\n" ## new line
        if ("".join(chars) == "href=\""):
            inHrefTag = True
            finalString += "https://www.lookmove.ch"
    return finalString
        
        

for page in range(firstPage, lastPage + 1):
    req = requests.get("https://www.lookmove.ch/de/immobilienagenturen-in-der-schweiz?pageNumber=" + str(page))

    soup = BeautifulSoup(req.content, "html.parser")

    # res = soup.findAll(class_="sc-5crxv8-0 cEqBmy" , class_="ncnw4r-0 hqjKCQ")

    res = soup.find_all(href=re.compile("/de/immobilienagenturen-in-der-schweiz/"))

    for i in res:
        # print(i.get_text())
        fileToPutDataIn.write(filterOutHref(str(i)))
