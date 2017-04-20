#!/usr/local/bin/python3

import webbrowser
#webbrowser.open('http://www.python.org')

c = webbrowser.get('chromium')
c.open('http://www.python.org')
c.open_new_tab('http://www.brainwerkz.com')
