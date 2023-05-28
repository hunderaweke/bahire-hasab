class BahireHasab:
    TINTE_METIK = 49 % 30
    TINTE_ABEKTE = 161 % 30
    WERAT = [
        "መስከረም",
        "ጥቅምት",
        "ኅዳር",
        "ታኅሣስ",
        "ጥር",
        "የካቲት",
        "መጋቢት",
        "ሚያዝያ",
        "ግንቦት",
        "ሰኔ",
        "ሐምሌ",
        "ነሐሴ",
        "ጷግሜ",
    ]
    WENGELAWI = ["ዮሐንስ", "ማቴዎስ", "ማርቆስ", "ሉቃስ"]
    ELET_TEWSAK = {"ሰኞ": 6, "ማክሰኞ": 5, "ረቡዕ": 4, "ሐሙስ": 3, "አርብ": 2, "ቅዳሜ": 8, "እሑድ": 7}
    ELETAT = ["ቅዳሜ", "እሑድ", "ሰኞ", "ማክሰኞ", "ረቡዕ", "ሐሙስ", "አርብ"]
    BEALAT_TEWSAK = [0, 14, 41, 62, 67, 69, 93, 108, 118, 119, 121]
    BEALAT = [
        "ጾመ ነነዌ",
        "ዐብይ ጾም",
        "ደብረ ዘይት",
        "ሆሳዕና",
        "ስቅለት",
        "ትንሳኤ",
        "ርክበ ካሕናት",
        "ዕርገት",
        "በዓለ ሀምሳ",
        "ጾመ ሐዋርያት",
        "ጾመ ድኅነት",
    ]

    ELETE_KEN = ["ረቡዕ", "ሐሙስ", "አርብ", "ቅዳሜ", "እሑድ", "ሰኞ", "ማክሰኞ"]

    def __init__(self, year):
        self.year = year if year else 2016

    @property
    def wengelawi(self) -> str:
        """A function for findin the Wengelawi."""
        _ = self.WENGELAWI[(self.year + 5500) % 4]
        return _

    @property
    def medeb(self) -> int:
        medeb = (self.year + 5500) % 19
        return medeb

    @property
    def wenber(self) -> int:
        wenber = self.medeb - 1
        return wenber if self.medeb else 18

    @property
    def abekte(self) -> int:
        abekte = self.wenber * self.TINTE_ABEKTE
        if abekte > 30:
            abekte %= 30
        return abekte if abekte else 30

    @property
    def metene_rabiet(self) -> int:
        _m = (self.year + 5500) // 4
        return _m

    @property
    def metk(self) -> int:
        _m = self.wenber * self.TINTE_METIK
        return _m % 30 if _m else 30

    @property
    def beale_metk(self) -> str:
        metk = self.metk
        if 15 <= metk <= 30:
            beale_metk = f"መስከረም {self.metk}"
        elif 2 <= metk <= 14:
            beale_metk = f"ጥቅምት {self.metk}"
        return beale_metk

    def elete_ken(self, elet) -> str:
        elet = [i for i in elet.split()]
        atsfe_wer = (self.WERAT.index(elet[0]) + 1) * 2
        tnete_yon = (self.metene_rabiet + self.year + 5500) % 7 - 1
        ken = int(elet[-1])
        _ = (ken + tnete_yon + atsfe_wer) % 7
        print(_)
        return self.ELETAT[_]

    @property
    def new_year(self):
        amete_alem = self.year + 5500
        _ = (amete_alem + self.metene_rabiet + 2) % 7
        return self.ELETAT[_]

    @property
    def mebaja_hamer(self):
        _mh = self.metk + self.ELET_TEWSAK.get(self.elete_ken(self.beale_metk))
        return _mh

    @property
    def neneweh(self) -> str:
        _l = [i for i in self.beale_metk.split()]
        _mh = self.mebaja_hamer
        if _mh > 30:
            _w = "የካቲት"
            _mh % 30
        elif self.metk == 30 or self.metk == 0:
            _w = "የካቲት"
        elif _l[0] == "መስከረም":
            _w = "ጥር"
        else:
            _w = "የካቲት"
        return f"{_w} {_mh}"

    def beal(self, beal) -> str:
        _bt = self.BEALAT_TEWSAK[self.BEALAT.index(beal)]
        if _bt == 0:
            return self.neneweh
        _nw, _nk = [_ for _ in self.neneweh.split()]
        _nk = int(_nk)
        _bk = _nk + _bt
        _bw = self.WERAT[self.WERAT.index(_nw) + (_bk // 30)]
        _bk = _bk % 30 if _bk > 30 else _bk
        return f"{_bw} {_bk}"
