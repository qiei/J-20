import sys
import urllib
import time

url = input("网址:")
txt = open(r"/data/data/com.termux/files/home/J-20/J.txt","r")
open_url = []
all_url = []
def search_url(url,txt):
    with open(r"/data/data/com.termux/files/home/J-20/J.txt""r") as f :
        for each in f:
            each = each.replace('\n','')
            urllist = url+each
            all_url.append(urllist)
            print("搜索:"+urllist+'\n')
            try:
                req = urllib.urlopen(urllist)
                if req.getcode() == 200:
                    open_url.append(urllist)
                if req.getcode() == 301:
                    open_url.append(urllib)
            except:
                pass
def main():
    search_url(url,txt)
    if open_url:
        print("后台:")
        for each in open_url:
            print(">"+each)
    else:
        print("搜索不到后台地址!")
    if if __name__ == "__main__":
        mian()