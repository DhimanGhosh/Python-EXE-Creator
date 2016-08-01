# This simple script which I am shocked was not created before converts the
# CLI pyinstaller process to a GUI-based installer creator.

import wx
from sys import exit
from subprocess import call


def createExe(e):
    if loadField.Value == '' or not loadField.Value.endswith('.py') and not loadField.Value.endswith('.pyw'):
        statusMsg.SetLabel('Please select a .py or .pyw file for conversion.')
        return
    else:
        statusMsg.SetLabel('Converting to EXE, please wait...') # why isn't this set when the label is currently an empty string?
        lineLast.Layout()
        
    arguments = ''
    if oneFile.Value == True: arguments = arguments + ' --onefile'
    if windowed.Value == True: arguments = arguments + ' --windowed'
    if fieldDpath.Value != '': arguments = arguments + ' --distpath "' + fieldDpath.Value + '"'
    if fieldWpath.Value != '': arguments = arguments + ' --workpath "' + fieldWpath.Value + '"'
    if overwriteOutput.Value == True: arguments = arguments + ' -y'
    if noUnicode.Value == True: arguments = arguments + ' -a'
    if fieldUpath.Value != '': arguments = arguments + ' --upx-dir "' + fieldUpath.Value + '"'
    if loglevel.Value in logopts: arguments = arguments + ' --log-level=' + loglevel.Value #don't use for now
    if cleanCache.Value == True: arguments = arguments + ' --clean'
    if fieldSpath.Value != '': arguments = arguments + ' --specpath "' + fieldSpath.Value + '"'
    if fieldAppName.Value != '':
        fixedName = fixName(fieldAppName.Value)
        arguments = arguments + ' -n "' + fixedName + '"' 
    if fieldIpath.Value != '': arguments = arguments + ' -i "' + fieldIpath.Value + '"'
    if fieldMisc.Value != '': arguments = arguments + ' ' + fieldMisc.Value
    if noUpx.Value == True: arguments = arguments + ' --noupx'
    if debugMode.Value == True: arguments = arguments + ' -d'
    if strip.Value == True: arguments = arguments + ' -s'
    if uacAdmin.Value == True: arguments = arguments + ' --uac-admin'
    if uacUiaccess.Value == True: arguments = arguments + ' --uac-uiaccess'
    if privateAssemblies.Value == True: arguments = arguments + ' --win-private-assemblies'
    if noAssyRedirects.Value == True: arguments = arguments + ' --uac-no-prefer-redirects'

    
    print 'pyinstaller' + arguments + ' "' + loadField.Value + '"'
    c = call('C:\Python27\Scripts\pyinstaller.exe' + arguments + ' "' + loadField.Value + '"', shell=True)

    if c == 0:
        exit(0)
    else:
        errMsg = wx.MessageDialog(win, 'Conversion completed with errors.', 'Error', style=wx.OK | wx.ICON_ERROR)
        if errMsg.ShowModal() == wx.ID_OK:
            exit(1) 

# a little function to fix invalid chars in filenames
def fixName(rawname):
    fixed = ''
    for i,c in enumerate(rawname):
        if c in '<>:"/\\|?*':
            fixed = fixed + '_'
        else:
            fixed = fixed + c
    if fixed.endswith('.exe'):
        fixed = fixed[:-4]
    return fixed

# about this program
def aboutDialog(e):
    description = """The pyinstaller EXEcutor is designed to convert
.py and .pyw scripts into Windows executables. See the
included documentation and wxpython.org for more
information."""

    lic = """pyinstaller EXEcutor is free software; you can distribute
it and/or modify it under the terms of the GNU General
Public License as published by the Free Software
Foundation; either version 2 of the License, or (at
your option) any later version.

pyinstaller EXEcutor is distributed in the hope that
it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details at:
http://www.gnu.org/licenses/gpl-3.0.en.html."""

    
    info = wx.AboutDialogInfo()
    #info.SetIcon(wx.Icon('xxx.png', wx.BITMAP_TYPE_PNG))
    info.SetName('pyinstaller EXEcutor')
    info.SetVersion('1.0')
    info.SetDescription(description)
    info.SetCopyright('(C) 2016 Wesley Dopkins')
    #info.SetWebSite('http://wescraft.technology')
    info.SetLicense(lic)
    info.AddDeveloper('Wesley Dopkins')
    info.AddDocWriter('Wesley Dopkins')
    info.AddArtist('wescraft productions')
    info.AddTranslator('Wesley Dopkins')
    wx.AboutBox(info)

