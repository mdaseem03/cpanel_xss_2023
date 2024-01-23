#!/usr/bin/env python3


"""
 * cpanel_xss_2023
 * CVE-2023-29489 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * Developed By mdaseem03 
 * Intern
 * Cappricio Securities <https://cappriciosec.com>
 */
 
"""
import requests
from utils import const
from utils import configure

def sendmessage(vul):

    data = {"Tname": "cpanel_xss_2023", "chatid": configure.get_chatid(), "data": vul,
            "bugname": const.Data.bugname, "Priority": "Medium"}

    headers = {
        "Content-Type": "application/json",
    }
    try:
        response = requests.put(const.Data.api, json=data, headers=headers)
    except:
        print("Bot Error")
