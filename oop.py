# Author: Hundera Awoke
# Date: 26/5/2023 G.C.
# Copyright
class Calendar:
    def __init__(self, ametemihret) -> None:
        self.ametemihret = ametemihret
        self.amete_alem = self.ametemihret + 5500
        self.wengelawi_dic = {1: "ማቴዎስ", 2: "ማርቆስ", 3: "ሉቃስ", 4: "ዮሐንስ"}
        self.months = {
            "መስከረም": 1,
            "ጥቅምት": 2,
            "ህዳር": 3,
            "ታህሳስ": 4,
            "ጥር": 5,
            "የካቲት": 6,
            "መጋቢት": 7,
            "ሚያዚያ": 8,
            "ግንቦት": 9,
            "ሰኔ": 10,
            "ሐምሌ": 11,
            "ነሀሴ": 12,
            "ጳጉሜን": 13,
        }
        self.wengelawi_key = self.amete_alem % 4
        self.wengelawi = self.wengelawi_dic[self.wengelawi_key]
        self.medeb = self.amete_alem % 19
        self.wenber = self.medeb - 1 if self.medeb > 0 else 18
        self.abekte = self.wenber * 11
        if self.abekte > 30:
            self.abekte %= 30
        self.metk = abs(30 - self.abekte)
        self.tnte_kemer = ((self.amete_alem // 4) + self.amete_alem) % 7

    def find_beale_metk(self):
        """A Function For Findein"""
        metk = self.metk
        if metk > 30:
            metk = metk - 30
        if metk >= 15 and metk <= 30:
            self.beale_metk = f"መስክረም {metk}"
        elif metk >= 2 and metk <= 14:
            self.beale_metk = f"ጥቅምት{metk}"
        return self.beale_metk

    def find_day_name(self, month_date_string: str) -> str:
        """A function for finding the name of the day of a given date in mm/dd format"""
        days = {1: "እሁድ", 2: "ሰኞ", 3: "ማክሰኞ", 4: "ረቡዕ", 5: "ሐሙስ", 6: "አርብ", 0: "ቅዳሜ"}
        month, date = [_ for _ in month_date_string.split()]
        date = int(date)
        tnte_yon = (((self.amete_alem // 4) + (self.amete_alem)) % 7) - 1
        months = self.months
        doubled_month = 2 * (months[month])
        sum_akt = doubled_month + date + tnte_yon
        sum_akt %= 7
        self.day = days[sum_akt]
        return self.day

    def find_mebaja_hamer(self) -> int:
        beale_metk = self.beale_metk
        TEWSAK = {"ቅዳሜ": 8, "እሁድ": 7, "ሰኞ": 6, "ማግሰኞ": 5, "ረቡዕ": 4, "ሐሙስ": 3, "አርብ": 2}
        day = Calendar.find_day_name(self, beale_metk)
        metk = self.metk
        tewsak = TEWSAK[day]
        self.mebaja_hamer = tewsak + metk if tewsak + metk < 30 else tewsak
        return self.mebaja_hamer

    def find_new_year(self) -> str:
        "A function for finding the name of the day of Ethiopian New Year according to Ethiopian Calendar."
        tnte_kemer_key = self.tnte_kemer
        tnte_kemer_dic = {
            2: "ረቡዕ",
            3: "ሐሙስ",
            4: "አርብ",
            5: "ቅዳሜ",
            6: "እሁድ",
            0: "ሰኞ",
            1: "ማግሰኞ",
        }
        self.new_year = tnte_kemer_dic[tnte_kemer_key]
        return self.new_year

    def find_neneweh(self) -> str:
        "A function for finding the day of tsome Neneweh"
        if 15 <= self.mebaja_hamer <= 30:
            month = "ጥር"
        else:
            month = "የካቲት"
        self.neneweh = f"{month} {self.mebaja_hamer}"

    def find_abiy_tsome(self) -> str:
        "A Function for finding the day of enterance of the Great lent according to the Ethiopian Calendar."
        abiy_tsome_tewsak = 14 + self.mebaja_hamer
        if abiy_tsome_tewsak > 30:
            abiy_tsome_tewsak -= 30
        abiy_tsome_wer = "የካቲት"
        self.abiy_tsome = f"{abiy_tsome_wer} {abiy_tsome_tewsak}"
        return self.abiy_tsome

    def find_debrezeyt(self) -> str:
        "A function for finding the date of debrezeyt(The middle of Great lent)."
        month, date = [_ for _ in self.neneweh.split()]
        date = int(date)
        debrezeyt_date = (date + 41) % 30
        debrezeyt_month = (
            "መጋቢት" if month == "የካቲት" or (month == "ጥር" and date >= 20) else "የካቲት"
        )
        self.debrezeyt = f"{debrezeyt_month} {debrezeyt_date}"
        return self.debrezeyt

    def find_hosaena(self) -> str:
        "A function for calculating the date of Hosaena in Ethiopian Calendar"
        month, date = [_ for _ in self.neneweh.split()]
        date = int(date)
        hosaena_date = (date + 62) % 30
        hosaena_month = "መጋቢት" if (month == "ጥር" and date <= 17) else "ሚያዚያ"
        self.hosaena = f"{hosaena_month} {hosaena_date}"
        return self.hosaena

    def find_seklet(self) -> str:
        "A function for calculating the date of Sklet(Crufication) in Ethiopian Calendar."
        month, date = [_ for _ in self.hosaena.split()]
        date = int(date)
        sklet_date = date + 5
        if sklet_date > 30:
            sklet_date -= 30
        self.sklet = f"{month} {date}"
        return self.sklet

    def find_tnsae(self) -> str:
        "A function for calculating the date of Tnsae(The end of Great lent) in Ethiopian Calendar."
        month, date = [_ for _ in self.sklet.split()]
        date = int(date)
        tnsae_date = date + 2
        self.tnsae = f"{month} {tnsae_date}"
        return self.tnsae

    def find_rkbe_kahnat(self) -> str:
        "A function for calculating the date of rkbe kahnat(The meeting of Priests) in Ethiopian Calendar."
        month, date = [_ for _ in self.tnsae.split()]
        date = int(date)
        rkbe_kahnat_date = date + 24
        if (
            month == "መጋቢት"
            and (54 >= date >= 50)
            or (month == "ሚያዚያ" and 30 >= date >= 24)
        ):
            rkbe_kahnat_month = "ሚያዚያ"
        else:
            rkbe_kahnat_month = "ግንቦት"
        rkbe_kahnat_date %= 30
        self.rkbe_kahnat = f"{rkbe_kahnat_month} {rkbe_kahnat_date}"
        return self.rkbe_kahnat

    def find_erget(self) -> str:
        "A function for calculating the date of Erget in Ethiopian Calendar."
        month, date = [_ for _ in self.rkbe_kahnat.split()]
        date = int(date)
        erget_date = date + 15
        if (month == "ሚያዚያ" and 45 >= date >= 35) or (
            month == "ግንቦት" and 15 >= date >= 1
        ):
            erget_month = "ግንቦት"
        else:
            erget_month = "ሰኔ"
        erget_date %= 30
        self.erget = f"{erget_month} {erget_date}"
        return self.erget
