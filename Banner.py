import colorama
from colorama import Fore, Style, init

def banner():
    return f"""

{Fore.YELLOW}██████╗ ██╗      █████╗ ██╗   ██╗    ███╗   ███╗ █████╗  ██████╗███████╗
{Fore.YELLOW}██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗██╔════╝██╔════╝
{Fore.YELLOW}██████╔╝██║     ███████║ ╚████╔╝     ██╔████╔██║███████║██║     ███████╗
{Fore.YELLOW}██╔═══╝ ██║     ██╔══██║  ╚██╔╝      ██║╚██╔╝██║██╔══██║██║     ╚════██║
{Fore.YELLOW}██║     ███████╗██║  ██║   ██║       ██║ ╚═╝ ██║██║  ██║╚██████╗███████║
{Fore.YELLOW}╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
        By ZIEDEV 2024 
        Github: https://github.com/zinzied                                                               
{Style.RESET_ALL}"""

init(autoreset=True)
