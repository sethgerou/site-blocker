# program to block specific sites (listed in website_list) during work hours on week days.

import time
from datetime import datetime as dt

#  r before path escapes special characters
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.gizmodo.com", "gizmodo.com", "www.engadget.com", "engadget.con"]

while True:
    # check to see whether the current time is between 8am on 4PM and not saturday or sunday.
    if (8 < dt.now().hour < 16) and dt.now().weekday() not in (5,6):
        print("working hours - blocking gadget sites.")
        with open(hosts_path, "r+") as hosts:
            content = hosts.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    hosts.write(redirect + " " + site + "\n")
    else:
        print("fun hours - no sites blocked.")
        with open(hosts_path, "r+") as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    hosts.write(line)
            hosts.truncate()
    time.sleep(300)
