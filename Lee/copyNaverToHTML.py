import urllib.request

if __name__ == "__main__":

    print("Hello, World!!")
    req = urllib.request.Request("http://www.naver.com");

    data = urllib.request.urlopen(req).read()

    print(data)


    f = open("./response_basic.html", "wb")

    f.write(data)
    f.close()


