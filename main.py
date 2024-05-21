import os
import json
import requests
import concurrent.futures
from pytube import YouTube
from pytube import Playlist
from termcolor import colored
from urllib.error import HTTPError
from pytube.exceptions import PytubeError
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

BASE_DIR = 'U-YDT'
LOG_FILE_PATH = f'{BASE_DIR}/log/log.json'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def banner():
    clear_terminal()
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⡖⡄⠀⠀⢀⣀⢤⢤⢤⢤⢤⢤⣄⣄⣄⣠⣀⣀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⢀⣀⣤⣤⣤⣄⣀⠀⠀⣠⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⢀⢯⢢⢠⡪⡳⠽⠝⠝⠽⠽⠽⠽⠺⢺⢺⢾⢿⢾⣿⣿⣿⣶⣤⡀⠀⠀⠀⢀⢴⢕⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⡀⠀⠀⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⡄⠀⠀⠀⠀⠀⢀⣀⣄⣤⣤⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⢝⢼⢸⠊⡄⠄⡀⢂⠐⠠⠠⠐⡈⡐⡐⡐⠔⣌⢜⢻⣿⣿⣳⢯⢆⠀⢠⢮⢣⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠁⠉⠙⠻⢿⣿⣿⣿⣿⣿⡄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⢠⢰⢣⠳⠀⡀⢂⡰⡴⣬⡀⠅⢂⢐⣄⣆⠌⠌⡂⡃⣺⣟⣞⢾⣝⣗⠀⡇⠇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣦⡀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡿⠿⠋⢠⣾⣿⣿⣿⣿⣿⡏⣻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⢔⢱⢑⠕⡕⠀⡀⢲⢽⣝⣞⡆⠂⢄⣗⢷⢽⢽⠀⡂⠂⢼⡺⣮⣳⣳⡳⣕⢬⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⣷⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠋⠈⠀⠀⢀⣿⣿⣿⢛⢛⢛⢿⡇⣺⡟⡛⡛⠟⣿⣿⣧⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠢⡑⢅⢣⡃⠀⡀⠘⣗⣗⠗⠅⠂⡐⢽⢽⢽⠝⡀⢂⠁⡾⣝⣞⢾⢸⢹⢪⢯⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⡇⠀⠀⢸⣶⣄⡀⠀⠀⠨⣿⣿⣿⡇", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⣺⣿⣿⡙⠇⡺⢹⣿⣿⡇⢽⣿⣿⡀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠈⠢⢱⢡⢃⢰⡀⠠⠀⢀⠈⡀⠂⠀⠄⠉⠁⠂⢐⠠⢀⣟⣞⢮⢯⢊⢎⠪⡪⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⡇⠀⠀⢸⣿⠟⠃⠀⠀⠨⣿⣿⣿⡇", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡇⣺⣿⣿⣿⣦⣴⣿⣿⣿⡇⢽⣿⣿⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⡎⡢⡠⡠⡐⣀⡀⡄⡀⡁⡠⢈⢀⠁⢌⢡⢜⢮⣪⣫⡫⡢⠂⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡇⠀⠀⠈⠀⠀⠀⠀⠀⢘⣿⣿⣿⠁", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠺⡿⡿⡿⡿⡿⡿⡿⡿⠇⣽⣿⠇⠀", 'green', 'on_black', ['bold']) + colored("⠠⣴⣲⢤⢤⣀⠀⠀⠀⠀⠀⠀⠱⡱⡱⡨⢢⢑⠔⡅⢇⢕⢱⢑⠕⡕⢍⠕⡕⡕⡕⡕⡕⡕⡕⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⡿⠃⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣿⡿⠃⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠕⡝⡽⣽⣺⢽⣳⢦⢦⢄⡀⠀⠈⠊⠮⢸⡰⡑⡕⡱⡘⢌⢎⠪⡊⡎⡪⢢⠣⡑⢕⠱⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠋⠁⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⢿⣿⣿⢿⠿⠻⠑⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠈⢐⠱⢱⢹⢝⢾⢽⢽⡪⡪⡣⡂⠀⠀⡀⡄⡬⢬⠬⡬⡢⡢⣕⢔⢔⢌⢔⡁⠊⠀⠀⠀⢀⢀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠙⠙⠛⠙⠙⠈⠀⠀⠀⠀⠀", 'red', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'green', 'on_black', ['bold']) + colored("⠀⠀⠀⠈⠐⢡⠃⢇⢏⠟⡚⢎⢎⠎⡠⡪⡪⡪⡪⡣⣫⡪⣯⡻⡮⣯⡳⣕⢕⢭⢣⢂⠀⢜⢮⡳⣕⢕⢦⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠈⠐⠀⠡⠈⠂⠈⢠⠣⡱⡑⡕⡕⡕⡵⣝⢮⡻⡺⣪⡻⡮⡧⡣⡣⡣⡀⢕⠵⣝⢮⣳⢯⣟⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢈⠢⡑⢜⠌⡎⡪⡪⡳⡹⡸⡸⡸⡪⡪⡪⡪⡪⡂⠐⡑⢭⡻⣾⢽⣺⣺⣺⣲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⣤⡤⠀⠀⠀⠀⠀⠀⢠⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣶⣤⡀⠀⠀⠀⠀⣠⠒⠁⠀⢀⡠⠤⣤⣤⡤⠤⠤⠤⣤⣄⡀⠀⠀⠀⠀⢀⠤⠤⠤⠤⠤⣤⣤⠤⠤⠤⠴⡆", 'light_magenta', 'on_black', ['bold']) + colored("⠨⡂⡆⡒⡆⡇⡎⢜⢜⢜⢜⢼⢜⢞⢞⢮⢮⢮⡪⡀⠀⠈⠆⡹⠸⡝⡾⣞⣞⡾⡽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣄⠀⠀⡼⠁⠀⠀⡐⠁⠀⠀⢽⣿⡇⠀⠀⠀⠀⠙⣿⣶⡀⠀⠀⡏⠀⠀⠀⠀⠀⣿⣿⠇⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⡇⡪⢪⢪⢪⢪⡊⡎⡎⡎⡮⡫⡫⡳⡳⡳⡕⡕⠀⠀⠀⠀⠈⠈⠜⡘⠜⡝⢽⢽⢽⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣆⣼⠁⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠸⣿⣿⡀⠀⠁⠀⠀⠀⠀⠀⣿⣿⡃⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⢱⠨⡊⡎⡎⡎⡆⡣⡣⡣⡫⡪⡪⡪⡪⡪⡪⡊⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠀⢸⡧⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠨⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⠨⣿⣿⡂⠀⠀⠀⠀⠀⠀⠀⣿⣿⡃⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⢳⠨⡊⢎⢎⢎⢄⢕⢜⢜⢜⢜⢜⢜⢜⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⣇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⠀⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡅⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠱⡨⠢⡑⢕⢕⢕⢕⢕⢕⢕⢕⢕⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⡄⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡇⠀⠀⠀⢀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡅⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠈⠪⢐⢑⠔⡑⢜⢐⠕⡘⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⠲⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠓⠓⠚⠚⠙⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠓⠀⠀⠀", 'light_magenta', 'on_black', ['bold']) + colored("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠂⠑⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀[ V-U_Beta ]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", 'light_cyan', 'on_black', ['bold']))
    # print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛", "green", 'on_black')) 
    # print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", "red", 'on_black'))
    # print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭| By Unkn0wn2603 |⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭", "green", 'on_black'))
    print(colored("⠀⠀⠀⠀⠀⠀⠀⠀⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭| By Unkn0wn2603 |⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭", "green", 'on_black'))
    print("\n")

