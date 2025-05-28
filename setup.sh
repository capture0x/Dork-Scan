
#!/bin/bash

set -e  

echo "[*] Downloading chromedriver..."
curl -L -O https://github.com/dreamshao/chromedriver/blob/main/132.0.6834.83%20chromedriver-linux64.zip

if [ ! -f chromedriver-linux64.zip ]; then
    echo "[!] Download failed: chromedriver-linux64.zip not found"
    exit 1
fi

echo "[*] Extracting chromedriver zip archive..."
unzip -o chromedriver-linux64.zip

if [ ! -d chromedriver-linux64 ]; then
    echo "[!] Archive extracted but chromedriver-linux64 directory not found"
    exit 1
fi

cd chromedriver-linux64

if [ ! -f chromedriver ]; then
    echo "[!] chromedriver binary not found in the directory"
    exit 1
fi

echo "[*] Moving chromedriver to /usr/bin/..."
sudo mv -f chromedriver /usr/bin/chromedriver

echo "[*] Setting permissions for chromedriver..."
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

echo "[✓] Installation completed successfully"




