# -*-coding:utf8;-*-
# created by Hundera Awoke
# May 28, 2023

import logging
from functools import cached_property

class BahireHasab:
    """Object for  finding the Holidays and lents in the Ethiopian Calendar
    Written by: Hundera Awoke
    Year : 2023 G.C.
    Copyright(c) 2023
    """
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
    def __init__(self, year, logger=None):
        self.year = year if year else 2016
        self.logger = logger or logging.getLogger(__name__)
        self.logger.debug(f"Initializing Bahre Hasab: Year: {year}")
        self.already_logged =False
        
    
    @property
    def wengelawi(self) -> str:
        """A function for findin the Wengelawi."""
        self.logger.debug(f"Calculating wengelawi for year: {self.year}")
        _ = self.WENGELAWI[(self.year + 5500) % 4]
        self.logger.debug(f"Wengelawi of {self.year} is {_}")
        return _

    @cached_property
    def medeb(self) -> int:
        """A function for finding medeb used in other calculations."""
        _medeb = (self.year + 5500) % 19
        already_logged = None
        if already_logged==None:
            already_logged = self.already_logged
        if not already_logged:
            self.logger.debug(f"Medeb Value returned: {_medeb}")
            already_logged=True
        return _medeb

    @cached_property
    def wenber(self) -> int:
        """A function for finding Wenber of the year."""
        _wenber = self.medeb -1
        already_logged = self.already_logged
        if not already_logged:
            self.logger.debug(f"Wenber Returned {_wenber}")
            already_logged = True
        return _wenber if self.medeb else 18

    @cached_property
    def abekte(self) -> int:
        """A function for finding the abekte used for other calculations."""
        _abekte = self.wenber * self.TINTE_ABEKTE
        if _abekte > 30:
            _abekte %= 30
        self.logger.debug(f"Returned Abekte: {_abekte}")
        return _abekte if _abekte else 30

    @property
    def metene_rabiet(self) -> int:
        """A function for finding metene rabiet"""
        _m = (self.year + 5500) // 4
        self.logger.debug(f"Calculated metene rabiet :{_m}")
        return _m

    @cached_property
    def metk(self) -> int:
        """A function for determinig metk used in other calculations."""
        _m = self.wenber * self.TINTE_METIK
        already_logged = self.already_logged
        if not already_logged:
            self.logger.debug(f"Calulated metk: {_m}")
            already_logged = True
        self.already_logged = False
        return _m % 30 if _m else 30

    @property
    def beale_metk(self) -> str:
        """A function for finding the date of beale metk used for other calculations."""
        metk = self.metk
        # self.logger.debug(f"Getting the metk: {metk}")
        # already_logged = self.already_logged
        if 15 <= metk <= 30:
            beale_metk = f"መስከረም {self.metk}"
        elif 2 <= metk <= 14:
            beale_metk = f"ጥቅምት {self.metk}"
        # if not already_logged:
        #     self.logger.debug(f"Returned beale metk: {beale_metk}")
        #     already_logged = True
        return beale_metk
    def elete_ken(self, elet) -> str:
        """A function for determinig the day name of the given date in Ethiopian Calendar. Input in mm/dd format"""
        elet = [i for i in elet.split()]
        atsfe_wer = (self.WERAT.index(elet[0]) + 1) * 2
        tnete_yon = (self.metene_rabiet + self.year + 5500) % 7 - 1
        already_logged = self.already_logged
        if not already_logged:
            self.logger.debug(f"Getting elet :{elet}")
            self.logger.debug(f"Getting atsfewer: {atsfe_wer}")
            self.logger.debug(f"Getting tnteyon: {tnete_yon}")
            already_logged = True
        ken = int(elet[-1])
        _ = (ken + tnete_yon + atsfe_wer) % 7
        self.logger.debug(f"Returning elete_ken: {_}")
        return self.ELETAT[_]

    @property
    def new_year(self):
        """A function for determining the day of the Ethiopian New year not the date but its name."""
        amete_alem = self.year + 5500
        _ = (amete_alem + self.metene_rabiet + 2) % 7
        return self.ELETAT[_]

    @property
    def mebaja_hamer(self):
        """A function for finding mebaja hamer important for other calculations."""
        _mh = self.metk + self.ELET_TEWSAK.get(self.elete_ken(self.beale_metk))
        return _mh

    @property
    def neneweh(self) -> str:
        """A function for finding the date of Nenewh Lent."""
        _l = [i for i in self.beale_metk.split()]
        _mh = self.mebaja_hamer
        if _mh > 30:
            _w = "የካቲት"
            _mh %= 30
        elif self.metk == 30 or self.metk == 0:
            _w = "የካቲት"
        elif _l[0] == "መስከረም":
            _w = "ጥር"
        else:
            _w = "የካቲት"
        return f"{_w} {_mh}"

    def atswamat_webealat(self, beal) -> str:
        """A function for finding the respective events or Bealat in Ethiopian Calendar."""
        self.logger.debug(f"Calculating the date of : {beal}")
        _bt = self.BEALAT_TEWSAK[self.BEALAT.index(beal)]
        if _bt == 0:
            return self.neneweh
        _nw, _nk = [_ for _ in self.neneweh.split()]
        _nk = int(_nk)
        _bk = _nk + _bt
        if _bk % 30 == 0:
            _bw = self.WERAT[self.WERAT.index(_nw) + (_bk // 30) - 1]
        else:
            _bw = self.WERAT[self.WERAT.index(_nw) + (_bk // 30)]
        _bk = _bk % 30 if _bk % 30 else 30
        self.logger.debug(f"Returned: {_bw} {_bk}")
        return f"{_bw} {_bk}"

    @property
    def abiy_tsom(self):
        """A Function for finding the day of enterance of the Great lent according to the Ethiopian Calendar."""
        return self.atswamat_webealat(beal=self.BEALAT[1])

    @property
    def debre_zeyt(self):
        """A function for finding the date of debrezeyt(The middle of Great lent)."""
        return self.atswamat_webealat(beal=self.BEALAT[2])

    @property
    def hosaena(self):
        """A function for calculating the date of Hosaena in Ethiopian Calendar"""
        return self.atswamat_webealat(beal=self.BEALAT[3])

    @property
    def sklet(self):
        """A function for calculating the date of Sklet(Crufication) in Ethiopian Calendar."""
        return self.atswamat_webealat(beal=self.BEALAT[4])

    @property
    def tnsae(self):
        """A function for calculating the date of Tnsae(The end of Great lent) in Ethiopian Calendar."""
        return self.atswamat_webealat(beal=self.BEALAT[5])

    @property
    def rkbe_kahnat(self):
        """A function for calculating the date of rkbe kahnat(The meeting of Priests) in Ethiopian Calendar."""
        return self.atswamat_webealat(beal=self.BEALAT[6])

    @property
    def erget(self):
        """A function for calculating the date of Erget in Ethiopian Calendar."""
        return self.atswamat_webealat(beal=self.BEALAT[7])

    @property
    def beale_hamsa(self):
        """A function for calculating the date of Beale hamsa in Ethiopian Calendar."""
        return self.atswamat_webealat(beal=self.BEALAT[8])

    @property
    def tsome_hawaryat(self):
        """A function for finding the date of Tsome Hawaryat (Lent of The Apostels) in Ethiopian Calendar."""
        return self.atswamat_webealat(beal=self.BEALAT[9])

    @property
    def tsome_dhnet(self):
        return self.atswamat_webealat(beal=self.BEALAT[10])