"""#################################################################################################################################
####################################################################################################################################
########                                                                                                                    ########
######        .oooooo.     .oooooo.   ooooo      ooo  .oooooo..o ooooooooooooo oooooooooooo ooooo      ooo ooooooooooooo      ######
######       d8P'  `Y8b   d8P'  `Y8b  `888b.     `8' d8P'    `Y8 8'   888   `8 `888'     `8 `888b.     `8' 8'   888   `8      ######
######      888          888      888  8 `88b.    8  Y88bo.           888       888          8 `88b.    8       888           ######
######      888          888      888  8   `88b.  8   `"Y8888o.       888       888oooo8     8   `88b.  8       888           ######
######      888          888      888  8     `88b.8       `"Y88b      888       888    "     8     `88b.8       888           ######
######      `88b    ooo  `88b    d88'  8       `888  oo     .d8P      888       888       o  8       `888       888           ######
######       `Y8bood8P'   `Y8bood8P'  o8o        `8  8""88888P'      o888o     o888ooooood8 o8o        `8      o888o          ######
########                                                                                                                    ########
####################################################################################################################################
#################################################################################################################################"""

def select_stream(yt, quality):
    stream = None
    if quality == "audio":
        stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    elif quality == "128kbps":
        stream = yt.streams.filter(only_audio=True, abr="128kbps").first()
    elif quality == "160kbps":
        stream = yt.streams.filter(only_audio=True, abr="160kbps").first()
    elif quality == "360p":
        stream = yt.streams.filter(res="360p", progressive=True).first()
    elif quality == "720p":
        stream = yt.streams.filter(res="720p", progressive=True).first()
    elif quality == "1080p":
        stream = yt.streams.filter(res="1080p").first()
    elif quality == "2k":
        stream = yt.streams.filter(res="1440p").first()
    elif quality == "4k":
        stream = yt.streams.filter(res="2160p").first()
    elif quality == "8k":
        stream = yt.streams.filter(res="4320p").first()
    else:
        stream = yt.streams.get_highest_resolution()
    return stream