def helpFile(e):
    desc = """The following is a short guide to using the pyinstaller EXEcutor."""

    installation = """You can use the program without installing anything. However, for it to function
as intended, you need to perform the following steps:
1. Install Python 2.x or 3.x
2. Install pyinstaller using the Windows binary on the website.
3. Go to Control Panel -> System -> Advanced system settings -> Environment
Variables. Add the pyinstaller installation directory to the end of the 'Path'
system variable (e.g. C:\python27\scripts).
4. Run pyinstaller EXEcutor."""

    use = """
Creating an EXE with pyinstaller EXEcutor is as easy as 1-2-3:
1. Run this program
2. Select a script at the top of the screen
3. Click 'Convert!' at the bottom.

pyinstaller EXEcutor works by automatically generating the required command line
input that the actual pyinstaller expects, while providing the user with a human-
readable user interface. However, all options other than the script to convert
are optional.

The following is a short description of the options. More information is
available at the pyinstaller home page.

EXE file name: Specify a name for the executable (and .spec) file. Otherwise,
the script file name is used.

ICO file: Select an .ICO or .EXE file which will be used as the icon for the
application. If you select an .EXE, the icon is extracted for use.

Save app to: The compiled application is saved by default to ./dist. You can
select another directory here.

Work files in: The working files used to generate the application are saved by
default to ./build. You can select another directory here.

UPX util path: UPX is a third-party application that further compresses the
application. If you have it on your computer and want to use it, specify its
directory here.

Save .spec to: The .SPEC file is automatically saved to the current directory
by default. You can select another directory here.

Convert to one file: Select this option to generate a single executable (like
this program), instead of a directory with an EXE and several DLLs, etc.

Windowed mode: Similar to using a .pyw script. The program will execute without
opening a command line.

Replace output directory: Select this option to automatically overwrite existing
files without confirmation.

No unicode support: Strips unicode support (if any) from the generated EXE (not
recommended).

Clean cache before build: Clears the pyinstaller cache before building the
application.

Logging level: DO NOT USE - UNDER DEVELOPMENT. Provides options for logging
the application build process.

Don't use UPX: Forces pyinstaller not to use the UPX utility, regardless of
other options.

Create debug EXE: Creates an executable that, when run, provides logging
outputs at the DEBUG level.

Symbol-table strip EXE/libs: pyinstaller doesn't recommend using this option...

Run app as admin: Creates an executable that asks for administrator privileges
when run.

Elevated app for RDP: Creates an executable that runs at an elevated permissions
level, suitable for running in a remote desktop session.

Create private assemblies for app: AFAIK, stores all the Microsoft assemblies
internally to the application, rather than relying on them being installed on the
PC running it. Avoids certain version incompatibility problems.

Don't prefer assembly redirects: Similar to the previous option, see the
pyinstaller page for details.

Other arguments: Enter additional parameters for the call to this line. Click
'Editor' to open a larger window where you have more space to enter them, as
well as buttons to quickly enter all the other possible parameters I could find.

Convert!: Converts the .py or .pyw file to an executable, using the options
selected above.

When you click the Convert button, the text changes to 'Converting to EXE,
please wait...' or changes to an appropriate error message.

If the conversion completes properly, the program closes when it is done.
If there are errors that prevent creating an EXE, an error message is shown
and the program closes. If this occurs, check the logs for details."""

    dlg = wx.MessageDialog(win, desc + '\n\n' + installation + '\n\n' + use, 'pyinstaller EXEcutor documentation', wx.OK)
    
    dlg.ShowModal()

def selectFile(e):
    dlg = wx.FileDialog(None, 'Select File', '', '', '*.*', wx.OPEN)
    if dlg.ShowModal() == wx.ID_OK:
        if e.GetId() == 1:
            loadField.Value = dlg.GetPath()
        elif e.GetId() == 6:
            fieldIpath.Value = dlg.GetPath()
        dlg.Destroy()

def selectDir(e):
    dlg = wx.DirDialog(None, 'Select Directory')
    if dlg.ShowModal() == wx.ID_OK:
        if e.GetId() == 2:
            fieldDpath.Value = dlg.GetPath()
        elif e.GetId() == 3:
            fieldWpath.Value = dlg.GetPath()
        elif e.GetId() == 4:
            fieldUpath.Value = dlg.GetPath()
        elif e.GetId() == 5:
            fieldSpath.Value = dlg.GetPath()
        dlg.Destroy()

