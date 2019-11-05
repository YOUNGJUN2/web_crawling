import urllib.request
import re

def par(name):
    client_id = "ID"
    client_secret = "PW"
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    #url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
            response_body = response.read()
            u = response_body.decode('utf-8')
        
            p = re.search('(https\w*\D*\d*)', u)
            p = p.group(1)
    else:
            print("Error Code:" + rescode)
    
    return p

