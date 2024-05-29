import re
import os
import json
import time
import requests
import warnings
import concurrent.futures
from typing import Iterable
from termcolor import colored
from urllib.error import HTTPError
from pytube import YouTube, Playlist
# from termcolor import colored as clrd
from http.client import IncompleteRead
from pytube.exceptions import PytubeError
from typing import Any, Dict, List, Optional, Tuple
warnings.filterwarnings("ignore", category=UserWarning)


BASE_DIR: str = 'U-YDT'
LOG_FILE_PATH: str = f'{BASE_DIR}/log/log.json'
def banner1() -> None:
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⡖⡄⠀⠀⢀⣀⢤⢤⢤⢤⢤⢤⣄⣄⣄⣠⣀⣀⣀⢀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⢀⣀⣤⣤⣤⣄⣀⠀⠀⣠⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⢀⢯⢢⢠⡪⡳⠽⠝⠝⠽⠽⠽⠽⠺⢺⢺⢾⢿⢾⣿⣿⣿⣶⣤⡀⠀⠀⠀⢀⢴⢕⠁", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⡀⠀⠀⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⡄⠀⠀⠀⠀⠀⢀⣀⣄⣤⣤⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⢝⢼⢸⠊⡄⠄⡀⢂⠐⠠⠠⠐⡈⡐⡐⡐⠔⣌⢜⢻⣿⣿⣳⢯⢆⠀⢠⢮⢣⠃", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠁⠉⠙⠻⢿⣿⣿⣿⣿⣿⡄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⢠⢰⢣⠳⠀⡀⢂⡰⡴⣬⡀⠅⢂⢐⣄⣆⠌⠌⡂⡃⣺⣟⣞⢾⣝⣗⠀⡇⠇⠁", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣦⡀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡿⠿⠋⢠⣾⣿⣿⣿⣿⣿⡏⣻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⢔⢱⢑⠕⡕⠀⡀⢲⢽⣝⣞⡆⠂⢄⣗⢷⢽⢽⠀⡂⠂⢼⡺⣮⣳⣳⡳⣕⢬", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⣷⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠋⠈⠀⠀⢀⣿⣿⣿⢛⢛⢛⢿⡇⣺⡟⡛⡛⠟⣿⣿⣧⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠢⡑⢅⢣⡃⠀⡀⠘⣗⣗⠗⠅⠂⡐⢽⢽⢽⠝⡀⢂⠁⡾⣝⣞⢾⢸⢹⢪⢯⢣", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⡇⠀⠀⢸⣶⣄⡀⠀⠀⠨⣿⣿⣿⡇", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⣺⣿⣿⡙⠇⡺⢹⣿⣿⡇⢽⣿⣿⡀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠈⠢⢱⢡⢃⢰⡀⠠⠀⢀⠈⡀⠂⠀⠄⠉⠁⠂⢐⠠⢀⣟⣞⢮⢯⢊⢎⠪⡪⠂", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⡇⠀⠀⢸⣿⠟⠃⠀⠀⠨⣿⣿⣿⡇", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡇⣺⣿⣿⣿⣦⣴⣿⣿⣿⡇⢽⣿⣿⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⡎⡢⡠⡠⡐⣀⡀⡄⡀⡁⡠⢈⢀⠁⢌⢡⢜⢮⣪⣫⡫⡢⠂⠑", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡇⠀⠀⠈⠀⠀⠀⠀⠀⢘⣿⣿⣿⠁", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠺⡿⡿⡿⡿⡿⡿⡿⡿⠇⣽⣿⠇⠀", 'green', 'on_black', ['bold']) + colored("⠠⣴⣲⢤⢤⣀⠀⠀⠀⠀⠀⠀⠱⡱⡱⡨⢢⢑⠔⡅⢇⢕⢱⢑⠕⡕⢍⠕⡕⡕⡕⡕⡕⡕⡕⠁", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⡿⠃⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣿⡿⠃⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠕⡝⡽⣽⣺⢽⣳⢦⢦⢄⡀⠀⠈⠊⠮⢸⡰⡑⡕⡱⡘⢌⢎⠪⡊⡎⡪⢢⠣⡑⢕⠱⠑", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠋⠁⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⢿⣿⣿⢿⠿⠻⠑⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠈⢐⠱⢱⢹⢝⢾⢽⢽⡪⡪⡣⡂⠀⠀⡀⡄⡬⢬⠬⡬⡢⡢⣕⢔⢔⢌⢔⡁⠊⠀⠀⠀⢀⢀⢀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠙⠙⠛⠙⠙⠈⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠈⠐⢡⠃⢇⢏⠟⡚⢎⢎⠎⡠⡪⡪⡪⡪⡣⣫⡪⣯⡻⡮⣯⡳⣕⢕⢭⢣⢂⠀⢜⢮⡳⣕⢕⢦⢄", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠈⠐⠀⠡⠈⠂⠈⢠⠣⡱⡑⡕⡕⡕⡵⣝⢮⡻⡺⣪⡻⡮⡧⡣⡣⡣⡀⢕⠵⣝⢮⣳⢯⣟⣦⣀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢈⠢⡑⢜⠌⡎⡪⡪⡳⡹⡸⡸⡸⡪⡪⡪⡪⡪⡂⠐⡑⢭⡻⣾⢽⣺⣺⣺⣲⡄", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⣤⡤⠀⠀⠀⠀⠀⠀⢠⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣶⣤⡀⠀⠀⠀⠀⣠⠒⠁⠀⢀⡠⠤⣤⣤⡤⠤⠤⠤⣤⣄⡀⠀⠀⠀⠀⢀⠤⠤⠤⠤⠤⣤⣤⠤⠤⠤⠴⡆", 'light_magenta', 'on_black', ['bold']) + colored("⠨⡂⡆⡒⡆⡇⡎⢜⢜⢜⢜⢼⢜⢞⢞⢮⢮⢮⡪⡀⠀⠈⠆⡹⠸⡝⡾⣞⣞⡾⡽⣧", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣄⠀⠀⡼⠁⠀⠀⡐⠁⠀⠀⢽⣿⡇⠀⠀⠀⠀⠙⣿⣶⡀⠀⠀⡏⠀⠀⠀⠀⠀⣿⣿⠇⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⡇⡪⢪⢪⢪⢪⡊⡎⡎⡎⡮⡫⡫⡳⡳⡳⡕⡕⠀⠀⠀⠀⠈⠈⠜⡘⠜⡝⢽⢽⢽⠅", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣆⣼⠁⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠸⣿⣿⡀⠀⠁⠀⠀⠀⠀⠀⣿⣿⡃⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⢱⠨⡊⡎⡎⡎⡆⡣⡣⡣⡫⡪⡪⡪⡪⡪⡪⡊⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠈", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠀⢸⡧⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠨⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠨⣿⣿⡂⠀⠀⠀⠀⠀⠀⠀⣿⣿⡃⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⢳⠨⡊⢎⢎⢎⢄⢕⢜⢜⢜⢜⢜⢜⢜⠜", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⣇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡅⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠱⡨⠢⡑⢕⢕⢕⢕⢕⢕⢕⢕⢕⠑", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⡄⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⢀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡅⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠈⠪⢐⢑⠔⡑⢜⢐⠕⡘⠔", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⠲⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠓⠓⠚⠚⠙⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠓⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠂⠑⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀[ V-U1.0.3 ]", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭| By Unkn0wn2603 |⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭", "green", 'on_black'))
    print("\n")
