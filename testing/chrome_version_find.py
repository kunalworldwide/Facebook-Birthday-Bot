import platform as pt
import os
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
    print(version_str)
    return version_str
    

get_chrome_version()
