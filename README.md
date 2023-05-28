<h1 align="center">📆 Bahire Hassab(ባህረ ሐሳብ) 🇪🇹 📦 </h1>

 [![Upload Python Package](https://github.com/hunderaweke/bahire-hasab/actions/workflows/python-publish.yml/badge.svg)](https://github.com/hunderaweke/bahire-hasab/actions/workflows/python-publish.yml)
 
 
- A python module for calculating Ethiopian Holidays and Lents
## Table Of Content
- [Table Of Content](#table-of-content)
- [Description](#description)
- [Installation](#installation)
- [Documentation](#documentation)
- [Todo](#todo)
## Description
- This is a python Installation module for Ethiopian Calender method for determining the dates of lents and holidays or in Amharic Bahire Hassab ባህረ ሐሳብ
- I have used the native calculation method If you want the book I used you can find it [](#)
- Each of the names I used in the module is mostly the Amharic Equivalent of the holiday if you want all you can get it <a href="https://drive.google.com/file/d/1e7AukagokWlEiuz_0YtZ8Oz3RcUoQaLC/view?usp=sharing" target="_blank">Click Here!</a>.
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
eth_easter = bh.tnsae
print(eth_easter)# ሚያዚያ 8 this is for the Ethiopian year 2015
# This is should print the date of the Ethiopian Easter according to the Ethiopian Calendar
```
- The method names are home how different from most methods that we know since I used most of them in Amharic there is their Equivalent in English

|Method|English Equivalent|Description|
|:-----|:-----------:  |     :----|
|new_year|Ethiopian New Year|The day of new year in Amharic|
|abiy_tsome|Ethiopian Great Lent Begin|The day at which the great lent begin in Ethiopia|
|neneweh|Ethiopian Fast of Neneviah|The Day of begining of the Neneviah fast|
|debre_zeyt|Ethiopian Great lent middle|The middle day of the Ethiopian Great lent|
|hosaena|Ethiopian Hoseana|The day of Entrance of Jesus to Jerusalem in Ethiopian Calender|
|sklet|The holy Friday|The day of holyfriday in Ethiopian Calender.|
|tnsae|Ethiopian Easter|The day of Easter in Ethiopian Calender.|
|rkbe_kahnat| - | - |
|erget|The day of ascension|Returns the day of ascension of the year.|
|beale_hamsa|The Pentecost|Returens the day of Pentecost of the year.|
|tsome_hawaryat|-|-|
|tsome_dhnet|-|-|


## Todo
- [x] Releasing the package to pypi.org
- [ ] Making API for it
- [ ] Support for Gregorian Calender
- [x] Finding corner Canses  
