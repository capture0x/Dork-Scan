#!/usr/bin/env python3
import random
import shutil
import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Banner dependencies
import pyfiglet
from colorama import init, Fore, Style

def print_banner():
    init(autoreset=True)
    banner = pyfiglet.figlet_format("DORK SCAN", font="slant")
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    for line in banner.split("\n"):
        print(random.choice(colors) + line)
    subtitle = f"{Style.BRIGHT}{Fore.WHITE}Coded By TMRSWRR"
    cols = shutil.get_terminal_size((80, 20)).columns
    print(subtitle.center(cols))
    print()

def extract_url_from_html(query, page_limit):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    service = Service('/usr/bin/chromedriver')
    try:
        browser = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"{Fore.RED}Error occurred: {e}{Style.RESET_ALL}")
        sys.exit(1)

    results = set()

    for page_num in range(page_limit):
        url = f"https://www.google.com/search?q={query}&start={page_num * 10}"
        browser.get(url)
        time.sleep(20)

        elements = browser.find_elements('css selector', 'span[jscontroller="msmzHf"] a[jsname="UWckNb"]')
        for elem in elements:
            href = elem.get_attribute('href')
            if href:
                print(f"{Fore.CYAN}{href}{Style.RESET_ALL}")
                results.add(href)

    browser.quit()
    return list(results)

if __name__ == "__main__":
    print_banner()
    dork = input(f"{Fore.GREEN}Enter the dork: {Style.RESET_ALL}")
    page_limit = int(input(f"{Fore.GREEN}How many pages to scan? {Style.RESET_ALL}"))

    matching_results = extract_url_from_html(dork, page_limit)

    with open("results.txt", "w") as f:
        for result in matching_results:
            f.write(result + "\n")

    print(f"\n{Fore.YELLOW}{len(matching_results)} unique matching results saved to 'results.txt'.{Style.RESET_ALL}")
