# SilentRaider

SilentRaider is an HTTP DoS testing tool designed to assess a server's capacity to withstand intensive and persistent HTTP requests. It exploits the HTTP Keep Alive + NoCache attack vector to simulate stress scenarios where the server must handle extended connections and repeated non-cached requests, challenging both the stability and security of HTTP services against denial-of-service threats.

# Usage
 USAGE:
 ```bash 
 ./SilentRaider.py <url> [OPTIONS]
```
 ```bash 
 OPTIONS:
    _____________________________________________________________________________________________________
   |       Flag:       |                Description:                     |           Default:            |
   |-------------------|-------------------------------------------------|-------------------------------|
   | -u, --useragents  | File with user-agents to use                    | (default: randomly generated) |
   | -w, --workers     | Number of concurrent workers                    | (default: 50)                 |
   | -s, --sockets     | Number of concurrent sockets                    | (default: 30)                 |
   | -m, --method      | HTTP Method to use 'get' or 'post'  or 'random' | (default: get)                |
   | -d, --debug       | Enable Debug Mode [more verbose output]         | (default: False)              |
   | -n, --nosslcheck  | Do not verify SSL Certificate                   | (default: True)               |
   | -h, --help        | Shows this help                                 |                               |
   -------------------------------------------------------------------------------------------------------
 ```
# Utilities
● util/getuas.py - Fetches user-agent lists from http://www.useragentstring.com/pages/useragentstring.php subpages
(ex: ./getuas.py "http://www.useragentstring.com/pages/useragentstring.php?name=All") |(!REQUIRES BEAUTIFULSOUP4!)|

● res/lists/useragents - Text lists (one per line) of User-Agent strings (from http://www.useragentstring.com)
