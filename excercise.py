# number 1
# import re
# student_portfolio = "jogn is a student of cycloboard and his matric number is m123d but he often says he is the scholar of our time"
# checks = re.findall("[\d]" , student_portfolio)
# checker = re.findall("\w" , student_portfolio)
# checking = re.findall("\s" , student_portfolio)
# if checks:
#     print('the integers were found', checks)
# if checker:
#     print('the word were found', checker)
# if checking:
#     print('the space was idenhtified', checking)    


# number 2
# import re
# string = 'glover '
# match = re.sub("\s", "_23", string, )
# print(match)

# number 3
# import re
# parababa = 'james, ire, kesh, lambert, ebube, asake aliyat, amazon211'
# matching = re.findall ("\w" "+" "\d", parababa)
# print (matching) 


# number4
# import re
# sentence = "i am john, the name of my tech acdemy is cyclobold "
# space = re.findall("\s", sentence)
# substituting = re.sub(","," and",sentence )
# print(space)
# # # print(sentence)
# # print(substituting)

# # number 5
# import re
# words = "eleniyan, jagun, ade, akande, temi, ebosky"
# begin = re.findall("\w" "+" "[^a | e]",words)
# print(begin)

# number 6
# import re
# # x = 0
# emails = input("your email: ")
# pampers = re.findall("\w" "+" "[ .com|\.net|\.org|\.edu $]" , emails)
# print(pampers)
# if pampers:
#     print(f"registration succseful {pampers}")
# else:
#     print('wrong input')


    # number 7
# print('hello')
# import re
# import requests
# from bs4 import BeautifulSoup 
# r = requests.get ("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# order = data.prettify()
# para = data.find_all('p')
# test = str(para)
# print(test)
# validation = "movies, form"
# validating = re.findall("movies" "form" "\s" "\d", test)
# if validating:
#     print("succesful")
# else:
#     raise TypeError("unsuccesful")


# number 8
# import requests
# from bs4 import BeautifulSoup
# r = requests.get ("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# order = data.prettify()
# para = data.find_all('p')
# test = str(para)
# pdf = open("exec.pdf", "w")
# pdf.write(test)
# pdf.close()

# number 9
# import webbrowser
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# order = data.prettify()
# para = data.find_all('img')
# print(para)
# test = str(para)
# # img = open("imgg.html", "w")
# # img.write(test)
# # img.close()
# # webbrowser.open("imgg.html")


