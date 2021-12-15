import argparse
import re
import json
from collections import defaultdict

parser = argparse.ArgumentParser(description='Process access.log')
# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/library/argparse.html#the-add-argument-method
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
args = parser.parse_args()

dict_ip = defaultdict(
    lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
)

with open(args.file) as file:
    idx = 0
    for line in file:
        if idx > 99:
            break

        # 109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip_match is not None:
            ip = ip_match.group()
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line)
            if method is not None:
                dict_ip[ip][method.group(1)] += 1
                idx += 1

print(json.dumps(dict_ip, indent=4))
