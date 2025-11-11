from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as drtd:
    drtd.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    drtd.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #drtd.set_window_size(resolution.width, resolution.height)
    #"#live-channel-stream-information"
    url = "https://kick.com/brutalles"
    drtd.uc_open_with_reconnect(url, 4)
    drtd.sleep(4)
    drtd.uc_gui_click_captcha()
    drtd.sleep(1)
    drtd.uc_gui_handle_captcha()
    drtd.sleep(4)
    if drtd.is_element_present('button:contains("Accept")'):
        drtd.uc_click('button:contains("Accept")', reconnect_time=4)
    if drtd.is_element_visible('#injected-channel-player'):
        drtd2 = drtd.get_new_driver(undetectable=True)
        drtd2.uc_open_with_reconnect("https://www.twitch.tv/brutalles", 5)
        drtd2.uc_gui_click_captcha()
        drtd2.uc_gui_handle_captcha()
        drtd.sleep(10)
        if drtd2.is_element_present('button:contains("Accept")'):
            drtd2.uc_click('button:contains("Accept")', reconnect_time=4)
        while drtd.is_element_visible('#injected-channel-player'):
            drtd.sleep(100)
        drtd.quit_extra_driver()
    drtd.sleep(1)
    if drtd.is_element_present("#live-channel-stream-information"):
        url = "https://www.twitch.tv/brutalles"
        drtd.uc_open_with_reconnect(url, 5)
        if drtd.is_element_present('button:contains("Accept")'):
            drtd.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            drtd2 = drtd.get_new_driver(undetectable=True)
            drtd2.uc_open_with_reconnect("https://kick.com/brutalles", 5)
            drtd.sleep(10)
            if drtd2.is_element_present('button:contains("Accept")'):
                drtd2.uc_click('button:contains("Accept")', reconnect_time=4)
            while drtd.is_element_present("#live-channel-stream-information"):
                drtd.sleep(100)
            drtd.quit_extra_driver()
    drtd.sleep(1)
