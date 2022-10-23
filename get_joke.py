import requests
import bs4

def get():
    url = 'https://anekdot.ru/random/anekdot'                        
    h   = {"User-Agent":"1"}                 
    web = requests.get(url, headers=h).text  
    bs  = bs4.BeautifulSoup(web, "lxml")                             
    result    = str(bs.find_all(class_="topicbox")[1].find(class_="text"))
    text = result.replace("<br/>","\n") 
    
    return text

print(get())
