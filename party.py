#!/usr/bin/env python

import json

while True:
    code = raw_input('Code   : ')
    if not code:
        break

    name = raw_input('Name   : ')
    website = raw_input('Website: ')

    filename = '{}.json'.format(code.lower())

    data = {
        'name': name,
        'code': code.upper(),
    }

    if website:
        data['website'] = website

    dfp = 'data/parties/' + filename
    open(dfp, 'w').write(json.dumps(data, sort_keys=True,
                                    indent=4, separators=(',', ': ')))
    print open(dfp).read()
    print ""
