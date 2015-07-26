import csv
import os.path


mod_table = {
    'NF': 1 <<  0,
    'EZ': 1 <<  1,
    'NV': 1 <<  2,
    'HD': 1 <<  3,
    'HR': 1 <<  4,
    'SD': 1 <<  5,
    'DT': 1 <<  6,
    # Relax
    'HT': 1 <<  8,
    'NC': 1 <<  9,
    'FL': 1 << 10,
    # Auto
    'SO': 1 << 12,
    # Autopilot
    'PF': 1 << 14,
}

def load_names():
    names = {}
    with open('names.csv', 'r') as fd:
        reader = csv.reader(fd)
        for user_id, user_name in reader:
            names[user_id] = user_name
    return names

def load_scores():
    data = {}
    with open('scores.csv', 'r') as fd:
        reader = csv.reader(fd)
        for user_id, beatmap_id, mods, pp in reader:
            data.setdefault(user_id, []).append((int(mods), float(pp)))
    return data


def process(data, filter_fun):
    return {user_id: [score[1] for score in scores if filter_fun(score[0])]
                for user_id, scores in data.items()}


def create_filter(**kwargs):
    allowed = {0}
    for mod in mod_table:
        # indifferent about unspecified mods, force mod if specified
        new_allowed = allowed
        if kwargs.get(mod, True):
            new_allowed = {c | mod_table[mod] for c in allowed}
        if mod not in kwargs:
            new_allowed |= allowed
        allowed = new_allowed
    return (lambda x: x in allowed)


def exponential_decay(iterable, decay_rate):
    return sum(pp * decay_rate**i for i, pp in enumerate(iterable))


def to_markdown_table(result, names):
    yield '| Rank | Player Name |  PP  |'
    yield '| ----:|:----------- | ----:|'
    for i, entry in enumerate(result, start=1):
        user_id, pp = entry
        if pp == 0:
            break
        url = '[{}](https://osu.ppy.sh/u/{})'.format(names[user_id], user_id)
        yield '| {} | {} | {} |'.format(i, url, round(pp, 2))


filters = {
    'AnyMod': create_filter(),
    'NoMod': create_filter(DT=0, HT=0, HR=0, EZ=0, HD=0, FL=0),
    'DT + others': create_filter(DT=1),
    'FL + others': create_filter(FL=1),
    'HT + others': create_filter(HT=1),
    'EZ + others': create_filter(EZ=1),
    'HD + others': create_filter(HD=1),
    'HR + others': create_filter(HR=1),
    'DTHR (HD optional)': create_filter(DT=1, HR=1, FL=0),
    'HDHR (no DT)': create_filter(HD=1, HR=1, DT=0, FL=0),
    'FullMod': create_filter(DT=1, HR=1, HD=1, FL=1),
}
names = load_names()
data = load_scores()

for filter_name, f in filters.items():
    processed_data = process(data, f)
    weighted_data = {k: exponential_decay(v, 0.95) for k, v in processed_data.items()}
    result = sorted(weighted_data.items(), key=lambda x: x[1], reverse=True)
    filename = '{}.markdown'.format(filter_name)
    with open(os.path.join('results', filename), 'w') as fd:
        fd.write('# {}\n'.format(filter_name))
        fd.write('\n'.join(to_markdown_table(result, names)))
        fd.write('\n')