def inputHelper(e):
    """This opens a small editor with buttons to insert available miscellaneous CLI arguments."""
    def onOk(e):
        fieldMisc.Value = contents.Value
        dlg.Destroy()
    def onCancel(e):
        dlg.Destroy()
    def onP(e):
        contents.Value = contents.Value + ' -p '
    def onHImport(e):
        contents.Value = contents.Value + ' --hidden-import '
    def onAHooksDir(e):
        contents.Value = contents.Value + ' -additional-hooks-dir '
    def onRuntimeHook(e):
        contents.Value = contents.Value + ' --runtime-hook '
    def onExclude(e):
        contents.Value = contents.Value + ' --exclude-module '
    def onKey(e):
        contents.Value = contents.Value + ' --key '
    def onVFile(e):
        contents.Value = contents.Value + ' --version-file '
    def onManifest(e):
        contents.Value = contents.Value + ' -m '
    def onResource(e):
        contents.Value = contents.Value + ' -r '


        
    dlg = wx.Frame(win, title='Enter additional arguments', size = (600,400))
    panel = wx.Panel(dlg)
    contents = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)

    btnP = wx.Button(panel, label='-p')
    btnP.Bind(wx.EVT_BUTTON, onP)
    btnHImport = wx.Button(panel, label='--hidden-import')
    btnHImport.Bind(wx.EVT_BUTTON, onHImport)
    btnAHooksDir = wx.Button(panel, label='--additional-hooks-dir')
    btnAHooksDir.Bind(wx.EVT_BUTTON, onAHooksDir)
    btnRuntimeHook = wx.Button(panel, label='--runtime-hook')
    btnRuntimeHook.Bind(wx.EVT_BUTTON, onRuntimeHook)
    btnExclude = wx.Button(panel, label='--exclude-module')
    btnExclude.Bind(wx.EVT_BUTTON, onExclude)
    btnKey = wx.Button(panel, label='--key')
    btnKey.Bind(wx.EVT_BUTTON, onKey)
    btnVFile = wx.Button(panel, label='--version-file')
    btnVFile.Bind(wx.EVT_BUTTON, onVFile)
    btnManifest = wx.Button(panel, label='--manifest')
    btnManifest.Bind(wx.EVT_BUTTON, onManifest)
    btnResource = wx.Button(panel, label='--resource')
    btnResource.Bind(wx.EVT_BUTTON, onResource)
    
    btnOk = wx.Button(panel, id=wx.ID_OK)
    btnOk.Bind(wx.EVT_BUTTON, onOk)
    btnCancel = wx.Button(panel, id=wx.ID_CANCEL)
    btnCancel.Bind(wx.EVT_BUTTON, onCancel)

    eOne = wx.BoxSizer()
    eOne.Add(btnP, proportion=0, flag=wx.LEFT, border=5)
    eOne.Add(btnHImport, proportion=0, flag=wx.LEFT, border=5)
    eOne.Add(btnAHooksDir, proportion=0, flag=wx.LEFT, border=5)
    eOne.Add(btnRuntimeHook, proportion=0, flag=wx.LEFT, border=5)
    eOne.Add(btnExclude, proportion=0, flag=wx.LEFT, border=5)

    eTwo = wx.BoxSizer()
    eTwo.Add(btnKey, proportion=0, flag=wx.LEFT, border=5)
    eTwo.Add(btnVFile, proportion=0, flag=wx.LEFT, border=5)
    eTwo.Add(btnManifest, proportion=0, flag=wx.LEFT, border=5)
    eTwo.Add(btnResource, proportion=0, flag=wx.LEFT, border=5)
    
    eLast = wx.BoxSizer()
    eLast.Add(btnOk, proportion=0, flag=wx.LEFT, border=5)
    eLast.Add(btnCancel, proportion=0, flag=wx.LEFT, border=5)

    eVbox = wx.BoxSizer(wx.VERTICAL)
    eVbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.ALL | wx.ALL | wx.ALL, border=5)
    eVbox.Add(eOne, proportion=0, flag=wx.ALL, border=5)
    eVbox.Add(eTwo, proportion=0, flag=wx.ALL, border=5)
    eVbox.Add(eLast, proportion=0, flag=wx.ALL, border=5)

    panel.SetSizer(eVbox)
    dlg.Show()
    return




