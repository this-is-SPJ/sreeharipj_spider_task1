# Cybersecurity - Domain specific

## Task 1 – Reconnaissance

Map the surface area of the web app: `http://testphp.vulnweb.com`
Refer to `/Recon-vulnweb/`

---

## Task 3 – Live Recon & Exploitation

**Objective:**  
Conduct real-world recon and basic exploitation on the Spider server.

### Phase 1: spider.nitt.edu  
Initial recon was performed on `*.spider.nitt.edu` due to unclear specification of the "Spider Server".  
Refer to `/spider.nitt.edu/`

### Phase 2: spider-nitt.org  
Later clarification revealed that the intended target was `spider-nitt.org`.  
Deep analysis of subdomain `spidertest.spider-nitt.org` led to the discovery of an exposed DVWA (Damn Vulnerable Web Application) instance.
Refer to `/spider-nitt.org/`
