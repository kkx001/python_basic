#!usr/bin/ python
#-*- coding:utf-8 _*-
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def download(img_name,img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(download, "1.jpg", "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1419095405,742716161&fm=26&gp=0.jpg"),
        gevent.spawn(download, "2.jpg", "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3823653156,487551649&fm=26&gp=0.jpg"),
        gevent.spawn(download, "3.jpg", "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2025469379,978303773&fm=26&gp=0.jpg"),
        gevent.spawn(download, "4.jpg", "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=374051540,2986346034&fm=26&gp=0.jpg"),
        gevent.spawn(download, "5.jpg", "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2324458383,2048677465&fm=26&gp=0.jpg"),
        gevent.spawn(download, "6.jpg", "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=159845476,1433213232&fm=26&gp=0.jpg")
    ])


if __name__ == '__main__':
    main()



