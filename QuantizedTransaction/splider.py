import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
import re
import json

def get_one_page(url):
    try:
        re = requests.get(url)
        if re.status_code == 200:
            return re.text
        return None
    except RequestException:
        return None

def pare_one_page(html):
    pattern = re.compile("")
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'actor':item[2].strip()[3:]
        }
def writer_to_file(content):
    with open("result.txt" ,"a" ,encoding="utf-8") as f:
        #输出为中文
        f.write(json.dump(content ,ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url=url)
    it = pare_one_page(html)
    for i in it:
        print(i)

if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)
        pool = Pool()
        pool.map(main ,[i*10 for i in range(10)])