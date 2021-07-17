#!/usr/bin/env python3

import sys
import csv

import yaml

with open(sys.argv[1]) as tsvfile:
    photoreader = csv.DictReader(tsvfile, delimiter='\t')
    n = 0
    for row in photoreader:
        description = row.pop('photo_description')
        row['tags'] = 'photos'
        row['layout'] = 'pets'
        with open(f'../photos/{n:03}.html', 'w') as f:
            yaml.dump(row, f, explicit_start=True)
            print('---', file=f)
            html = f"""    <figure>
        <img src="{{{{ photo_image_url }}}}" height="600" />
        <figcaption>{description}</figcaption>
    </figure>"""
            print(html, file=f)
        n += 1
