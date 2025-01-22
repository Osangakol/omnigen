# OmniGen

OmniGen is a Python-based utility designed to maintain the security of Windows systems by automatically monitoring and applying the latest security patches and updates. It ensures that your system is protected against vulnerabilities by staying up-to-date with the latest security enhancements.

## Features

- **Automated Update Checks**: Regularly checks for available Windows updates.
- **Automatic Installation**: Installs updates automatically when they become available.
- **Logging**: Records update status and errors in a log file for auditing and troubleshooting.
- **Continuous Operation**: Runs continuously in the background to ensure your system remains secure.

## Requirements

- Python 3.x
- Administrative privileges (required for installing updates)

## Installation

1. Clone the repository or download the `omnigen.py` file.
2. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Open a terminal or command prompt with administrative privileges.
2. Navigate to the directory containing `omnigen.py`.
3. Run the script using Python:

   ```sh
   python omnigen.py
   ```

OmniGen will start monitoring for updates and apply them as they become available. It logs all actions to `omnigen.log`, which can be reviewed to verify update application status or troubleshoot any issues.

## Note

- The script requires administrative privileges to apply updates. Make sure to run the terminal or command prompt as an administrator.
- The script is configured to check for updates every 24 hours. You can modify the `time.sleep(86400)` statement to change the interval.

## License

This project is licensed under the MIT License.