from urllib import request
import requests
from urllib3 import exceptions
from socket import setdefaulttimeout
from sys import exit
import argparse

# simple as piece of cake: we use requests for 'pinging' google.com with proxy

parser = argparse.ArgumentParser(description="proxy checker that works with crawler")


parser.add_argument("-f", "--file", help="input file", default="output.txt")

parser.add_argument("-o", "--output", help="output file", default="cleared_proxies.txt")

parser.add_argument("-t", "--timeout", help="timeout", default=5)

parser.add_argument("-a", "--add", help="either add to output file cleared proxies or not", default=True)


args = parser.parse_args()

def CheckProxies(proxy_list):
    setdefaulttimeout(args.timeout)

    cleared_proxies = []

    for proxy in proxy_list:
        try:
            session = requests.Session()
            session.headers['User-agent'] = 'Mozilla/5.0'
            session.max_redirects = 250
            proxy[1] = proxy[1].split('\n')[0]
            session.get('http://www.google.com', proxies={'http': 'http' + '://' + proxy[1]}, timeout=(args.timeout, 27), allow_redirects=True)

        except requests.exceptions.ConnectionError as e:
            print( 'Error!')
            continue
        except requests.exceptions.ConnectTimeout as e:
            print( 'Error,Timeout!')
            continue
        except requests.exceptions.HTTPError as e:
            print( 'HTTP ERROR!')
            continue
        except requests.exceptions.Timeout as e:
            print( 'Error! Connection Timeout!')
            continue
        except exceptions.ProxySchemeUnknown as e:
            print('ERROR unkown Proxy Scheme!')
            continue
        except requests.exceptions.TooManyRedirects as e:
            print( 'ERROR! Too many redirects!')
            continue

        cleared_proxies.append(proxy[1])
            
    try:
        if args.add:
             with open(args.output, 'r') as file:
                previous_list = file.readlines()
                if previous_list != None:
                    previous_list.extend(cleared_proxies)
                    cleared_proxies = previous_list

        with open(args.output, 'w') as file:

            file.writelines(cleared_proxies)
    except:
        print("You got some problems with output file")
        

if __name__ == "__main__":
    try:
        proxy_list = []

        with open(args.file) as file:
            strings = file.readlines()

            for string in strings:
                proxy_list.append(list(string.split('#')))

    except:
        print("You got some problems with input file")
        exit()

    CheckProxies(proxy_list)