from cx_Freeze import setup, Executable
import os
import sys

includes = []
include_files = [r"C:\Users\...\AppData\Local\Programs\Python\Python37\DLLs\tcl86t.dll",
                 r"C:\Users\...\AppData\Local\Programs\Python\Python37\DLLs\tk86t.dll"]
os.environ['TCL_LIBRARY'] = r'C:\Users\...\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\...\AppData\Local\Programs\Python\Python37\tcl\tk8.6'
base = 'Win32GUI' if sys.platform == 'win32' else None


setup(name='Calculator', version='0.1', description='My first Python calculator',
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables=[Executable(r'C:\Users\...\Desktop\pythON\cal\cal01.py', base=base)])