def banner2() -> None:
    print(colored("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⣤⡀⠀⠀⠀⠀⠀              ⢰⡄  ⢀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⡶⡿⡿⣿⣿⣿⣿⣾⣿⣷⡀⠀⠀                 ⢸⡺⢀⡮⠿⠽⠻⠻⠻⠟⠿⠿⡿⡿⡿⣿⣿⣿⣷⣦⡀  ⢀⣴⢏⢏⡦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠉⢛⣿⣿⣿⣿⠀⠀     ⣠⣴⣶⣶⣶⣶⣦⣄    ⠂⢯⡳⡃⠑⠄⠂⡁⢂⠡⠨⢐⢐⠰⡘⡴⣙⣿⣿⣿⣿⡄⢀⡿⢕⠁
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡏⠀⢀⠀⠀⠀⠁⣿⣿⡄⠀⠀⠀⠀⠀⠀⠘⠛⠋⠉⠀⠀    ⠀⣾⣿⣿⣿ ⢸⣿⣿⣿⣧  ⡠⡪⡎⣗ ⠡⢰⣽⣾⣔⠠⢈⣴⣶⣦⠊⡐⠡⣿⣿⡿⣷⣇⡪⠊
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⢸⣿⡦⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠈⠀⠀⣿⣿⣿⣍⠃⠘⣩⣿⣿⣿ ⢀⠣⢣⠣⡚ ⠄⢿⢿⣽⠗ ⢺⣿⣽⡾⠂⢂⢁⣿⣟⣿⡳⣿⢽⡦
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡇⠀⠘⠉⠀⠀⠀⣿⣿⠇⠀⠤⣤⣤⡄⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⢻⣿⣿⣿⣓⣚⣿⣿⣿⡟  ⠑⠅⣎⢎⢠⠠ ⠍⠑⠈⡀⠂⠙⠚⢁⠁⡂⢸⣯⣟⣷⠹⡸⡱⠝
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣶⣶⣶⣶⣶⣶⣿⠏⠀⠀⠨⣿⣿⡂⠀⠀⠀⠀⠀⢽⡇⠀⠀⠀⠀ ⠙⠻⠿⠿⠿⠿⠟⠋    ⢱⢱⠥⡡⡠⡐⣀⢂⣀⢄⣁⡈⣀⣐⡣⣫⢷⣻⡺⡕⠈⠂⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠛⠋⠀⠀⠀⠀⠨⣿⣿⡂⠀⠀⠀⠀⠀⢽⡇⠀⠀⠀⠀     ⡶⣶⣶⣴⣄⣀   ⠈⠺⡜⡜⡸⡨⡢⡣⡪⡪⡢⡣⡣⡪⡪⡳⡹⣪⢺⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⡂⠀⠀⠀⠀⠀⢽⡇⠀⠀⠀⠀     ⠨⠹⡻⡿⣿⣿⣿⣯⣖⣄⡀⠈⠘⠊⠎⠮⠜⢌⣊⡊⠪⠊⢎⠪⠸⡘⠌⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡆⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀      ⠈⠈⡪⢫⢻⢻⢿⡺⣺⡪⢀⢔⡜⣎⢯⡫⣗⡷⣽⡯⣟⡮⡮⡦⡀ ⢠⢦⣖⢦⢄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣤⣀⣀⣠⠾⠋⠀⠀⠀⠀⠀⠀          ⠁⠘⠈⠆⠕⠁⡪⡕⡕⡕⣇⢿⣻⣿⣳⢿⣻⣽⡳⣝⣝⠄⡹⣽⢾⢽⣽⣷⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               ⢰⠱⡘⢜⠜⡬⡹⢝⢟⢎⢯⢳⠳⡝⡎⡎⡇⠨⡊⢿⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢶⣦⣀⠀⠀⠀⢀⡴⠋⠁⢀⣠⡤⣤⣤⡤⠤⠤⣤⣄⣀⠀⠀⠀⠀⣠⡤⠤⠤⠤⣤⣤⡤⠤⠤⣴   ⡇⡆⡧⣪⢦⢣⢳⢱⢝⡾⡽⣽⣳⢯⢯⡂ ⠘⠔⡱⠻⡿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⡀⢠⡞⠁⠀⣐⠉⠀⠀⣿⣿⡇⠀⠀⠀⠙⣿⣷⣄⠀⢸⠁⠀⠀⠀⠀⣿⣿⡇⠀⠀⠈    ⢇⢎⢎⢮⢳⡣⡣⡳⣹⣺⢽⡳⡽⡽⡵⠁    ⠑⠑⠩⠋⠟⠻⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣶⡿⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⢘⣿⣷⡂⠀⠃⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀    ⠘⣆⠣⡣⡳⣕⠱⡱⡱⣏⢷⠽⣝⢞⠊
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⢐⣿⣿⡂⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀     ⠘⢜⠌⡎⢎⢇⢯⢺⢕⡝⣝⢜⠊
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⡂⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀       ⠑⢜⢌⠪⡊⢎⠪⡊⠆⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣂⠀⠀⠀⠀⠀⠀⢀⣿⣿⣇⣀⣀⣤⡾⠿⠃⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣇⠀⠀⠀          ⠁⠁⠁⠁        Version : U1.0.3
          """, "cyan", attrs=['bold']))
    print("\n")
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛", "green", 'on_black', attrs=['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", "red", 'on_black', attrs=['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭| By Unkn0wn2603 |⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭", "green", 'on_black', attrs=['bold']))
    print("\n")
def banner() -> None:
    if os.name == 'nt':
        os.system('cls')
        banner1()
    elif os.name == 'posix':
        os.system('clear')
        banner2()
    else:
        banner1()
def select_stream(yt: YouTube, quality: str) -> Optional[Any]:
    filters: Dict[str, Any] = {
        "audio": lambda: yt.streams.filter(only_audio=True).order_by('abr').desc().first(),
        "128kbps": lambda: yt.streams.filter(only_audio=True, abr="128kbps").first(),
        "160kbps": lambda: yt.streams.filter(only_audio=True, abr="160kbps").first(),
        "360p": lambda: yt.streams.filter(res="360p", progressive=True).first(),
        "720p": lambda: yt.streams.filter(res="720p", progressive=True).first(),
        "1080p": lambda: yt.streams.filter(res="1080p").first(),
        "2k": lambda: yt.streams.filter(res="1440p").first(),
        "4k": lambda: yt.streams.filter(res="2160p").first(),
        "8k": lambda: yt.streams.filter(res="4320p").first(),
        "highest": lambda: yt.streams.get_highest_resolution()
    }
    return filters.get(quality, filters["highest"])()
def quality_input() -> str:
    quality_map: Dict[str, str] = {
        '1': 'audio',
        '2': '128kbps',
        '3': '160kbps',
        '4': '360p',
        '5': '720p',
        '6': '1080p',
        '7': '2k',
        '8': '4k',
        '9': '8k',
        '10': 'highest'
    }
    print(colored('        [i] Select the download quality:', 'cyan', attrs=['bold']))
    options: List[str] = [
        "Audio only (best quality)",
        "Audio 128kbps",
        "Audio 160kbps",
        "360p",
        "720p",
        "1080p",
        "2k",
        "4k",
        "8k",
        "Highest available quality"
    ]
    for i, desc in enumerate(options, start=1):
        print(colored(f'        [{i}] {desc}', 'cyan'))
    quality_choice: str = input(colored('        [?] Enter the number of your choice: ', 'cyan', attrs=['bold'])).strip()
    return quality_map.get(quality_choice, 'highest')
def load_json(file_path: str) -> Optional[Any]:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None

def save_json(file_path: str, data: Any) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
def update_log(log_file: str, log_data: Dict[str, Any]) -> None:
    data: List[Dict[str, Any]] = load_json(log_file) or []
    data.append(log_data)
    save_json(log_file, data)


"""################################################################################################################################################################
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
################################################################################################################################################################"""


def download_single_video(video_url: str) -> None:
    banner()
    quality: str = quality_input()
    try:
        yt: YouTube = YouTube(video_url)
        print(colored(f'        [i] Downloading video: {yt.title} ({quality})', color="blue", attrs=["bold"]))
        download_dir: str = os.path.join(BASE_DIR, 'videos', quality)
        os.makedirs(download_dir, exist_ok=True)
        log_dir: str = os.path.join(BASE_DIR, 'videos', 'log')
        os.makedirs(log_dir, exist_ok=True)
        stream: Optional[Any] = select_stream(yt, quality)
        if stream:
            log_data: Dict[str, Any] = {
                'title': yt.title,
                'quality': quality,
                'video_url': video_url,
                'duration': yt.length,
                'author': yt.author,
                'views': yt.views,
                'publish_date': str(yt.publish_date),
                'others': {
                    'description': yt.description,
                    'keywords': yt.keywords,
                    'thumbnail_url': yt.thumbnail_url,
                    'rating': yt.rating
                }
            }
            log_file_path1: str = os.path.join(log_dir, 'all_log.json')
            log_file_path2: str = os.path.join(log_dir, f'{quality}_log.json')
            update_log(log_file_path1, log_data)
            update_log(log_file_path2, log_data)
            stream.download(output_path=download_dir)
            print(colored(f'        [i] Download complete: {yt.title}', color="green", attrs=["bold"]))
        else:
            print(colored(f'        [!] No stream found for {yt.title} with quality {quality}', color="red", attrs=["bold"]))
    except Exception as e:
        print(colored(f'        [!] Failed to download {video_url}: {e}', color="red", attrs=["bold"]))

"""################################################################################################################################################################
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
################################################################################################################################################################"""


def sanitize_filename(filename: str) -> str:
    # Remove or replace characters that are invalid in filenames
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Optionally, truncate the filename to a reasonable length
    return filename[:200]

def file_exists(folder: str, filename: str, expected_size: int) -> bool:
    file_path = os.path.join(folder, filename)
    if os.path.exists(file_path):
        if os.path.getsize(file_path) == expected_size:
            return True
        else:
            print(colored(f'        [!] File {filename} exists but size does not match. It will be overwritten.', color="yellow", attrs=["bold"]))
    return False

def playlist_download_video(video: Any, folder: str, idx: int, total_videos: int, log_file: str, log_data: Dict[str, List[str]], quality: str, max_retries: int = 3) -> None:
    for attempt in range(max_retries):
        try:
            yt: YouTube = YouTube(video.watch_url)
            print(colored(f'        [i] Downloading video ({idx}/{total_videos}): {video.title} ({quality})', color="blue", attrs=["bold"]))
            stream: Optional[Any] = select_stream(yt, quality)
            if stream:
                # Sanitize the filename to avoid invalid characters and truncation issues
                safe_title = sanitize_filename(video.title)
                filename = f'{idx:03d} - {safe_title}.mp4'
                file_path = os.path.join(folder, filename)
                
                # Check if file already exists with the same title and size
                if file_exists(folder, filename, stream.filesize):
                    print(colored(f'        [i] File already exists: {filename}', color="green", attrs=["bold"]))
                    log_data['completed'].append(video.watch_url)
                    save_json(log_file, log_data)
                    return
                
                # Download the video
                stream.download(output_path=folder, filename=filename)
                print(colored(f'        [i] Download complete: {video.title}', color="green", attrs=["bold"]))
                log_data['completed'].append(video.watch_url)
                save_json(log_file, log_data)
                return
            else:
                print(colored(f'        [!] No stream found for {video.title} with quality {quality}', color="red", attrs=["bold"]))
                if video.watch_url not in log_data['not_completed']:
                    log_data['not_completed'].append(video.watch_url)
                save_json(log_file, log_data)
                return
        except IncompleteRead as e:
            print(colored(f'        [!] IncompleteRead error on attempt {attempt + 1} for {video.title}: {e}', color="yellow", attrs=["bold"]))
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait a bit before retrying
        except Exception as e:
            print(colored(f'        [!] Failed to download {video.title} on attempt {attempt + 1}: {e}', color="red", attrs=["bold"]))
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait a bit before retrying
    # If all attempts fail, log the failure
    if video.watch_url not in log_data['not_completed']:
        log_data['not_completed'].append(video.watch_url)
    save_json(log_file, log_data)


"""################################################################################################################################################################
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
################################################################################################################################################################"""

def playlist_video_exists(video: Any, log_data: Dict[str, List[str]]) -> bool:
    return video.watch_url in log_data['completed']
def playlist_create_directories(playlist_title: str, quality: str) -> Tuple[str, str, str]:
    base_dir: str = 'playlist'
    playlist_folder: str = os.path.join(BASE_DIR, base_dir, playlist_title)
    quality_folder: str = os.path.join(playlist_folder, quality)
    log_folder: str = os.path.join(playlist_folder, 'download_data')
    os.makedirs(quality_folder, exist_ok=True)
    os.makedirs(log_folder, exist_ok=True)
    return playlist_folder, quality_folder, log_folder
def playlist_get_video_links(playlist_url: str, links_file: str) -> List[str]:
    links_data: Optional[Dict[str, Any]] = load_json(links_file)
    if links_data and 'video_urls' in links_data:
        return links_data['video_urls']
    playlist: Playlist = Playlist(playlist_url)
    video_urls: List[str] = [video.watch_url for video in playlist.videos]
    save_json(links_file, {'video_urls': video_urls})
    return video_urls



def download_playlist_videos(playlist_url: str) -> None:
    banner()
    playlist: Playlist = Playlist(playlist_url)
    print(colored(f'        [i] Downloading playlist: {playlist.title}', color="magenta", attrs=["bold"]))
    quality: str = quality_input()
    playlist_folder, quality_folder, log_folder = playlist_create_directories(playlist.title, quality)
    links_file: str = os.path.join(log_folder, 'links.json')
    log_file: str = os.path.join(log_folder, f'{quality}.json')
    video_urls: List[str] = playlist_get_video_links(playlist_url, links_file)
    log_data: Dict[str, List[str]] = load_json(log_file) or {'completed': [], 'not_completed': []}
    total_videos: int = len(video_urls)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(playlist_download_video, YouTube(video_url), quality_folder, idx, total_videos, log_file, log_data, quality)
            for idx, video_url in enumerate(video_urls, start=1) if not playlist_video_exists(YouTube(video_url), log_data)
        ]
        for future in concurrent.futures.as_completed(futures):
            future.result()
    print(colored('        [i] All downloads complete!', 'green'))



"""################################################################################################################################################################
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
################################################################################################################################################################"""


def channel_load_log(log_file: str) -> Dict[str, List[str]]:
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return json.load(f)
    return {'completed': [], 'not_completed': []}
def channel_select_stream(yt: YouTube, quality: str) -> Optional[Any]:
    return select_stream(yt, quality)
def channel_save_log(log_file: str, log_data: Dict[str, List[str]]) -> None:
    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=4)
