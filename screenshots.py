import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Read URLs from the text file
with open("/path/to/your/urls.txt", "r") as file:
    url_list = [line.strip() for line in file]

# Path to your ChromeDriver executable
chrome_driver_path = "/path/to/your/chromedriver"

# Folder to save the screenshots
output_folder = "/path/to/your/output_folder"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

# Start the browser with the configured options
browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Iterate through the URLs and take screenshots
for url in url_list:
    browser.get(url)

    # Wait for the page to load
    browser.implicitly_wait(10)

    # Generate the screenshot file name
    date_string = datetime.datetime.now().strftime("%Y-%m-%d")
    domain = url.split("//")[-1].split("/")[0]
    file_name = f"{date_string}_{domain}.png"
    file_path = os.path.join(output_folder, file_name)

    # Take and save the screenshot
    browser.save_screenshot(file_path)

# Close the browser
browser.quit()
