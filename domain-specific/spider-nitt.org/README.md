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




