import pync
import subprocess
import time

def monitor():
    applescript_code = '''tell application "Google Chrome" 
    set siteName to URL of active tab of front window 
    set webName to "Current site is " & siteName 
    return webName 
    end tell
    '''
    
    currentSite = subprocess.run(['osascript', '-e' , applescript_code], capture_output = True , text = True)

    site = currentSite.stdout.strip()

    badSites = ["x.com","youtube.com","reddit.com"]

    if any(sub in site for sub in badSites) :
        pync.notify('😆', title = 'Back to Work...')
        subprocess.run(['open' , '-a', 'Visual Studio Code'])




while True:
    monitor()
    time.sleep(5)


