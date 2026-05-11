import time
import requests
from bs4 import BeautifulSoup as BS

DoWrite = 1
DoPrint = 0
links_list = []
text_list = []

def scrapeUseme(url):
    resp = requests.get(url)
    resp.raise_for_status()

    soup = BS(resp.text, 'html.parser')


if(DoWrite == 1):
    try:
        f = open("./links.txt", "w")
    except:
        f = open("./links.txt", "x")

url_list =[
    f"https://useme.com/pl/jobs/category/programowanie-i-it,35/?page=",
    f"https://www.pracuj.pl/praca/opole;wp?rd=0&et=1%2C17%2C2&pn="
    ]

for j in range(len(url_list)):
    for i in range(1,6):
        print("loop")

url = url_list[j] + f"{i}"
print(url)
time.sleep(2)  
# input("Proceed? ")

for i in range(len(titles)):
    if titles[i].text != '':
        print("getting elements")
        text_list.append([
            titles[i].text
        ])
        links_list.append(
        )
h = 0
if(DoWrite == 1):
    # Write extracted data
    for row in text_list:
        f.write(f"Ogłoszenie:\n{row[0]}\nLink:\n{links_list[h]}\n")
        h+=1

h = 0
if(DoPrint == 1):
    for row in text_list:
        print(f"\nOgłoszenie:\n{row[0]}")
        print(f"Link:\n{links_list[h]}")
        h += 1


# element_list.remove('')
driver.quit()

# if(DoWrite == 1):
#     try:
#         f = open("./links.txt", "w")
#     except:
#         f = open("./links.txt", "x")
#     # Write extracted data
#     for row in text_list:
#         for i in row:
#             print("%s: ", i)
#             f.write(i + ": ")
#         f.write("\n")

# h = 0
# if(DoPrint == 1):
#     for row in text_list:
#         print(f"\nOgłoszenie:\n{row[0]}")
#         print(f"Link:\n{links_list[h]}")
#         h += 1

# print(f"TEXT_LIST:\n{text_list}")
# print(f"LINKS_LIST:\n{links_list}")