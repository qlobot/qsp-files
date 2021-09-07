#!/usr/bin/env python3

import json
from urllib.parse import quote
from os import listdir
from os.path import isfile, join


qsp_dir = "QSP Files"
output = "index-files.md"

qsp_files = [f for f in listdir(qsp_dir) if isfile(join(qsp_dir, f))]

writer = open(output, 'w')
writer.write("""
[//]: # (File ini adalah hasil generate dari generator.py)
[//]: # (Jangan update secara manual)

# Daftar File QSP

**TIPS**: Untuk memudahkan download, klik kanan pada kolom **QSP File** lalu klik **Save link as..**.

| Wesite | QSP File |
| ------ | -------- |
""")

for file in qsp_files:
    with open(join(qsp_dir, file), "r") as f:
        data = json.load(f)
        out_line = '''| [{}]({}) | [{}](https://raw.githubusercontent.com/qlobot/qlobot-scrap-plugins/main/{}) |\n'''

        writer.write(out_line.format(data['name'], data['base_url'][0], file, quote(qsp_dir)+"/"+quote(file)))

writer.close()