def singel_content_select_stream(yt, quality):
    return select_stream(yt, quality)
def playlist_select_stream(yt, quality):
    return select_stream(yt, quality)
def channel_select_stream(yt, quality):
    return select_stream(yt, quality)

def quality_input():
    print(colored('        [i] Select the download quality:', 'cyan', attrs=['bold']))
    print(colored('        [1] Audio only (best quality)', 'cyan'))
    print(colored('        [2] Audio 128kbps', 'cyan'))
    print(colored('        [3] Audio 160kbps', 'cyan'))
    print(colored('        [4] 360p', 'cyan'))
    print(colored('        [5] 720p', 'cyan'))
    print(colored('        [6] 1080p', 'cyan'))
    print(colored('        [7] 2k', 'cyan'))
    print(colored('        [8] 4k', 'cyan'))
    print(colored('        [9] 8k', 'cyan'))
    print(colored('        [10] Highest available quality', 'cyan'))
    quality_choice = input(colored('        [?] Enter the number of your choice : ', 'cyan', attrs=['bold'])).strip()
    quality_map = {
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
    quality = quality_map.get(quality_choice, 'highest')
    return quality

"""#################################################################################################################################
####################################################################################################################################
########                                                                                                                    ########
######       .o            .oooooo.     .oooooo.   ooooo      ooo ooooooooooooo oooooooooooo ooooo      ooo ooooooooooooo     ######
######     o888           d8P'  `Y8b   d8P'  `Y8b  `888b.     `8' 8'   888   `8 `888'     `8 `888b.     `8' 8'   888   `8     ######
######      888          888          888      888  8 `88b.    8       888       888          8 `88b.    8       888          ######
######      888  ######  888          888      888  8   `88b.  8       888       888oooo8     8   `88b.  8       888          ######
######      888          888          888      888  8     `88b.8       888       888    "     8     `88b.8       888          ######
######      888          `88b    ooo  `88b    d88'  8       `888       888       888       o  8       `888       888          ######
######     o888o          `Y8bood8P'   `Y8bood8P'  o8o        `8      o888o     o888ooooood8 o8o        `8      o888o         ######
########                                                                                                                    ########
####################################################################################################################################
#################################################################################################################################"""
def download_single_video(video_url):
    quality = quality_input()
    try:
        yt = YouTube(video_url)
        print(colored(f'        [i] Downloading video: {yt.title} ({quality})', color="blue", attrs=["bold"]))
        
        # Create directory for downloads if it doesn't exist
        download_dir = os.path.join(BASE_DIR, 'videos', quality)
        os.makedirs(download_dir, exist_ok=True)
        
        # Create log directory if it doesn't exist
        log_dir = os.path.join(BASE_DIR, 'videos', 'log')
        os.makedirs(log_dir, exist_ok=True)
        
        # Download the video
        stream = singel_content_select_stream(yt, quality)
        if stream:
            # Log download information
            log_data1 = {
                'title': yt.title,
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
            log_data2 = {
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
                    'rating': yt.rating,
                }
            }
            log_file_path1 = os.path.join(log_dir, 'all_log.json')
            log_file_path2 = os.path.join(log_dir, f'{quality}_log.json')
            singel_content_update_log(log_file_path1, log_data1)
            singel_content_update_log(log_file_path2, log_data2)
            
            file_path = stream.download(output_path=download_dir)
            print(colored(f'        [i] Download complete: {yt.title} ', color="green", attrs=["bold"]))
            
        else:
            print(colored(f'        [!] No stream found for {yt.title} with quality {quality}', color="red", attrs=["bold"]))
    except Exception as e:
        print(colored(f'        [!] Failed to download {yt.title}: {e} ', color="red", attrs=["bold"]))
def singel_content_load_log(log_file):
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return json.load(f)
    return []
def singel_content_update_log(log_file, log_data):
    log = singel_content_load_log(log_file)
    log.append(log_data)
    with open(log_file, 'w') as f:
        json.dump(log, f, indent=4)
"""#########################################################################################################################
############################################################################################################################
########                                                                                                            ########
######       ooooooooo.   ooooo              .o.      oooooo   oooo ooooo        ooooo  .oooooo..o ooooooooooooo      ######
######       `888   `Y88. `888'             .888.      `888.   .8'  `888'        `888' d8P'    `Y8 8'   888   `8      ######
######        888   .d88'  888             .8"888.      `888. .8'    888          888  Y88bo.           888           ######
######        888ooo88P'   888            .8' `888.      `888.8'     888          888   `"Y8888o.       888           ######
######        888          888           .88ooo8888.      `888'      888          888       `"Y88b      888           ######
######        888          888       o  .8'     `888.      888       888       o  888  oo     .d8P      888           ######
######       o888o        o888ooooood8 o88o     o8888o    o888o     o888ooooood8 o888o 8""88888P'      o888o          ######
########                                                                                                            ########
############################################################################################################################
#########################################################################################################################"""
# IMPORTS TO RUN PLAYLIST DOWNLOADER FUNCTIONS
def playlist_load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None
def playlist_save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
def playlist_download_video(video, folder, idx, total_videos, log_file, log_data, quality):
    try:
        yt = YouTube(video.watch_url)
        print(colored(f'        [i] Downloading video ({idx}/{total_videos}): {video.title} ({quality})', color="blue", attrs=["bold"]))
        stream = playlist_select_stream(yt, quality)
        if stream:
            stream.download(output_path=folder)
            print(colored(f'        [i] Download complete: {video.title} ', color="green", attrs=["bold"]))
            log_data['completed'].append(video.watch_url)
        else:
            print(colored(f'        [!] No stream found for {video.title} with quality {quality}', color="red", attrs=["bold"]))
            if video.watch_url not in log_data['not_completed']:
                log_data['not_completed'].append(video.watch_url)
        playlist_save_json(log_file, log_data)
    except Exception as e:
        print(colored(f'        [!] Failed to download {video.title}: {e} ', color="red", attrs=["bold"]))
        if video.watch_url not in log_data['not_completed']:
            log_data['not_completed'].append(video.watch_url)
        playlist_save_json(log_file, log_data)
def playlist_video_exists(video, log_data):
    return video.watch_url in log_data['completed']
def playlist_create_directories(playlist_title, quality):
    base_dir = 'playlist'
    playlist_folder = os.path.join(BASE_DIR, base_dir, playlist_title)
    quality_folder = os.path.join(playlist_folder, quality)
    log_folder = os.path.join(playlist_folder, 'download_data')
    
    os.makedirs(quality_folder, exist_ok=True)
    os.makedirs(log_folder, exist_ok=True)
    
    return playlist_folder, quality_folder, log_folder

def playlist_get_video_links(playlist_url, links_file):
    links_data = playlist_load_json(links_file)
    if links_data and 'video_urls' in links_data:
        return links_data['video_urls']
    
    playlist = Playlist(playlist_url)
    video_urls = [video.watch_url for video in playlist.videos]
    playlist_save_json(links_file, {'video_urls': video_urls})
    return video_urls
def download_playlist_videos(playlist_url):
    playlist = Playlist(playlist_url)
    print(colored(f'        [i] Downloading playlist: {playlist.title} ', color="magenta", attrs=["bold"]))
    quality = quality_input()
    playlist_folder, quality_folder, log_folder = playlist_create_directories(playlist.title, quality)
    links_file = os.path.join(log_folder, 'links.json')
    log_file = os.path.join(log_folder, f'{quality}.json')
    
    video_urls = playlist_get_video_links(playlist_url, links_file)
    log_data = playlist_load_json(log_file) or {'completed': [], 'not_completed': []}
    
    total_videos = len(video_urls)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for idx, video_url in enumerate(video_urls, start=1):
            video = YouTube(video_url)
            if playlist_video_exists(video, log_data):
                print(colored(f'        [~] Skipping already downloaded video ({idx}/{total_videos}): {video.title} ', color="yellow", attrs=["bold"]))
                continue
            futures.append(executor.submit(playlist_download_video, video, quality_folder, idx, total_videos, log_file, log_data, quality))
        
        for future in concurrent.futures.as_completed(futures):
            future.result()
    
    print(colored('        [i] All downloads complete!', 'green'))
"""#########################################################################################################################
############################################################################################################################
########                                                                                                            ########
######         .oooooo.   ooooo   ooooo       .o.       ooooo      ooo ooooo      ooo oooooooooooo ooooo              ######
######        d8P'  `Y8b  `888'   `888'      .888.      `888b.     `8' `888b.     `8' `888'     `8 `888'              ######
######       888           888     888      .8"888.      8 `88b.    8   8 `88b.    8   888          888               ######
######       888           888ooooo888     .8' `888.     8   `88b.  8   8   `88b.  8   888oooo8     888               ######
######       888           888     888    .88ooo8888.    8     `88b.8   8     `88b.8   888    "     888               ######
######       `88b    ooo   888     888   .8'     `888.   8       `888   8       `888   888       o  888       o       ######
######        `Y8bood8P'  o888o   o888o o88o     o8888o o8o        `8  o8o        `8  o888ooooood8 o888ooooood8       ######
########                                                                                                            ########
############################################################################################################################
#########################################################################################################################"""
# IMPORTS TO RUN CHANNEL DOWNLOADER FUNCTIONS
def channel_get_video_urls(api_key, channel_id, channel_name):
    # Define the base URLs
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    # Check if the links.json file exists for the channel
    links_file = os.path.join(BASE_DIR, 'channels', channel_name, 'download_data', 'links.json')
    if os.path.exists(links_file):
        # Load existing video URLs from the JSON file
        with open(links_file, 'r') as f:
            data = json.load(f)
            print(colored('        [i] There is info and links of this channel in local db, not fatching from google :', 'cyan', attrs=['bold']))
            return data['video_urls']
    # If the links.json file doesn't exist, fetch video URLs from the YouTube Data API
    first_url = f'{base_search_url}key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50'
    video_urls = []
    # Retrieve video URLs from the API response
    url = first_url
    while True:
        response = requests.get(url).json()
        for item in response['items']:
            if item['id']['kind'] == "youtube#video":
                video_urls.append(base_video_url + item['id']['videoId'])
        # Check if there are more pages of results
        try:
            next_page_token = response['nextPageToken']
            url = f'{first_url}&pageToken={next_page_token}'
        except KeyError:
            break
    # Save the fetched video URLs to the links.json file for future use
    os.makedirs(os.path.join(BASE_DIR, 'channels', channel_name, 'download_data'), exist_ok=True)
    with open(links_file, 'w') as f:
        json.dump({'video_urls': video_urls}, f, indent=4)
    print(colored('        [i] Fatching from google info and links of this channel :', 'cyan', attrs=['bold']))
    return video_urls
def channel_load_log(log_file):
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return json.load(f)
    return {'completed': [], 'not_completed': []}
def channel_save_log(log_file, log_data):
    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=4)
