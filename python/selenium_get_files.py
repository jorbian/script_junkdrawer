#!/usr/bin/python3

import requests
import time

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

def create_file_name(url):
    return ((url[url.rfind("/") + 1:]))

url = "https://musicasacra.com/recordings/audio"

outfolder_path = create_file_name(url)
outfolder_obj = Path(outfolder_path)

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("incognito")

driver = webdriver.Chrome(options)
driver.get(url)

mp3_file_urls = [
    y for y in (
        x.get_attribute('href') for x in
            driver.find_elements(By.XPATH, "//a[@href]")
    ) if ".mp3" in y
]
mp3_file_objs = [
    Path(f"./{outfolder_obj.name}/{create_file_name(x)}") for x in mp3_file_urls
]

outfolder_obj.mkdir(parents=True, exist_ok=True)

for (url, file_obj) in zip(mp3_file_urls, mp3_file_objs):
    #TRIES TO DOWNLOAD IN THE LEAST DOUCHEY WAY IT CAN
    response_obj = requests.get(url)
    if (not response_obj.ok):
        continue

    file_obj.write_bytes(response_obj.content)
    time.sleep(5)

driver.quit()