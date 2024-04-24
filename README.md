# Usage
The usage of this portscanner is really simple. You´ll need the following libraries:
```
import socket
import time
from termcolor import colored
```
They also can be found in the requirements.txt. This is the command for installing the requirement:
```
pip install -r requirements.txt
```
Or:
```
pip install termcolor
```
When installed with pip, you can start the script by opening a terminal and navigating to the corresponding folder.
Then type the following:

```
python portscanner.py
```

You will be prompted to input any informations needed. It will then go through the given ports and give you a colored feedback on what ports are open (green) ore closed (red).
I´ve compiled the .py file into an .exe too but that doesn´t write the output-file. That is because you have to enter your own path in line 20 of the script.

After you´ve done that, you can compile it yourself using the following commands:

```
pip install pyinstaller
pyinstaller --onefile -F portscanner.py
```