def download_channel_video(video_url, folder, idx, total_videos, log_file, log_data, quality):
    try:
        yt = YouTube(video_url)
        print(colored(f'        [i] Downloading video ({idx}/{total_videos}): {yt.title} ({quality})', color="blue", attrs=["bold"]))
        stream = channel_select_stream(yt, quality)
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
def channel_video_exists(video_url, log_data):
    return video_url in log_data['completed']
def download_channel(api_key, channel_id, channel_name):
    # Get video URLs from the channel
    video_urls = channel_get_video_urls(api_key, channel_id, channel_name)
    # Check if there are existing log files for the channel and quality
    log_folder = os.path.join(BASE_DIR, 'channels', channel_name, 'download_data')
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    # Ask user for desired quality
    quality = quality_input() # returns one of 'audio','128kbps','160kbps','360p','720p','1080p','2k','4k','8k','highest'
    log_file = os.path.join(log_folder, f'{quality}.json')
    log_data = channel_load_log(log_file)
    if log_data['completed'] or log_data['not_completed']:
        print(colored('        [i] Some records found for this channel and quality.', 'cyan'))
        print(colored('        [i] There are some incomplete downloads.', 'cyan'))
        print(colored('        [i] What would you like to do?', 'cyan'))
        print(colored('        [1] Download only incomplete items from the JSON database.', 'cyan'))
        print(colored('        [2] Recheck all videos from Google data.', 'cyan'))
        choice = input(colored("        [?] Enter your choice (default: 1): ", 'blue')).strip()
        if choice == '2':
            log_data = {'completed': [], 'not_completed': []}  # Reset log data for rechecking from Google
        else:
            print(colored('        [i] Downloading incomplete items from the JSON database.', 'cyan'))
    else:
        print(colored('        [i] No downloading records found for this channel and quality.', 'cyan'))
        print(colored('        [i] Proceeding to fetch video URLs from Google data.', 'cyan'))
    # Total number of videos in the channel
    total_videos = len(video_urls)
    # Download videos concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for idx, video_url in enumerate(video_urls, start=1):
            if channel_video_exists(video_url, log_data):
                print(colored(f'        [~] Skipping already downloaded video ({idx}/{total_videos}): {video_url} ',
                              color="yellow", attrs=["bold"]))
                continue
            futures.append(
                executor.submit(download_channel_video, video_url, os.path.join(BASE_DIR, 'channels', channel_name, quality), idx, total_videos, log_file, log_data, quality))
        # Wait for all the threads to complete
        for future in concurrent.futures.as_completed(futures):
            future.result()
    print(colored('        [i] All downloads complete!', 'green'))
