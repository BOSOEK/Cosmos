# 이미지 html 파일에서 이미지 주소 크롤링
# 53페이지 까지 다함 54페이지 부터 시작
from bs4 import BeautifulSoup
import urllib.request

count = 0
for k in range(54, 190):
    data = open('source/' + str(k) +'.html', encoding='UTF-8')

    soup = BeautifulSoup(data.read(), 'html.parser')

    link = []

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    for meta in soup.body.find_all('meta'):
        link.append(meta.get('content'))

    for i in link:
        if i[-1] == 'g' and i[-2] == 'p' and i[-3] == 'j' and i[-4] == '.' or i[-1] == 'g' and i[-2] == 'n' and i[-3] == 'p' and i[-4] == '.' :
            #print(i)
            count += 1
            save = './data/' + str(count) + '.jpg'
            urllib.request.urlretrieve(i, save)
    print(k)
