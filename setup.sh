#!/bin/bash

set -e  


echo "[*] Detecting Chrome/Chromium version..."
if command -v google-chrome >/dev/null 2>&1; then
    ver_full=$(google-chrome --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
elif command -v chromium-browser >/dev/null 2>&1; then
    ver_full=$(chromium-browser --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
elif command -v chromium >/dev/null 2>&1; then
    ver_full=$(chromium --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
else
    echo "[!] Chrome or Chromium not found. Please install one of them first."
    exit 1
fi

if [ -z "$ver_full" ]; then
    echo "[!] Could not parse browser version."
    exit 1
fi

echo "[*] Detected browser version: $ver_full"


driver_version="$ver_full"


url="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${driver_version}/linux64/chromedriver-linux64.zip"
echo "[*] Downloading ChromeDriver for version $driver_version..."
curl -L -o chromedriver-linux64.zip "$url"

if [ ! -f chromedriver-linux64.zip ]; then
    echo "[!] Download failed: chromedriver-linux64.zip not found"
    exit 1
fi


echo "[*] Extracting zip archive..."
unzip -o chromedriver-linux64.zip

if [ ! -d chromedriver-linux64 ]; then
    echo "[!] Extraction succeeded but 'chromedriver-linux64' directory not found"
    exit 1
fi

cd chromedriver-linux64

if [ ! -f chromedriver ]; then
    echo "[!] 'chromedriver' binary not found inside archive"
    exit 1
fi


echo "[*] Moving chromedriver to /usr/bin/..."
sudo mv -f chromedriver /usr/bin/chromedriver

echo "[*] Setting ownership and executable bit..."
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

echo "[✓] ChromeDriver $driver_version installed successfully!"
