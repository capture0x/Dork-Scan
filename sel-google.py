from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def extract_url_from_html(query, page_limit):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    service = Service('/usr/bin/chromedriver')
    try:
        browser = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Error occurred: {e}")

    results = set()

    for page_num in range(page_limit):
        url = f"https://www.google.com/search?q={query}&start={page_num * 10}"
        browser.get(url)
        time.sleep(20)  

        elements = browser.find_elements('css selector', 'span[jscontroller="msmzHf"] a[jsname="UWckNb"]')
        
        for elem in elements:
            href = elem.get_attribute('href')
            if href:
                print(href)
                results.add(href)

    browser.quit()
    return list(results)

if __name__ == "__main__":
    dork = input("Enter the dork: ")
    page_limit = int(input("How many pages to scan? "))

    matching_results = extract_url_from_html(dork, page_limit)

    with open("results.txt", "w") as f:
        for result in matching_results:
            f.write(result + "\n")

    print(f"\n{len(matching_results)} unique matching results saved to 'results.txt'.")