def download_channel_video(video_url: str, folder: str, idx: int, total_videos: int, log_file: str, log_data: Dict[str, List[str]], quality: str) -> None:
    try:
        yt: YouTube = YouTube(video_url)
        print(colored(f'        [i] Downloading video ({idx}/{total_videos}): {yt.title} ({quality})', color="blue", attrs=["bold"]))
        stream: Optional[Any] = channel_select_stream(yt, quality)
        if stream:
            stream.download(output_path=folder)
            print(colored(f'        [i] Download complete: {yt.title} ', color="green", attrs=["bold"]))
            log_data['completed'].append(video_url)
        else:
            print(colored(f'        [!] No stream found for {yt.title} with quality {quality}', color="red", attrs=["bold"]))
            if video_url not in log_data['not_completed']:
                log_data['not_completed'].append(video_url)
        channel_save_log(log_file, log_data)
    except Exception as e:
        print(colored(f'        [!] Failed to download {yt.title}: {e} ', color="red", attrs=["bold"]))
        if video_url not in log_data['not_completed']:
            log_data['not_completed'].append(video_url)
        channel_save_log(log_file, log_data)
def channel_get_video_urls(api_key: str, channel_id: str, channel_name: str) -> List[str]:
    base_video_url: str = 'https://www.youtube.com/watch?v='
    base_search_url: str = 'https://www.googleapis.com/youtube/v3/search?'
    links_file: str = os.path.join(BASE_DIR, 'channels', channel_name, 'download_data', 'links.json')
    if os.path.exists(links_file):
        with open(links_file, 'r') as f:
            data = json.load(f)
            print(colored('        [i] There is info and links of this channel in local db, not fetching from google:', 'cyan', attrs=['bold']))
            return data['video_urls']
    first_url: str = f'{base_search_url}key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50'
    video_urls: List[str] = []
    url: str = first_url
    while True:
        response = requests.get(url).json()
        for item in response['items']:
            if item['id']['kind'] == "youtube#video":
                video_urls.append(base_video_url + item['id']['videoId'])
        try:
            next_page_token: str = response['nextPageToken']
            url = f'{first_url}&pageToken={next_page_token}'
        except KeyError:
            break
    os.makedirs(os.path.join(BASE_DIR, 'channels', channel_name, 'download_data'), exist_ok=True)
    with open(links_file, 'w') as f:
        json.dump({'video_urls': video_urls}, f, indent=4)
    print(colored('        [i] Fetching from google info and links of this channel:', 'cyan', attrs=['bold']))
    return video_urls
