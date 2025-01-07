import PyInstaller.__main__

PyInstaller.__main__.run([
    'Jarvis_main.py',
    '--onefile',
    '--name=Jarvis',
    '--clean',
    '--add-data=GreetMe.py;.',
    '--add-data=FocusMode.py;.',
    '--add-data=FocusGraph.py;.',
    '--add-data=game.py;.',
    '--add-data=focus.txt;.',
    '--exclude-module=cryptography',
    '--exclude-module=_cffi_backend',
    '--exclude-module=rust_x509',
    '--exclude-module=speedtest_cli',
]) 