# GUI elements
# Line 0: menu items
# Line 1: load script
# Line 2-n: CLI options
# Line 'last': Convert button
app = wx.App()
win = wx.Frame(None, title='pyinstaller EXEcutor', size=(600,600))

# Initialize menu items
menubar = wx.MenuBar()
helpMenu = wx.Menu()
helpMenu.Append(100, '&About')
helpMenu.Append(200, '&Help')
win.Bind(wx.EVT_MENU, aboutDialog, id=100)
win.Bind(wx.EVT_MENU, helpFile, id=200)
menubar.Append(helpMenu, '&Help')
win.SetMenuBar(menubar)

bkg = wx.Panel(win)

loadLbl = wx.StaticText(bkg, label='Select a python script: ')
loadField = wx.TextCtrl(bkg)
loadBtn = wx.Button(bkg, id=1, label='Browse')
loadBtn.Bind(wx.EVT_BUTTON, selectFile)

# Options
lblAppName = wx.StaticText(bkg, label='EXE file name: ')
fieldAppName = wx.TextCtrl(bkg)
lblIpath = wx.StaticText(bkg, label='ICO file: ')
fieldIpath = wx.TextCtrl(bkg)
btnIpath = wx.Button(bkg, id=6, label='Browse')
btnIpath.Bind(wx.EVT_BUTTON, selectFile)

lblDpath = wx.StaticText (bkg, label='Save app to: ')
fieldDpath = wx.TextCtrl(bkg)
btnDpath = wx.Button(bkg, id=2, label='Browse')
btnDpath.Bind(wx.EVT_BUTTON, selectDir)
lblWpath = wx.StaticText(bkg, label='Work files in: ')
fieldWpath = wx.TextCtrl(bkg)
btnWpath = wx.Button(bkg, id=3, label='Browse')
btnWpath.Bind(wx.EVT_BUTTON, selectDir)

lblUpath = wx.StaticText (bkg, label='UPX util path: ')
fieldUpath = wx.TextCtrl(bkg)
btnUpath = wx.Button(bkg, id=4, label='Browse')
btnUpath.Bind(wx.EVT_BUTTON, selectDir)
lblSpath = wx.StaticText (bkg, label='Save .spec to: ')
fieldSpath = wx.TextCtrl(bkg)
btnSpath = wx.Button(bkg, id=5, label='Browse')
btnSpath.Bind(wx.EVT_BUTTON, selectDir)

oneFile = wx.CheckBox(bkg, label='Convert to one file')
windowed = wx.CheckBox(bkg, label='Windowed mode')
overwriteOutput = wx.CheckBox(bkg, label='Replace output directory')

noUnicode = wx.CheckBox(bkg, label='No unicode support')
cleanCache = wx.CheckBox(bkg, label='Clean cache before build')
lblLog = wx.StaticText(bkg, label='Logging level: ')
logopts = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'] #Several of these cause problems - fix later
loglevel = wx.ComboBox(bkg, value='', choices=logopts, style=wx.CB_READONLY)

noUpx = wx.CheckBox(bkg, label='Don\'t use UPX')
debugMode = wx.CheckBox(bkg, label='Create debug EXE')
strip = wx.CheckBox(bkg, label='Symbol-table strip EXE/libs')

uacAdmin = wx.CheckBox(bkg, label='Run app as admin')
uacUiaccess = wx.CheckBox(bkg, label='Elevated app for RDP')

privateAssemblies = wx.CheckBox(bkg, label='Create private assemblies for app')
noAssyRedirects = wx.CheckBox(bkg, label='Don\'t prefer assembly redirects')

lblMisc = wx.StaticText(bkg, label='Other arguments: ')
fieldMisc = wx.TextCtrl(bkg)
btnMisc = wx.Button(bkg, id=6, label='Editor')
btnMisc.Bind(wx.EVT_BUTTON, inputHelper)

# Convert button
toggle = True
convertBtn = wx.Button(bkg, label='Convert!')
convertBtn.SetFont(wx.Font(12,wx.DEFAULT, wx.NORMAL, wx.BOLD))
convertBtn.Bind(wx.EVT_BUTTON, createExe)
statusMsg = wx.StaticText(bkg, label='All options other than the script name are optional.')



#horizontal-vertical layout
lineOne = wx.BoxSizer()
lineOne.Add(loadLbl, proportion=0, flag=wx.LEFT, border=5)
lineOne.Add(loadField, proportion=1, flag=wx.EXPAND, border=5)
lineOne.Add(loadBtn, proportion=0, flag=wx.LEFT, border=5)

