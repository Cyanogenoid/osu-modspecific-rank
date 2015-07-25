import csv
import time

import requests
import lxml.html


top10k = {}
for page_index in range(1, 201):
    print('Requesting page {}'.format(page_index))
    url = 'https://osu.ppy.sh/p/pp/'
    payload = {
        'm': 0,  # osu! standard gamemode
        'o': 1,  # descending order
        'page': page_index,
    }
    page = requests.get(url, params=payload)
    tree = lxml.html.document_fromstring(page.text)
    print('Processing page {}'.format(page_index))
    rows = tree.cssselect('tr a')
    for row in rows:
        user_name = row.text
        user_id = row.attrib['href'][3:]
        top10k[user_id] = user_name
        print(user_name, user_id)
    time.sleep(1)  # Be nice and slow down


with open('10k.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for user_id, user_name in top10k.items():
        writer.writerow([user_id, user_name])
