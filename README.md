# TWMigrationBot

## Supported environments
This bot is only designed to work on Ubuntu 16.04 using Python 3.7.3. Limited support will be provided for other operating environments.


## Setting up
To start, download pywikibot. Instructions can be found here:
    https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Python

To use pywikibot, ensure pywikibot.pywikibot is in the PYTHONPATH.
    export PYTHONPATH="$PYTHONPATH:PATH_TO_PYWIKIBOT"

### Helpful configurations
In user-config.py some settings can be changed to make the bot operate faster: these should be reasonably high to avoid overloading the server.

    minthrottle = 0
    maxthrottle = 5
    put_throttle = 2