"""################################################################################################################################
###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
################################################################################################################################"""
def normalize_video_url(url):
    base_url = 'https://www.youtube.com/watch?v='
    # Check if the input is just a video ID
    if len(url) == 11:
        normalized_url = base_url + url
    else:
        # Ensure the URL starts with 'https://www.youtube.com/'
        if not url.startswith('https://www.youtube.com/'):
            if url.startswith('https://'):
                url = url.replace('https://', 'https://www.')
            elif url.startswith('youtube.com/'):
                url = 'https://www.' + url
            else:
                url = 'https://www.youtube.com/' + url.split('youtube.com/')[1]
        # Find the start of the video ID
        video_id_index = url.find('v=')
        # If the video ID is found, return the normalized URL
        if video_id_index != -1:
            # Extract the base URL up to the video ID
            base_url = url[:video_id_index + len('v=')]
            # Extract the video ID
            video_id = url[video_id_index + len('v='):]
            # Find the end of the video ID (before any additional parameters)
            end_of_id_index = video_id.find('&')
            if end_of_id_index != -1:
                video_id = video_id[:end_of_id_index]
            # Construct the normalized URL
            normalized_url = base_url + video_id
        else:
            normalized_url = url
    return normalized_url
def fetch_video_title(normalized_url):
    try:
        video = YouTube(normalized_url)
        video_title = video.title
    except (PytubeError, HTTPError) as e:
        print(f"Failed to fetch video title: {e}")
        video_title = None
    return video_title
