import argparse
from os import error
from sys import exit
from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options


parser = argparse.ArgumentParser(description="a crawler program which can be used for crawling various proxy list sites")

parser.add_argument("-s", "--site", help="a site which we wanna to crawl (you can set only what in proxylists.txt)", default="https://spys.one/en/")

parser.add_argument("-f", "--file", help="set an output file", default="output.txt")

parser.add_argument("-p", "--proxy_lists", help="set a file which contains accepted sites", default="proxylists.txt")

parser.add_argument("-a", "--anonymous", help="use only anonymous proxies", default=True)
args = parser.parse_args()

mode = 0

options = Options()
options.add_argument('--headless')


def main():
    global mode

    driver = webdriver.Firefox(options=options)
    driver.get(args.site)

    useful_info = []
    if mode == 0:
        list_proxies = driver.find_elements_by_class_name('spy1xx')

        print("All info from the site:")
        for proxy_element in list_proxies[12:]:
            compounds = proxy_element.find_elements_by_tag_name('td')

            info_list = []
            for compound in compounds:
                info_list.append(compound.find_element_by_tag_name('font').text)
            print(info_list)

            if args.anonymous:
                    if info_list[2] == 'NOA':
                        continue

            useful_info.append(info_list[1].lower() + '#' + info_list[0] + '\n')

    else:
        print("Lol, I haven't include this feature yet")
        driver.quit()
        exit()

    try:
        with open(args.file, 'w') as file:
            file.writelines(useful_info)
    except:
        print("You got some problems with output file")
        

    driver.quit()


if __name__ == "__main__":
    try:
        with open(args.proxy_lists) as file:
            strings = file.readlines()
            
            found = False
            for index, site in enumerate(strings):
                if args.site in site:
                    found = True
                    mode = index
                    break
            
            if not found:
                print("You had setted the denied site")
                raise ValueError("swag")


    except:
        print("You have some problems with files")
        exit()

    main()
