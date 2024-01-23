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

from includes import scan

def reader(input,output):
    try:
        with open(input,'r') as file:
            for line in file:
                scan.cvescan(line.strip(), output)
    except FileNotFoundError:
        print("File not found. Check the file path and name.")

    