#!/usr/bin/env python

import json

while True:
    first = raw_input('First name: ')
    if not first:
        break

    last = raw_input('Last name : ')
    party = raw_input('Party     : ')
    candidate = raw_input('Where     : ')

    filename = '{}-{}.json'.format(last.lower().translate(None, " -'"),
                                   first.lower().translate(None, " -'"))
    data = {
        'first_name': first,
        'last_name': last,
        'party': party,
        'candidate': candidate
    }

    if candidate.startswith('state'):
        data['ballot_position'] = int(raw_input('Position  : '))

    dpf = 'data/people/' + filename
    open(dpf, 'w').write(json.dumps(data, sort_keys=True,
                                    indent=4, separators=(',', ': ')))
    print open(dpf).read()
    print ""
