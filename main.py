

def findMedeb(year) -> int:
    medeb = (year+5500) % 19
    return medeb


def findWenber(medeb) -> int:
    wenber = medeb-1 if medeb > 0 else 18
    return wenber


def findAbekte(wenber) -> int:
    abekte = wenber*11
    if abekte > 30:
        abekte -= 30
    else:
        pass
    return abekte


def findMetk(wenber) -> int:
    abekte = findAbekte(wenber)
    metk = abs(abekte-30)
    return metk


tewsak = {'ቅዳሜ': 8, 'እሁድ': 7, 'ሰኞ': 6,
          'ማግሰኞ': 5, 'ረቡዕ': 4, 'ሐሙስ': 3, 'አርብ': 2}


def findBealeMetk(metk):
    if metk >= 15 and metk <= 30:
        beale_metk = {f'መስከርም {metk}': 1}
    elif metk >= 2 and metk <= 14:
        beale_metk = {f'ጥቅምት {metk}': 2}
    return beale_metk


def findDay(year, month, date):
    meskerem1 = findMeskerem1(year)
    tnteYon = {'ረቡዕ': 1, 'ሐሙስ': 2, 'አርብ': 3,
               'ቅዳሜ': 4, 'እሁድ': 5, 'ሰኞ': 6, 'ማግሰኞ': 7}
    tnte_yon = tnteYon[meskerem1]
    astfe_wer = month*2
    day = (date+astfe_wer+tnte_yon) % 7
    match day:
        case 1:
            day = "እሁድ"
        case 2:
            day = "ሰኞ"
        case 3:
            day = "ማግሰኞ"
        case 4:
            day = "ረቡዕ"
        case 5:
            day = "ሐሙስ"
        case 6:
            day = "አርብ"
        case 0:
            day = "ቅዳሜ"
    return day


def findMebajaHamer(metk):
    pass


def findAmeteWengelawe(year):
    keri = (year+5500) % 4
    match keri:
        case 1:
            wengelawe = "ማቴዎስ"
        case 2:
            wengelawe = "ማርቆስ"
        case 3:
            wengelawe = "ሉቃስ"
        case 0:
            wengelawe = "ዮሐንስ"
    return wengelawe


def findMeskerem1(year):
    tnte_kemer = (((year+5500)//4)+(year+5500)) % 7
    tnteKemer = {2: 'ረቡዕ', 3: 'ሐሙስ', 4: 'አርብ',
                 5: 'ቅዳሜ', 6: 'እሁድ', 0: 'ሰኞ', 1: 'ማግሰኞ'}
    day = tnteKemer[tnte_kemer]
    return day


if '__main__' == __name__:
    year, month, date = [int(i) for i in input("Date: ").split('/')]
    print(findDay(year, month, date))