"""################################################################################################################################
###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
################################################################################################################################"""
def normalize_playlist_url(url):
    base_url = 'https://www.youtube.com/playlist?list='
    # Check if the input is just a playlist ID
    if url.startswith('PL'):
        normalized_url = base_url + url
    else:
        # Ensure the URL starts with 'https://www.youtube.com/'
        if not url.startswith('https://www.youtube.com/'):
            if url.startswith('https://'):
                url = url.replace('https://', 'https://www.')
            elif url.startswith('youtube.com/'):
                url = 'https://www.' + url
            else:
                url = 'https://www.youtube.com/' + url.split('youtube.com/')[1]
        # Find the start of the playlist ID
        playlist_id_index = url.find('list=')
        # If the playlist ID is found, return the normalized URL
        if playlist_id_index != -1:
            # Extract the base URL up to the playlist ID
            base_url = url[:playlist_id_index + len('list=')]
            # Extract the playlist ID
            playlist_id = url[playlist_id_index + len('list='):]
            # Find the end of the playlist ID (before any additional parameters)
            end_of_id_index = playlist_id.find('&')
            if end_of_id_index != -1:
                playlist_id = playlist_id[:end_of_id_index]
            # Construct the normalized URL
            normalized_url = base_url + playlist_id
        else:
            normalized_url = url
    return normalized_url
def fetch_playlist_title(normalized_url):
    try:
        playlist = Playlist(normalized_url)
        playlist_title = playlist.title
    except PytubeError as e:
        print(f"Failed to fetch playlist title: {e}")
        playlist_title = None
    except HTTPError as e:
        print(f"Failed to fetch playlist title: {e}")
        playlist_title = None
    return playlist_title
"""################################################################################################################################
###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
################################################################################################################################"""
def load_log():
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as file:
            return json.load(file)
    return {}
def save_log(log):
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    with open(LOG_FILE_PATH, 'w') as file:
        json.dump(log, file, indent=4)