def channel_video_exists(video_url: str, log_data: Dict[str, List[str]]) -> bool:
    return video_url in log_data['completed']
def download_channel(api_key: str, channel_id: str, channel_name: str) -> None:
    banner()
    video_urls: List[str] = channel_get_video_urls(api_key, channel_id, channel_name)
    log_folder: str = os.path.join(BASE_DIR, 'channels', channel_name, 'download_data')
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    quality: str = quality_input()
    log_file: str = os.path.join(log_folder, f'{quality}.json')
    log_data: Dict[str, List[str]] = channel_load_log(log_file)
    if log_data['completed'] or log_data['not_completed']:
        print(colored('        [i] Some records found for this channel and quality.', 'cyan'))
        print(colored('        [i] There are some incomplete downloads.', 'cyan'))
        print(colored('        [i] What would you like to do?', 'cyan'))
        print(colored('        [1] Download only incomplete items from the JSON database.', 'cyan'))
        print(colored('        [2] Recheck all videos from Google data.', 'cyan'))
        choice: str = input(colored("        [?] Enter your choice (default: 1): ", 'blue')).strip()
        if choice == '2':
            log_data = {'completed': [], 'not_completed': []}
        else:
            print(colored('        [i] Downloading incomplete items from the JSON database.', 'cyan'))
    else:
        print(colored('        [i] No downloading records found for this channel and quality.', 'cyan'))
        print(colored('        [i] Proceeding to fetch video URLs from Google data.', 'cyan'))
    total_videos: int = len(video_urls)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for idx, video_url in enumerate(video_urls, start=1):
            if channel_video_exists(video_url, log_data):
                print(colored(f'        [~] Skipping already downloaded video ({idx}/{total_videos}): {video_url} ',
                              color="yellow", attrs=["bold"]))
                continue
            futures.append(
                executor.submit(download_channel_video, video_url, os.path.join(BASE_DIR, 'channels', channel_name, quality), idx, total_videos, log_file, log_data, quality))
        for future in concurrent.futures.as_completed(futures):
            future.result()
    print(colored('        [i] All downloads complete!', 'green'))
    

