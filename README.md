# esxtop_parser
Grab the output of interactive esxtop parser..

Most of the articles talks about the esxtop batch mode which results in tonns of column CSV data.

The “esxtop” command is a special command which has two complex characteristics. 
It wont write output to stdout so  shell redirections won’t work. 
* It basically writes to terminal device (/dev/tty (or) /dev/pts)
* It redraws screen, which means that for every ’n’ seconds you will get the refreshed data. 

Thanks to python and pexpect, through which we can grab esxtop output while it is in interactive mode.

Basically, the logic is that, through python, we are opening a new pseudo terminal device and executing the esxtop command in that terminal.
Since it esxtop uses “curses” module for self refreshing (redrawing the terminal screen), the generated output has too many terminal control escape characters).
I cleared out all of them through script and made the final copy of the script ready. 

Also, to avoid typing ’n’ for network, ‘c’ for cpu on esxtop, I generated the configuration files and used it appropriately for esxtop. (using its ‘-c’ option).
If you start esxtop with the network configuration, it will dump the data of the network only. The same logic is hold good for cpu configuration. For other configurations, goto esxtop interactive mode and type 'h'

**Pre-requisites**
* Python 2.7+
* pexpect module (pip install pexpect)

**How to run**
* Naviagate to the script directory
* Run python grab_esxtop_output.py
* output will be saved under "cpu_and_network_data.txt" in the script's directory itself.
