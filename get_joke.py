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

def text_map(wrapped_text):
    text = wrapped_text.split(">")
    text[0] = ""
    text = ''.join(text).split('<')
    text[-1] = ""
    text = ''.join(text)
    return text

wrapped_joke = get()
print(text_map(wrapped_joke))