lineTwo = wx.BoxSizer()
lineTwo.Add(lblAppName, proportion=0, flag=wx.LEFT, border=5)
lineTwo.Add(fieldAppName, proportion=1, flag=wx.EXPAND, border=5)
lineTwo.Add(lblIpath, proportion=0, flag=wx.LEFT, border=10)
lineTwo.Add(fieldIpath, proportion=1, flag=wx.EXPAND, border=5)
lineTwo.Add(btnIpath, proportion=0, flag=wx.LEFT, border=5)

lineThree = wx.BoxSizer()
lineThree.Add(lblDpath, proportion=0, flag=wx.LEFT, border=5)
lineThree.Add(fieldDpath, proportion=1, flag=wx.EXPAND, border=5)
lineThree.Add(btnDpath, proportion=0, flag=wx.LEFT, border=5)
lineThree.Add(lblWpath, proportion=0, flag=wx.LEFT, border=10)
lineThree.Add(fieldWpath, proportion=1, flag=wx.EXPAND, border=5)
lineThree.Add(btnWpath, proportion=0, flag=wx.LEFT, border=5)

lineFour = wx.BoxSizer()
lineFour.Add(lblUpath, proportion=0, flag=wx.LEFT, border=5)
lineFour.Add(fieldUpath, proportion=1, flag=wx.EXPAND, border=5)
lineFour.Add(btnUpath, proportion=0, flag=wx.LEFT, border=5)
lineFour.Add(lblSpath, proportion=0, flag=wx.LEFT, border=10)
lineFour.Add(fieldSpath, proportion=1, flag=wx.EXPAND, border=5)
lineFour.Add(btnSpath, proportion=0, flag=wx.LEFT, border=5)

lineFive = wx.BoxSizer()
lineFive.Add(oneFile, proportion=0, flag=wx.LEFT, border=10)
lineFive.Add(windowed, proportion=0, flag=wx.LEFT, border=10)
lineFive.Add(overwriteOutput, proportion=0, flag=wx.LEFT, border=10)

lineSix = wx.BoxSizer()
lineSix.Add(noUnicode, proportion=0, flag=wx.LEFT, border=10)
lineSix.Add(cleanCache, proportion=0, flag=wx.LEFT, border=10)
lineSix.Add(lblLog, proportion=0, flag=wx.LEFT, border=10)
lineSix.Add(loglevel, proportion=0, flag=wx.LEFT, border=5)

lineSvn = wx.BoxSizer()
lineSvn.Add(noUpx, proportion=0, flag=wx.LEFT, border=10)
lineSvn.Add(debugMode, proportion=0, flag=wx.LEFT, border=10)
lineSvn.Add(strip, proportion=0, flag=wx.LEFT, border=10)

lineEight = wx.BoxSizer()
lineEight.Add(uacAdmin, proportion=0, flag=wx.LEFT, border=10)
lineEight.Add(uacUiaccess, proportion=0, flag=wx.LEFT, border=10)

lineNine = wx.BoxSizer()
lineNine.Add(privateAssemblies, proportion=0, flag=wx.LEFT, border=10)
lineNine.Add(noAssyRedirects, proportion=0, flag=wx.LEFT, border=10)

lineTen = wx.BoxSizer()
lineTen.Add(lblMisc, proportion=0, flag=wx.LEFT, border=5)
lineTen.Add(fieldMisc, proportion=1, flag=wx.EXPAND, border=5)
lineTen.Add(btnMisc, proportion=0, flag=wx.LEFT, border=5)

lineLast = wx.BoxSizer()
lineLast.Add(convertBtn, proportion=0, flag=wx.LEFT, border=5)
lineLast.Add(statusMsg, proportion=0, flag=wx.LEFT, border=5)


vBox = wx.BoxSizer(wx.VERTICAL)
vBox.Add(lineOne, proportion=0, flag=wx.EXPAND | wx.ALL, border = 10)
vBox.Add(lineTwo, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineThree, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineFour, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineFive, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineSix, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineSvn, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineEight, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineNine, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vBox.Add(lineTen, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)

vBox.Add(lineLast, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)

bkg.SetSizer(vBox)

win.Show()
app.MainLoop()

#call(installer + ' ' + script + ' ' + args, shell=True)
