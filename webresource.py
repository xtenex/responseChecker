#!/usr/bin/env python3

# This is just an excercie that I saw on elaearnSecurity eJPT but I went far away of the excercise adding an https connection to verify if a resource exist
# on port 80 or 443
# I think I have to add a way to check on both ports even if the 80 is responding with a 200 

import http.client, sys

def main():
    try:
        conn = http.client.HTTPConnection(sys.argv[1], http.client.HTTP_PORT, timeout=5)
        conn.request('GET','/')
        res = conn.getresponse()
        if res.status != 200:
            print(f'Host: {sys.argv[1]} has nothing on port: {http.client.HTTP_PORT}\nStatus: {res.status}\nReason: {res.reason}\nLooking on port: {http.client.HTTPS_PORT}')
            res.close()
            con = http.client.HTTPSConnection(sys.argv[1], http.client.HTTPS_PORT, timeout=5)
            con.request('GET', '/')
            r = con.getresponse()
               
            if r.status != 200:
                print(f'That path does not exist\nStatus: {r.status}\nReason: {r.reason}')
                r.close()
            else:
                print(f'Status: {r.status}\nReason: {r.reason}')
                r.close()
    
    except (IndexError, ConnectionRefusedError):
        print('connection refused')
        res.close()


if __name__ == '__main__':
    main()
