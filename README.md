# DDoS-Protection
Quick-coded (D)DoS protection on flask web applications.

# Requirements
`flask`

# Usage
`python3 server.py`

# How it works?
It refuses to accept requests on the page the code is located.
After 10 requests, it blocks them. To change number of requests just do it on 6th line `rate_limit = numberofrequests`
