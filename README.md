# Chrome Screenshots Automation
This Python script automates taking screenshots of multiple browser tabs in Chrome and saves each screenshot in a folder with the naming convention: YYYY-MM-DD_domain.com

## Requirements
- python 3.6+
- Selenium WebDriver
```
pip install selenium
```
- ChromeDriver executable

## Installation
1. Clone repository
```
git clone https://github.com/brandsecure/chrome-screenshots
```
2. Download the appropriate ChromeDriver executable for your system from the [ChromeDriver Downloads page](https://sites.google.com/chromium.org/driver/downloads?authuser=0). Choose the version that matches your installed Chrome browser version.
3. Unzip the downloaded file and move the chromedriver executable to a suitable location on your system.

## Configuration
1. Update the chrome_driver_path variable in the screenshots.py script with the path to your ChromeDriver executable:
```
chrome_driver_path = "/path/to/chromedriver"
```
2. Update the with open line with the path to the urls.txt (one URL per line)
```
# Read URLs from the text file
with open("/path/to/your/urls.txt", "r") as file:
```
3. Update the output_folder to desired location
```
# Folder to save the screenshots
output_folder = "/path/to/your/output_folder"
```
4. Default is headless mode. Other custom settings can be configured here:
```
# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
```
## Troubleshooting
### ChromeDriver Issues
If you encounter issues related to ChromeDriver, make sure you have downloaded the correct version for your installed Chrome browser. You can check your Chrome version by navigating to the menu (three vertical dots) in the top-right corner of the browser, then click Help > About Google Chrome.

For macOS users, if you encounter an error regarding "developer cannot be verified," follow these steps to allow the execution of the ChromeDriver binary:

1. Open a terminal.
2. Execute the following command:
```
xattr -d com.apple.quarantine /path/to/your/chromedriver
```
Replace /path/to/your/chromedriver with the actual path to your chromedriver binary. This command removes the quarantine attribute from the chromedriver binary, which should allow it to run without being blocked by Gatekeeper.
