from Awm import login
login()
import os

try:

    import requests

except ImportError:

    print('\ [✓] installing requests !...\')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\ [✓] installing futures !...\')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\ [✓] installing bs4 !...\')

    os.system('pip install bs4')
