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
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""
    
👋 Hey \033[96m{username}
   \033[92m                                                             v1.0
   ___ ___               _  __  _____ ___   ___ __ ___ ____
  / __| _ \__ _ _ _  ___| | \ \/ / __/ __| |_  )  \_  )__ /
 | (__|  _/ _` | ' \/ -_) |  >  <\__ \__ \  / / () / / |_ \
  \___|_| \__,_|_||_\___|_| /_/\_\___/___/ /___\__/___|___/
                                                               

                                   \033[0mDeveloped By \x1b[31;1m\033[4m@mdaseem03\033[0m


\x1b[31;1mCVE-2021-20323 : Bug scanner for WebPentesters and Bugbounty Hunters 

\x1b[31;1m$ \033[92mCVE-2021-20323\033[0m [option]

Usage: \033[92mCVE-2021-20323\033[0m [options]

Options:
  -u, --url     URL to scan                                CVE-2021-20323 -u https://target.com                
  -i, --input   <filename> Read input from txt             CVE-2021-20323 -i target.txt                         
  -o, --output  <filename> Write output in txt file        CVE-2021-20323 -i target.txt -o output.txt     
  -c, --chatid  Creating Telegram Notification             CVE-2021-20323 --chatid yourid    
  -h, --help    Help Menu                       
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
   \033[92m                                                             v1.0
   ___ ___               _  __  _____ ___   ___ __ ___ ____
  / __| _ \__ _ _ _  ___| | \ \/ / __/ __| |_  )  \_  )__ /
 | (__|  _/ _` | ' \/ -_) |  >  <\__ \__ \  / / () / / |_ \\
  \___|_| \__,_|_||_\___|_| /_/\_\___/___/ /___\__/___|___/
                                                               

                                   \033[0mDeveloped By \x1b[31;1m\033[4m@mdaseem03\033[0m


\x1b[31;1mCVE-2023-29489 scanner for WebPentesters and Bugbounty Hunters 

\033[0m"""
    print(help_banner)
