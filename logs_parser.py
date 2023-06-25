import re
from log import Log
from datetime import datetime
from time import strftime


def parse(line):
    regex = re.compile('((\d{1,3}\.){3}\d{1,3}) - - \[(\d{1,2}\/\w{3}\/\d{4}\:\d{1,2}\:\d{1,2}\:\d{1,2}) (\+|-)(\d{3})\] "(\w+) (\/\S+) (HTTP\/\d\.\d)" (\d{3}) (\d+)')
    for m in regex.finditer(line):
        ip = m.group(1)
        created_at = datetime.strptime(m.group(3), '%d/%b/%Y:%H:%M:%S')
        gmt = m.group(4) + m.group(5)
        request = m.group(6)
        adress = m.group(7)
        http = m.group(8)
        code = int(m.group(9))
        size = int(m.group(10))
        return Log(ip, created_at, gmt, request, adress, http, code, size)

