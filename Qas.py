import os,platform
try:
    import requests
except ImportError:
    print ("Installing Module Requests...")
    os.system("pip2 install requests")
bit=platform.architecture()[0]
if bit=="64bit":
    import kb
    kb.police()
elif bit=="32bit":
    import kb
    kb.police()