"""################################################################################################################################################################
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
################################################################################################################################################################"""


def normalize_video_url(url: str) -> str:
    base_url: str = 'https://www.youtube.com/watch?v='
    if len(url) == 11:
        return base_url + url
    if not url.startswith('https://www.youtube.com/'):
        if url.startswith('https://'):
            url = url.replace('https://', 'https://www.')
        elif url.startswith('youtube.com/'):
            url = 'https://www.' + url
        else:
            url = 'https://www.youtube.com/' + url.split('youtube.com/')[1]
    video_id_index: int = url.find('v=')
    if video_id_index != -1:
        base_url = url[:video_id_index + len('v=')]
        video_id: str = url[video_id_index + len('v='):]
        end_of_id_index: int = video_id.find('&')
        if end_of_id_index != -1:
            video_id = video_id[:end_of_id_index]
        return base_url + video_id
    return url
def fetch_video_title(normalized_url: str) -> Optional[str]:
    try:
        video: YouTube = YouTube(normalized_url)
        return video.title
    except (PytubeError, HTTPError) as e:
        print(f"Failed to fetch video title: {e}")
        return None
def normalize_playlist_url(url: str) -> str:
    base_url: str = 'https://www.youtube.com/playlist?list='
    if url.startswith('PL'):
        return base_url + url
    if not url.startswith('https://www.youtube.com/'):
        if url.startswith('https://'):
            url = url.replace('https://', 'https://www.')
        elif url.startswith('youtube.com/'):
            url = 'https://www.' + url
        else:
            url = 'https://www.youtube.com/' + url.split('youtube.com/')[1]
    playlist_id_index: int = url.find('list=')
    if playlist_id_index != -1:
        base_url = url[:playlist_id_index + len('list=')]
        playlist_id: str = url[playlist_id_index + len('list='):]
        end_of_id_index: int = playlist_id.find('&')
        if end_of_id_index != -1:
            playlist_id = playlist_id[:end_of_id_index]
        return base_url + playlist_id
    return url
