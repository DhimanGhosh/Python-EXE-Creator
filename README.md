# Python-EXE-Creator
This script gives the user a gui-based pyinstaller implementation to convert .py to EXEs.

The script runs on Python 2.7. You need to download pyinstaller to convert a script to an executable file.

Usage: Double-click createExe.py. It opens as a wxPython-based window with all of the applicable options for pyinstaller. After you select the desired options, it runs pyinstaller-exe with all of the corresponding command line arguments. You can even use it to make the script itself into an executable ;-)

All of the available options are documented in the pyinstaller project documentation. Note that not all of the options have been tested. 

The program expects that pyinstaller is installed to c:\python27\scripts\pyinstaller.exe. If it is not located there, you can change it to the actual directory on line 43 of the script.
