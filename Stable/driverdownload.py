#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
import sys
import os
import pathlib
import urllib.request
import re
import zipfile
import stat
from sys import platform
import platform as pt
cwd = os.getcwd()
def get_driver():
    # Attempt to open the Selenium chromedriver. If it fails, download the latest chromedriver.
    driver = None
    retry = True

    while retry:
        retry = False
        is_download = False

        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(chrome_options=options, executable_path='/home/jackreaper/Documents/Facebook-Birthday-Bot/Stable/chromedriver')
        except SessionNotCreatedException as e:
            if 'This version of ChromeDriver' in e.msg:
                is_download = True
        except WebDriverException as e:
            if "wrong permissions" in e.msg:
                st = os.stat('/home/jackreaper/Documents/Facebook-Birthday-Bot/Stable/chromedriver')
                os.chmod('/home/jackreaper/Documents/Facebook-Birthday-Bot/Stable/chromedriver', st.st_mode | stat.S_IEXEC)
                retry = True
            elif "chromedriver' executable needs to be in PATH" in e.msg:
                is_download = True

        retry = is_download and download_driver()

    return driver

def get_chrome_version():
    os_name = pt.system()
    if os_name == 'Darwin':
        installation_path = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
    elif os_name == 'Windows':
        installation_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    elif os_name == 'Linux':
        installation_path = "/usr/bin/google-chrome"
    else:
        raise NotImplemented(f"Unknown OS '{os_name}'")

    version_str = os.popen(f"{installation_path} --version").read().strip('Google Chrome ').strip()
    return version_str
    
def download_driver():
    # Find the latest chromedriver, download, unzip, set permissions to executable.
    result = False
    url = 'https://chromedriver.chromium.org/downloads'
    base_driver_url = 'https://chromedriver.storage.googleapis.com/'
    file_name = 'chromedriver_' + get_platform_filename()
    driver_file_name = 'chromedriver' + '.exe' if platform == "win32" else ''
    pattern = 'https://.*?path=(\d+\.\d+\.\d+\.\d+)'

    # Download latest chromedriver.
    print('Finding latest chromedriver..')
    opener = urllib.request.FancyURLopener({})
    stream = opener.open(url)
    content = stream.read().decode('utf8')

    # Parse the latest version.
    match = re.search(pattern, content)
    if match and match.groups():
        # Url of download html page.
        url = match.group(0)
        # Version of latest driver.
        version = get_chrome_version()
        driver_url = base_driver_url + get_chrome_version() + '/' + file_name

        # Download the file.
        print('Version ' + version)
        print('Downloading ' + driver_url)
        app_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver_path = app_path + '/' + driver_file_name
        file_path = app_path + '/' + file_name
        urllib.request.urlretrieve(driver_url, file_path)

        # Unzip the file.
        print('Unzipping ' + file_path)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(app_path)

        print('Setting executable permission on ' + chromedriver_path)
        st = os.stat(chromedriver_path)
        os.chmod(chromedriver_path, st.st_mode | stat.S_IEXEC)

        # Cleanup.
        os.remove(file_path)

        result = True

    return result

def get_platform_filename():
    filename = ''

    is_64bits = sys.maxsize > 2**32

    if platform == "linux" or platform == "linux2":
        # linux
        filename += 'linux'
        filename += '64' if is_64bits else '32'
    elif platform == "darwin":
        # OS X
        filename += 'mac64'
    elif platform == "win32":
        # Windows...
        filename += 'win32'

    filename += '.zip'

    return filename


d = get_driver()
d.get('https://www.google.com')