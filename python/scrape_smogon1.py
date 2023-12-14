#!/usr/bin/python3

import json
import requests
import time

from bs4 import BeautifulSoup
from pathlib import Path

URL_TEMPLATE = "https://www.smogon.com/dex/{}/pokemon/"
GENERATIONS = ("rb", "gs", "rs", "dp", "bw", "xy", "sm", "ss", "sv")
OUTPUT_FOLDER = "./strategy_pokedex"
OUTPUT_FILES = dict(
    zip(
        (Path(f"{OUTPUT_FOLDER}/gen{x}.json") for x in (x for x in range(1, len(GENERATIONS)))),
        [URL_TEMPLATE.format(x) for x in GENERATIONS]
    )
)

Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)

for (file, source) in OUTPUT_FILES.items():
    source_page = requests.get(source)
    page_soup = BeautifulSoup(source_page.text, 'html.parser')

    javascript_code = (
        [x for x in (x.text for x in (page_soup.find_all("script"))) if x][0]
    )
    target_data = json.dumps(
        (
            json.loads(
                javascript_code[javascript_code.find("{"):]
            )
        ).get('injectRpcs')[1][1], indent=4
    )
    file.write_text(target_data)

    time.sleep(15)