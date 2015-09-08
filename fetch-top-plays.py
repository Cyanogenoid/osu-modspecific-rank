import csv
import json
import time
import collections
import sys

import requests

import api_key


REQUESTS_PER_MINUTE = 59

user_ids = collections.OrderedDict()
with open('names.csv', 'r') as fd:
    reader = csv.reader(fd)
    for line in reader:
        user_id = line[0]
        user_name = line[1]
        user_ids[user_id] = user_name

url = "https://osu.ppy.sh/api/get_user_best"
for i, user_id in enumerate(user_ids):
    start_time = time.perf_counter()
    completion = 100 * i / len(user_ids)
    print('{}% complete'.format(completion))
    print('Requesting best plays from {} ({})'.format(user_ids[user_id], user_id))
    payload = {
        'k': api_key.key,
        'u': user_id,
        'type': 'id',
        'm': 0,  # osu! standard
        'limit': 100,
    }
    success = False
    while not success:
        try:
            r = requests.get(url, params=payload)
            r.raise_for_status()
            best_scores = json.loads(r.text)
            success = True
        except Exception as e:
            print('ERROR ({}): {}'.format(user_id, e), file=sys.stderr)
            print('Retrying {}...'.format(user_id))
            time.sleep(2)

    with open('scores.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for score in best_scores:
            pp = score['pp']
            mods = score['enabled_mods']
            beatmap = score['beatmap_id']
            writer.writerow([user_id, beatmap, mods, pp])
    end_time = time.perf_counter()
    time_diff = end_time - start_time
    wait_time = max(0, 60/REQUESTS_PER_MINUTE - time_diff)
    print('{0:.4f} s elapsed, waiting {1:.4f} s'.format(time_diff, wait_time))
    time.sleep(wait_time)
