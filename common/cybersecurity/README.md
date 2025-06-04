# Publicly Exposed Tesla Assets Using Google Dorks

### Spider R&D Inductions 2025 – Cybersecurity Common Task

This report documents the use of Google Dorks to identify publicly exposed Tesla assets. Some generic dorks are also included where Tesla-specific results were limited.

---

### 1. Publicly Accessible Confidential Documents

![image](https://github.com/user-attachments/assets/9ca2fc03-0240-4726-ad61-75175eb573ad)

**Dork:** `site:tesla.com "confidential"`
* **Findings:**
    * Archived Model Y reference diagram (original locked, accessed via Wayback Machine):
        * `https://web.archive.org/web/20250406224538/https://service.tesla.com/docs/ModelY/ElectricalReference/prog-196/diagram/2022.1_ModelY-SOP4.pdf`
    * 2012 Model S electrical document (not protected):
        * `https://service.tesla.com/docs/ModelS/ElectricalReference2012/s-lhd-sop1/2012_ModelS_LHD_Release.pdf`

**Dork:** `"tesla" filetype:xlsx "confidential"`
* **Finding:**
    * Tesla employee contacts:
        * `https://www.neso.energy/document/323126/download`

---

### 2. Exposed Login Portals

**Dork:** `site:tesla.com inurl:login`
* **Findings:**
    * `https://login.solarcity.com/`
    * `https://feedback.tesla.com/login/identity-provider-select?stateID=2e044c72-b2f2-4370-92a5-583ea5148f8f`

**Dork:** `site:tesla.com inurl:auth`
* **Finding:**
    * `https://inside.tesla.com/en-US/en-us/auth/login`

---

### 3. Public Backup / Config Files

**Dork:** `site:tesla.com filetype:tar.gz`
* **Finding:**
    * `https://os.tesla.com/parrot-sources/parrot-sources.tar.gz`

---

### 4. Exposed Logs / Error Messages

**Dork:** `"tesla" intitle:"index of" "config"`
* **Finding:**
    * `https://evwest.com/support/?SD`

**Dork:** `intext:"proftpd.conf" "index of"`
* **Finding:**
    * `https://genesis.jpl.nasa.gov/ftp/`

---

### 5. Publicly Listed Contact Info

**Dork:** `site:tesla.com intext:@tesla.com`
* **Finding:**
    * `https://www.tesla.com/contact`

**Dork:** `site:tesla.com intext:email`
* **Finding:**
    * `https://www.tesla.com/support/energy/more/additional-support/contact-us`

---

### 6. Exposed Git / Env Files (Examples)

**Dork:** `"index of" /.env OR /config.php -github.com`
* **Finding:**
    * `https://amda.irap.omp.eu/php/`

**Dork:** `intitle:"index of" env.cgi`
* **Finding:**
    * `http://46.188.44.46:8081/env/`
