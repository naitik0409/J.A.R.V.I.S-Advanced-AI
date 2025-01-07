import os
import shutil
import PyInstaller.__main__

# Clean up previous builds
if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('dist'):
    shutil.rmtree('dist')

# Run PyInstaller
PyInstaller.__main__.run([
    'Jarvis_main.py',
    '--onefile',
    '--clean',
    '--name=Jarvis',
    '--add-data=GreetMe.py;.',
    '--add-data=FocusMode.py;.',
    '--add-data=FocusGraph.py;.',
    '--add-data=game.py;.',
    '--add-data=focus.txt;.',
    '--hidden-import=pyttsx3.drivers',
    '--hidden-import=pyttsx3.drivers.sapi5',
    '--hidden-import=pygame',
    '--hidden-import=speech_recognition',
    '--hidden-import=numpy',
    '--hidden-import=PIL',
    '--hidden-import=matplotlib',
    '--exclude-module=cryptography',
    '--exclude-module=_cffi_backend',
    '--exclude-module=rust_x509',
    '--exclude-module=speedtest_cli',
]) 