<h1 align="center">📆 Bahire Hassab(ባህረ ሐሳብ) 🇪🇹 📦 </h1>

## Table Of Content
- [Description](#description)
- [Installation](#installation)
- [Documentation](#documentation)
- [Todo](#todo)
## Description
- This is a python Installation module for Ethiopian Calender method for determining the dates of lents and holidays or in Amharic Bahire Hassab ባህረ ሐሳብ
- I have used the native calculation method If you want the book I used you can find it [](#)
- Each of the names I used in the module is mostly the Amharic Equivalent of the holiday if you want all you can get it [here](#).
## Installation
- Bahire Hassab is available now on [](#https://pypi.org/)
- You can Install it through pip by
 ```pip
 pip install bahire-hassab
 ```
## Documentation
- There is a snippet how to use it for your personal projects
```python
from bahire_hasab import BahireHasab
from detetime import detetime
# The year according to the Ethiopian Calender
year = datetime.now().year -8
bh = BahireHasab(year)
eth_easter = bh.tnsea
print(eth_easter)
# This is should print the date of the Ethiopian Easter according to the Ethiopian Calendar
```
- The method names are home how different from most methods that we know since I used most of them in Amharic there is their Equivalent in English

|Method|English Equivalent|Description|
|:-----|:-----------:  |     :----|
|new_year|Ethiopian New Year|The day of new year in Amharic|
|meskel|Ethiopian Feast of Cross|The Date of the feast of cross in Amharic|
## Todo
- [x] Releasing the package to pypi.org
- [ ] Making API for it
- [ ] Support for Gregorian Calender
- [ ] Finding corner Canses  
