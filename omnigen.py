import os
import subprocess
import logging
from datetime import datetime
import time

# Configure logging
logging.basicConfig(filename='omnigen.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_print(message):
    logging.info(message)
    print(message)

def check_for_updates():
    log_and_print("Checking for available Windows updates...")
    try:
        update_command = 'powershell "Get-WindowsUpdate"'
        result = subprocess.run(update_command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            log_and_print("Updates found:\n" + result.stdout)
            return True
        else:
            log_and_print("No updates available or error checking updates.")
            return False
    except Exception as e:
        log_and_print(f"Error while checking updates: {e}")
        return False

def apply_updates():
    log_and_print("Applying available Windows updates...")
    try:
        install_command = 'powershell "Install-WindowsUpdate -AcceptAll -AutoReboot"'
        result = subprocess.run(install_command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            log_and_print("Updates successfully applied:\n" + result.stdout)
        else:
            log_and_print("Failed to apply updates:\n" + result.stderr)
    except Exception as e:
        log_and_print(f"Error while applying updates: {e}")

def omni_gen():
    log_and_print("OmniGen Security Patch Management Started")
    while True:
        if check_for_updates():
            apply_updates()
        else:
            log_and_print("System is up-to-date with the latest security patches.")

        # Wait for 24 hours before checking again
        time.sleep(86400)

if __name__ == "__main__":
    omni_gen()