def fetch_playlist_title(normalized_url: str) -> Optional[str]:
    try:
        playlist: Playlist = Playlist(normalized_url)
        return playlist.title
    except (PytubeError, HTTPError) as e:
        print(f"Failed to fetch playlist title: {e}")
        return None
def load_log() -> Dict[str, Any]:
    return load_json(LOG_FILE_PATH) or {}
def save_log(log: Dict[str, Any]) -> None:
    save_json(LOG_FILE_PATH, log)


"""################################################################################################################################################################
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
################################################################################################################################################################"""


def start_u_ydt() -> None:
    log: Dict[str, Any] = load_log()
    print(colored("        [i] What would you like to download?", 'blue'))
    print(colored("        [1] Channel", 'cyan'))
    print(colored("        [2] Playlist", 'cyan'))
    print(colored("        [3] Single Content", 'cyan'))
    print(colored("        [4] Check Previous", 'cyan'))
    choice: str = input(colored("        [~] Choose an option: ", 'yellow')).strip()
    if choice == '1':
        api_key, channel_id, channel_name = handle_channel_input(log)
        save_log(log)
        download_channel(api_key, channel_id, channel_name)
    elif choice == '2':
        playlist_url: str = input(colored("        [~] Enter playlist URL or ID: ", 'yellow')).strip()
        normalized_url: str = normalize_playlist_url(playlist_url)
        playlist_title: str = handle_playlist_input(log, normalized_url)
        save_log(log)
        download_playlist_videos(normalized_url)
    elif choice == '3':
        single_content_url: str = input(colored("        [~] Enter single content URL or ID: ", 'yellow')).strip()
        normalized_url: str = normalize_video_url(single_content_url)
        video_title: str = handle_single_content_input(log, normalized_url)
        save_log(log)
        download_single_video(normalized_url)
    elif choice == '4':
        check_previous_downloads(log)
