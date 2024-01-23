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
def writedata(output,data):
    with open(output,'a') as file:
        file.write(data)