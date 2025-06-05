# Reconnaissance Report – testphp.vulnweb.com

This report contains findings from a Level 1 reconnaissance exercise on the web application hosted at `http://testphp.vulnweb.com`. The objective was to gather surface-level technical information using both passive and active methods.

---

## Target Overview

- **URL:** http://testphp.vulnweb.com  
- **IP Address:** 44.228.249.3  
- **Hosting Provider:** Amazon EC2  
- **Reverse DNS:** ec2-44-228-249-3.us-west-2.compute.amazonaws.com

---

## DNS Information

- **A Record:** 44.228.249.3
- **rDNS:** ec2-44-228-249-3.us-west-2.compute.amazonaws.com
- **Name Servers:**
  - ns-1822.awsdns-35.co.uk
  - ns-1147.awsdns-15.org
  - ns-968.awsdns-57.net
  - ns-297.awsdns-37.com
- **MX Records:** None found

---

## Technology Stack

- **Web Server:** nginx/1.19.0
- **Backend Language:** PHP 5.6.40-38 (Ubuntu 20.04)
- **Platform:** Likely Ubuntu 20.04.1 LTS
- **Frontend Technologies:** HTML, JavaScript
- **Legacy Features:** Adobe Flash, ActiveX
- **Headers:**
  - `X-Powered-By: PHP/5.6.40-38+ubuntu20.04.1+deb.sury.org+1`

---

## Subdomains Identified

- `www.testphp.vulnweb.com`
- `sieb-web1.testphp.vulnweb.com`

---

## Open Ports and Services

| Port | Protocol | State | Service |
|------|----------|-------|---------|
| 80   | TCP      | Open  | HTTP (nginx 1.19.0) |
| Others | TCP | Filtered | 999 ports scanned with no response |

---

## Directory Enumeration

Discovered via `ffuf` and `dirsearch`:

- `/`
- `/admin/`
- `/cgi-bin/`
- `/crossdomain.xml`
- `/CVS/`  
  - `/CVS/Entries`  
  - `/CVS/Root`
- `/images/`
- `/pictures/`
- `/secured/`
- `/vendor/`
- `/index.php`
- `/index.bak`
- `/index.zip`
- `/logout.php`
- `/login.php`
- `/product.php`
- `/search.php`
- `/signup.php`
- `/userinfo.php`
- `/.idea/`
  - `.idea/modules.xml`
  - `.idea/workspace.xml`
  - `.idea/vcs.xml`
- `/_mmServerScripts/`
- `/Connections/`
- `/404.php`
- `/favicon.ico`

---

## Page Titles, Parameters, and Forms

- **Homepage Title:** Home of Acunetix Art
- **Forms Found:**  
  - `<form action="search.php?test=query" method="post">`
    - `input name="searchFor"` (text)
    - `input name="goButton"` (submit)

| Type        | Tools Used                                     | Examples                                              |
| ----------- | ---------------------------------------------- | ----------------------------------------------------- |
| **Passive** | `whois`, `dig`, `curl`, `waybackurls`, `httpx` | Domain info, DNS records, historical URLs             |
| **Active**  | `nmap`, `ffuf`, `dirsearch`, `curl` (POSTs)    | Live port scan, directory brute force, form detection |