def handle_channel_input(log: Dict[str, Any]) -> Tuple[str, str, str]:
    if 'api_keys' in log and log['api_keys']:
        api_key: str = select_api_key(log)
    else:
        api_key = input(colored("        [~] Enter new API key: ", 'yellow')).strip()
        log['api_keys'] = [api_key]
    channel_id: str = input(colored("        [~] Enter channel ID: ", 'yellow')).strip()
    if 'channels' in log and channel_id in [c['channel_id'] for c in log['channels']]:
        channel: Dict[str, str] = next(c for c in log['channels'] if c['channel_id'] == channel_id)
        channel_name: str = channel['channel_name']
        print(colored(f"        [~] Channel exists in log, named: {channel_name}", 'yellow'))
    else:
        channel_name = input(colored("        [~] Enter channel name: ", 'yellow')).strip()
        log.setdefault('channels', []).append({'channel_id': channel_id, 'channel_name': channel_name})
    return api_key, channel_id, channel_name
def select_api_key(log: Dict[str, Any]) -> str:
    print(colored("        [i] Available API keys:", 'blue'))
    for i, api_key in enumerate(log['api_keys'], 1):
        print(colored(f"        [{i}] {api_key}", 'cyan'))
    api_choice: str = input(colored("        [~] Choose an API key or enter 'new' to use a new API key: ", 'yellow')).strip()
    if api_choice.isdigit() and 1 <= int(api_choice) <= len(log['api_keys']):
        return log['api_keys'][int(api_choice) - 1]
    else:
        api_key: str = input(colored("        [~] Enter new API key: ", 'yellow')).strip()
        log.setdefault('api_keys', []).append(api_key)
        return api_key
def handle_playlist_input(log: Dict[str, Any], normalized_url: str) -> str:
    if 'playlists' in log and normalized_url in [p['playlist_url'] for p in log['playlists']]:
        playlist: Dict[str, str] = next(p for p in log['playlists'] if p['playlist_url'] == normalized_url)
        playlist_title: str = playlist['playlist_title']
        print(colored(f"        [~] Playlist exists in log, named: {playlist_title}", 'yellow'))
    else:
        playlist_title: Optional[str] = fetch_playlist_title(normalized_url)
        if playlist_title is None:
            playlist_title = "Unknown Playlist"
        log.setdefault('playlists', []).append({'playlist_url': normalized_url, 'playlist_title': playlist_title})
    return playlist_title
def handle_single_content_input(log: Dict[str, Any], normalized_url: str) -> str:
    if 'single_contents' in log and normalized_url in [v['video_url'] for v in log['single_contents']]:
        video: Dict[str, str] = next(v for v in log['single_contents'] if v['video_url'] == normalized_url)
        video_title: str = video['video_title']
        print(colored(f"        [~] The content exists in log, named: {video_title}", 'yellow'))
    else:
        video_title: Optional[str] = fetch_video_title(normalized_url)
        if video_title is None:
            video_title = "Unknown Video"
        log.setdefault('single_contents', []).append({'video_url': normalized_url, 'video_title': video_title})
    return video_title
