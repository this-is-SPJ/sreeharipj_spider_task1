# Recon & Exploitation on "spider server"

This document summarizes reconnaissance and exploitation findings on the `spider.nitt.edu` infrastructure during the Spider R&D Club selection process. The goal was to identify vulnerabilities, misconfigurations, and insecure design patterns across subdomains and endpoints using open-source tools and manual testing.

---

## Scope
*.spider.nitt.edu
(subdomains of spider server)
---

## Reconnaissance

**Target:** spider.nitt.edu (203.129.195.136)
**Open Ports:** 22, 80, 443
**Web Server:** Nginx 1.20.1

**Used subfinder to find 9 subdomains:**
api.spider.nitt.edu
restapis.lcas.spider.nitt.edu
lynx.spider.nitt.edu
api.lynx.spider.nitt.edu
api.lynxid.spider.nitt.edu
ctf.spider.nitt.edu
inductions.spider.nitt.edu
api.inductions.spider.nitt.edu
grpc.lcas.spider.nitt.edu

from these i thought that one of the subdomain was vernerable (which was wrongly assumed), various methods of recon was used, then these are what i found

### inductions.spider.nitt.edu

* inductions.spider.nitt.edu allows HTTP PUT and DELETE methods without authentication(200 OK), but not able to exploit.(refer txt attached)
* 




### api,spider.nitt.edu

Insecure CORS Configuration on GraphQL Endpoint <<< found while monitering `https://api.spider.nitt.edu/signin` via burp

Endpoint:
POST [https://api.spider.nitt.edu/api/graphql](https://api.spider.nitt.edu/api/graphql)

Issue:
The endpoint, responsible for user authentication (via the authenticateUserWithPassword GraphQL mutation) and likely other authenticated API functions, consistently returns the HTTP headers:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

Impact:
This combination allows a malicious website visited by an authenticated user of api.spider.nitt.edu to make requests to this GraphQL endpoint using the victim's credentials (cookies). The malicious site could then read the response, leading to potential:

* Session hijacking (if session tokens are passed in body/header accessible via JS post-auth).
* Unauthorized data exfiltration via other GraphQL queries accessible post-authentication.
* Execution of unauthorized actions via other GraphQL mutations.

An attacker could craft a webpage that, when visited by a logged-in user, uses JavaScript fetch with {credentials: 'include'} to make arbitrary (authenticated) GraphQL queries/mutations to this endpoint and potentially exfiltrate data.

Honestly i am not sure if this is false flag or not
