#!/usr/bin/env python3

import sys
import csv

import yaml

with open(sys.argv[1]) as tsvfile:
    photoreader = csv.DictReader(tsvfile, delimiter='\t')
    n = 0
    for row in photoreader:
        description = row.pop('photo_description')
        animal_tag = row.get('photo_keyword') + 's'
        if animal_tag != 'dogs':
            if animal_tag != 'cats':
                animal_tag = 'others'
        row['tags'] = 'photos', animal_tag
        row['layout'] = 'base'
        with open(f'../photos/{n:03}.html', 'w') as f:
            yaml.dump(row, f, explicit_start=True)
            print('---', file=f)
            html = f"""    <div class="pet-photo-file">
        <img src="{{{{ photo_image_url }}}}" height="600"/>
        <figcaption>{description}</figcaption>
    </div>"""
            print(html, file=f)
        n += 1
