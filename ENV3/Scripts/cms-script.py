#!c:\users\btrac\pycharmprojects\sp20-516-226\env3\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cloudmesh-cmd5','console_scripts','cms'
__requires__ = 'cloudmesh-cmd5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cloudmesh-cmd5', 'console_scripts', 'cms')()
    )