def check_previous_downloads(log: Dict[str, Any]) -> None:
    print(colored("        [i] Which type of previous downloads do you want to check?", 'blue'))
    print(colored("        [1] Videos", 'cyan'))
    print(colored("        [2] Playlists", 'cyan'))
    print(colored("        [3] Channels", 'cyan'))
    print(colored("        [4] All", 'cyan'))
    check_choice: str = input(colored("        [~] Choose an option: ", 'yellow')).strip()
    if check_choice == '1':
        handle_check_videos(log)
    elif check_choice == '2':
        handle_check_playlists(log)
    elif check_choice == '3':
        handle_check_channels(log)
    elif check_choice == '4':
        handle_check_all(log)
def handle_check_videos(log: Dict[str, Any]) -> None:
    if 'single_contents' in log:
        print(colored("        [i] Previous video downloads:", 'blue'))
        for i, video in enumerate(log['single_contents'], 1):
            print(colored(f"                [{i}] {video['video_title']} ({video['video_url']})", 'cyan'))
        video_choice: int = int(input(colored("        [~] Enter the number of the video to download: ", 'yellow')).strip())
        download_single_video(log['single_contents'][video_choice - 1]['video_url'])
def handle_check_playlists(log: Dict[str, Any]) -> None:
    if 'playlists' in log:
        print(colored("        [i] Previous playlist downloads:", 'blue'))
        for i, playlist in enumerate(log['playlists'], 1):
            print(colored(f"                [{i}] {playlist['playlist_title']} ({playlist['playlist_url']})", 'cyan'))
        playlist_choice: int = int(input(colored("        [~] Enter the number of the playlist to download: ", 'yellow')).strip())
        download_playlist_videos(log['playlists'][playlist_choice - 1]['playlist_url'])
def handle_check_channels(log: Dict[str, Any]) -> None:
    if 'channels' in log:
        print(colored("        [i] Previous channel downloads:", 'blue'))
        for i, channel in enumerate(log['channels'], 1):
            print(colored(f"                [{i}] {channel['channel_name']} ({channel['channel_id']})", 'cyan'))
        channel_choice: int = int(input(colored("        [~] Enter the number of the channel to download: ", 'yellow')).strip())
        channel: Dict[str, str] = log['channels'][channel_choice - 1]
        api_key: str = select_api_key(log)
        save_log(log)
        download_channel(api_key, channel['channel_id'], channel['channel_name'])
def handle_check_all(log: Dict[str, Any]) -> None:
    sn: int = 1
    if 'single_contents' in log:
        print(colored("        [i] Previous video downloads:", 'blue'))
        for video in log['single_contents']:
            print(colored(f"                [{sn}] {video['video_title']} ({video['video_url']})", 'cyan'))
            sn += 1
    if 'playlists' in log:
        print(colored("        [i] Previous playlist downloads:", 'blue'))
        for playlist in log['playlists']:
            print(colored(f"                [{sn}] {playlist['playlist_title']} ({playlist['playlist_url']})", 'cyan'))
            sn += 1
    if 'channels' in log:
        print(colored("        [i] Previous channel downloads:", 'blue'))
        for channel in log['channels']:
            print(colored(f"                [{sn}] {channel['channel_name']} ({channel['channel_id']})", 'cyan'))
            sn += 1
    prev_choice: int = int(input(colored("        [~] Enter the number of the download to complete: ", 'yellow')).strip())
    if prev_choice <= len(log.get('single_contents', [])):
        download_single_video(log['single_contents'][prev_choice - 1]['video_url'])
    elif prev_choice <= len(log.get('single_contents', [])) + len(log.get('playlists', [])):
        download_playlist_videos(log['playlists'][prev_choice - len(log.get('single_contents', [])) - 1]['playlist_url'])
    else:
        index: int = prev_choice - len(log.get('single_contents', [])) - len(log.get('playlists', [])) - 1
        channel_info: Dict[str, str] = log['channels'][index]
        api_key: str = select_api_key(log)
        save_log(log)
        download_channel(api_key, channel_info['channel_id'], channel_info['channel_name'])
def main() -> None:
    while True:
        try:
            banner()
            start_u_ydt()
        except Exception as e:
            input(colored(f"\n        [!] Error Occurred, Details: {e}", 'red'))
        except KeyboardInterrupt:
            input(colored("\n        [?] Press Enter to exit: ", 'red'))
            break
        if input(colored("\n        [?] Want to do some more things (y/n): ", 'red')).strip().lower() != 'y':
            break
if __name__ == "__main__":
    main()