def start_u_ydt():
    log = load_log()
    print(colored("        [i] What would you like to download?", 'blue'))
    print(colored("        [1] Channel", 'cyan'))
    print(colored("        [2] Playlist", 'cyan'))
    print(colored("        [3] Single Content", 'cyan'))
    print(colored("        [4] Check Previous", 'cyan'))
    choice = input(colored("        [~] Choose an option : ", 'yellow'))
    if choice == '1':
        # Channel download
        if 'api_keys' in log and log['api_keys']:
            print(colored("        [i] Available API keys:", 'blue'))
            for i, api_key in enumerate(log['api_keys'], 1):
                print(colored(f"        [{i}] {api_key}", 'cyan'))
            api_choice = input(colored("        [~] Choose an API key or enter 'new' to use a new API key: ", 'yellow'))
            if api_choice.isdigit() and 1 <= int(api_choice) <= len(log['api_keys']):
                api_key = log['api_keys'][int(api_choice) - 1]
            else:
                api_key = input(colored("        [~] Enter new API key: ", 'yellow'))
                log.setdefault('api_keys', []).append(api_key)
        else:
            api_key = input(colored("        [~] Enter new API key: ", 'yellow'))
            log['api_keys'] = [api_key]
        channel_id = input(colored("        [~] Enter channel ID: ", 'yellow'))
        if 'channels' in log and channel_id in [c['channel_id'] for c in log['channels']]:
            channel = next(c for c in log['channels'] if c['channel_id'] == channel_id)
            default_name = channel['channel_name']
            print(colored(f"        [~] Channel exist in log, named : {default_name}: ", 'yellow'))
            channel_name = default_name
        else:
            channel_name = input(colored("        [~] Enter channel name: ", 'yellow'))
            log.setdefault('channels', []).append({
                'channel_id': channel_id,
                'channel_name': channel_name
            })
        save_log(log)
        download_channel(api_key, channel_id, channel_name)
    elif choice == '2':
        # Playlist download
        playlist_url = input(colored("        [~] Enter playlist URL or ID: ", 'yellow'))
        normalized_url = normalize_playlist_url(playlist_url)
        if 'playlists' in log and normalized_url in [p['playlist_url'] for p in log['playlists']]:
            playlist = next(p for p in log['playlists'] if p['playlist_url'] == normalized_url)
            default_title = playlist['playlist_title']
            print(colored(f"        [~] Playlist exist in log, named : {default_title}: ", 'yellow'))
            playlist_title =  default_title
        else:
            playlist_title = fetch_playlist_title(normalized_url)
            log.setdefault('playlists', []).append({
                'playlist_url': normalized_url,
                'playlist_title': playlist_title
            })
        save_log(log)
        download_playlist_videos(normalized_url)
    elif choice == '3':
        # Single content download
        single_content_url = input(colored("        [~] Enter single content URL or ID: ", 'yellow'))
        normalized_url = normalize_video_url(single_content_url)
        if 'single_contents' in log and normalized_url in [v['video_url'] for v in log['single_contents']]:
            video = next(v for v in log['single_contents'] if v['video_url'] == normalized_url)
            default_title = video['video_title']
            print(colored(f"        [~] The Content exist in log, named : {default_title}: ", 'yellow'))
            video_title = default_title
        else:
            video_title = fetch_video_title(normalized_url)
            log.setdefault('single_contents', []).append({
                'video_url': normalized_url,
                'video_title': video_title
            })
        save_log(log)
        download_single_video(normalized_url)
    elif choice == '4':
        # Check previous downloads
        print(colored("        [i] Which type of previous downloads do you want to check?", 'blue'))
        print(colored("        [1] Videos", 'cyan'))
        print(colored("        [2] Playlists", 'cyan'))
        print(colored("        [3] Channels", 'cyan'))
        print(colored("        [4] All", 'cyan'))
        check_choice = input(colored("        [~] Choose an option : ", 'yellow'))
        if check_choice == '1':
            if 'single_contents' in log:
                print(colored("        [i] Previous video downloads:", 'blue'))
                for i, video in enumerate(log['single_contents'], 1):
                    print(colored(f"        [{i}] {video['video_title']} ({video['video_url']})", 'cyan'))
                video_choice = int(input(colored("        [~] Enter the number of the video to download: ", 'yellow')))
                save_log(log)
                download_single_video(log['single_contents'][video_choice - 1]['video_url'])
        elif check_choice == '2':
            if 'playlists' in log:
                print(colored("        [i] Previous playlist downloads:", 'blue'))
                for i, playlist in enumerate(log['playlists'], 1):
                    print(colored(f"        [{i}] {playlist['playlist_title']} ({playlist['playlist_url']})", 'cyan'))
                playlist_choice = int(input(colored("        [~] Enter the number of the playlist to download: ", 'yellow')))
                save_log(log)
                download_playlist_videos(log['playlists'][playlist_choice - 1]['playlist_url'])
        elif check_choice == '3':
            if 'channels' in log:
                print(colored("        [i] Previous channel downloads:", 'blue'))
                for i, channel in enumerate(log['channels'], 1):
                    print(colored(f"        [{i}] {channel['channel_name']} ({channel['channel_id']})", 'cyan'))
                channel_choice = int(input(colored("        [~] Enter the number of the channel to download: ", 'yellow')))
                channel = log['channels'][channel_choice - 1]
                if 'api_keys' in log and log['api_keys']:
                    print(colored("        [i] Available API keys:", 'blue'))
                    for i, api_key in enumerate(log['api_keys'], 1):
                        print(colored(f"        [{i}] {api_key}", 'cyan'))
                    api_choice = input(colored("        [~] Choose an API key or enter 'new' to use a new API key: ", 'yellow'))
                    if api_choice.isdigit() and 1 <= int(api_choice) <= len(log['api_keys']):
                        api_key = log['api_keys'][int(api_choice) - 1]
                    else:
                        api_key = input(colored("        [~] Enter new API key: ", 'yellow'))
                        log.setdefault('api_keys', []).append(api_key)
                else:
                    api_key = input(colored("        [~] Enter new API key: ", 'yellow'))
                    log['api_keys'] = [api_key]
                save_log(log)
                download_channel(api_key, channel['channel_id'], channel['channel_name'])
        elif check_choice == '4':
            if 'single_contents' in log:
                print(colored("        [i] Previous video downloads:", 'blue'))
                for i, video in enumerate(log['single_contents'], 1):
                    print(colored(f"        [{i}] {video['video_title']} ({video['video_url']})", 'cyan'))
            if 'playlists' in log:
                print(colored("        [i] Previous playlist downloads:", 'blue'))
                for i, playlist in enumerate(log['playlists'], 1):
                    print(colored(f"        [{i}] {playlist['playlist_title']} ({playlist['playlist_url']})", 'cyan'))
            if 'channels' in log:
                print(colored("        [i] Previous channel downloads:", 'blue'))
                for i, channel in enumerate(log['channels'], 1):
                    print(colored(f"        [{i}] {channel['channel_name']} ({channel['channel_id']})", 'cyan'))
            prev_choice = input(colored("        [~] Enter the number of the download to complete: ", 'yellow'))
            prev_choice = int(prev_choice)
            if prev_choice <= len(log.get('single_contents', [])):
                save_log(log)
                download_single_video(log['single_contents'][prev_choice - 1]['video_url'])
            elif prev_choice <= len(log.get('single_contents', [])) + len(log.get('playlists', [])):
                save_log(log)
                download_playlist_videos(log['playlists'][prev_choice - len(log.get('single_contents', [])) - 1]['playlist_url'])
            else:
                index = prev_choice - len(log.get('single_contents', [])) - len(log.get('playlists', [])) - 1
                channel_info = log['channels'][index]
                if 'api_keys' in log and log['api_keys']:
                    print(colored("        [i] Available API keys:", 'blue'))
                    for i, api_key in enumerate(log['api_keys'], 1):
                        print(colored(f"        [{i}] {api_key}", 'cyan'))
                    api_choice = input(colored("        [~] Choose an API key or enter 'new' to use a new API key: ", 'yellow'))
                    if api_choice.isdigit() and 1 <= int(api_choice) <= len(log['api_keys']):
                        api_key = log['api_keys'][int(api_choice) - 1]
                    else:
                        api_key = input(colored("        [~] Enter new API key: ", 'yellow'))
                        log.setdefault('api_keys', []).append(api_key)
                else:
                    api_key = input(colored("        [~] Enter new API key: ", 'yellow'))
                    log['api_keys'] = [api_key]
                save_log(log)
                download_channel(api_key, channel_info['channel_id'], channel_info['channel_name'])

def main():
    while True:
        try:
            banner()
            start_u_ydt()
        except Exception as e:
            input(colored(f"\n        [!] Error Occured, Details : {e} ", 'red'))
        except KeyboardInterrupt as e:
            input(colored("\n        [?] Press Enter to get out : ", 'red'))
            break
        xinp = input(colored("\n        [?] Want to do some more things (y/n):", 'red'))
        if xinp == 'y':
            continue
        else:
            break
if __name__ == "__main__":
    main()
