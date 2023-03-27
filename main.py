


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


tewsak = {'kidame': 8, 'ehud': 7, 'segno': 6,
          'magsegno': 5, 'rebue': 4, 'hamus': 3, 'arb': 2}


def findBealeMetk(metk):
    if metk >= 15 and metk <= 30:
        beale_metk = {f'መስከርም {metk}': 1}
    elif metk >= 2 and metk <= 14:
        beale_metk = {f'ጥቅምት {metk}': 2}
    return beale_metk


def findMebajaHamer(metk):
    pass


def findAmeteWengelawe(year):
    keri = (year+5500) % 4
    match keri:
        case 1:
            wengelawe = ["Mathewos", 1]
        case 2:
            wengelawe = ["Markos", 2]
        case 3:
            wengelawe = ["Lukas", 3]
        case 0:
            wengelawe = ["Yohans", 0]
    return wengelawe


def findMeskerem1(year):
    tnte_kemer = (((year+5500)//4)+(year+5500)) % 7
    match tnte_kemer:
        case 1:
            day = "Magsegno"
        case 2:
            day = "Rebue"
        case 3:
            day = "Hamus"
        case 4:
            day = "Arb"
        case 5:
            day = "Kidame"
        case 6:
            day = "Ehud"
    return day


if '__main__' == __name__:
    print(findMeskerem1(2006))
    print(findAmeteWengelawe(year=2006))
    medeb = findMedeb(2006)
    wenber = findWenber(medeb)
    abekte = findAbekte(wenber)
    metk = findMetk(wenber)
    print(findBealeMetk(metk))
