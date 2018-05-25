import requests
from bs4 import BeautifulSoup

base_url = "https://ridibooks.com/bestsellers/general?order=weekly&page={}"

ridi_page = 2

for n in range(ridi_page):
    url = base_url.format(n+1)
    # print(url)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    # print(html)

    title_list_find = soup.find_all(class_="title_text")
    id_title = 1
    for title_find in title_list_find:
        print(str(id_title) + " " + title_find.text.strip())
        id_title += 1

    # rate_list_find1 = soup.find_all(class_="book_metadata star_rate hidden_for_portrait")
    # print(type(rate_list_find))
    # print(rate_list_find)

#    rate_list_find2 = rate_list_find1.find(class_="StarRate_Score")
#    for rate_find in rate_list_find2:
#        print(rate_find.text.strip())


    rate_list_sel = soup.select('.book_metadata.star_rate.hidden_for_portrait .StarRate_Score')
#   print(rate_list_sel)
    for rate_sel in rate_list_sel:
        print(rate_sel.text.strip())

    count_list_find = soup.select('.book_metadata.star_rate.hidden_for_portrait .StarRate_ParticipantCount')
#   count_list_find = soup.find_all(class_="StarRate_ParticipantCount")
    for count_find in count_list_find:
        print(count_find.text.strip())
    

  # title_list_sel = soup.select('div > h3 > a > span')
  # for title_sel in title_list_sel:
  #     print(title_sel.text)
