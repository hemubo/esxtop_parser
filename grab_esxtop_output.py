#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import pexpect
import os
import string
import re

def cleanoutput(output):
    output = re.sub('\015', '', output)
    output = re.sub('\[\?\d+h\[H\[\d+J\[\d+;\d+H\[\d+m\[\d+;\d+H', '', output)
    output = re.sub('\[\d+;\d+H\[K\[\d+;\d+H\[\d+m', '', output)
    output = re.sub('\[K\[\d+m\[J\[\d+;\d+H\[\d+;\d+H', '', output)
    output = re.sub('\[K.*H?', '', output)
    output = re.sub('\[\d+m.*H?', '', output)
    output = re.sub('\[\d+;\d+H\[\d+;\d+H\[\d+m','', output)
    return output


def main():
    os.environ['TERM'] = 'xterm'
    output, status = pexpect.run("sh ./runcpu.sh", timeout=4, withexitstatus=1)
    output = output.decode('utf-8')
    cpuoutput = b""
    cpuoutput = cpuoutput.decode('utf-8') # python 3 compliance.
    for o in output:
        if o in string.printable:
           cpuoutput += o
    cpuoutput = cleanoutput(cpuoutput)
    with open('cpu_and_network_data.txt', 'w') as f:
        f.write(""+'-'*131+"\n")
        f.write(" "*70+"CPU data"+" "*53+"\n")
        f.write(""+'-'*131+"\n")
        f.write("\n")
        f.write(cpuoutput)
        f.write("\n"+'-'*131+"\n")
    output, status = pexpect.run("sh ./runnet.sh", timeout=4, withexitstatus=1)
    output = output.decode('utf-8')
    networkoutput = b""
    networkoutput = networkoutput.decode('utf-8')
    for o in output:
        if o in string.printable:
           networkoutput += o
    networkoutput = cleanoutput(networkoutput)

    with open('cpu_and_network_data.txt', 'a') as f:
        f.write(" "*70+"Network Data"+" "*53+"\n")
        f.write('-'*131+"\n")
        f.write(networkoutput)
        f.write("\n"+'-'*131+"\n")
    pid = os.getpid()
    os.system("kill -9 `pgrep python | xargs -n1 | grep -v {0}` >/dev/null 2>&1".format(pid))
    os.system("kill -9 `pgrep esxtop` >/dev/null 2>&1")

if __name__ == '__main__':
    main()
