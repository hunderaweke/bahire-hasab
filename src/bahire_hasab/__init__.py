# Author: Hundera Awoke
# Date: 26/5/2023 G.C.
# Copyright
class BahireHasab:
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
            "ነሐሴ": 12,
            "ጳጉሜን": 13,
        }
        self.wengelawi_key = self.amete_alem % 4
        if self.wengelawi_key ==0:
            self.wengelawi_key = 4
        self.wengelawi = self.wengelawi_dic[self.wengelawi_key]
        self.medeb = self.amete_alem % 19
        self.wenber = self.medeb - 1 if self.medeb > 0 else 18
        self.abekte = self.wenber * 11
        if self.abekte > 30:
            self.abekte %= 30
        self.metk = abs(30 - self.abekte)
        self.beale_metk = self.find_beale_metk()
        self.mebaja_hamer = self.find_mebaja_hamer()
        self.tnte_kemer = ((self.amete_alem // 4) + self.amete_alem) % 7
        self.new_year=self.find_new_year()
        self.neneweh = self.find_neneweh()
        self.abiy_tsome = self.find_abiy_tsome()
        self.hosaena = self.find_hosaena()
        self.seklet = self.find_seklet()
        self.tnsae = self.find_tnsae()
        self.rkbe_kahnat= self.find_rkbe_kahnat()
        self.erget = self.find_erget()
        self.beale_hamsa = self.find_beale_hamsa()
        self.tsome_hawaryat = self.find_tsome_hawaryat()
        self.tsome_dihinet = self.find_tsome_dhnet()
        self.gena = (
            f"{self.find_day_name('ታህሳስ 29')} ታህሳስ 29"
            if self.wengelawi != "ዘመነ ዮሐንስ"
            else f"{self.find_day_name('ታህሳስ 28')} ታህሳስ 28"
        )
        self.timket = f"{self.find_day_name('ጥር 11')} ጥር 11"
        self.kana_zegelila = f"{self.find_day_name('ጥር 12')} ጥር 12"
        self.meskel = f"{self.find_day_name('መስከረም 17')} መስከረም 17"
        self.beale_tsinset = f"{self.find_day_name('መጋቢት 29')} መጋቢት 29"
        self.beale_simeon = f"{self.find_day_name('የካቲት 8')} የካቲት 8"
        self.beale_gizret = f"{self.find_day_name('ጥር 6')} ጥር 6"
        self.genbot_lideta = f"{self.find_day_name('ግንቦት 1')} ግንቦት 1"
        self.debre_tabor = f"{self.find_day_name('ነሐሴ 13')} ነሐሴ 13"
        self.tsome_lidet = (
            f"{self.find_day_name('ህዳር 15')} ህዳር 16"
            if self.wengelawi!= "ዘመነ ዮሐንስ"
            else f"{self.find_day_name('ህዳር 15')} ህዳር 15"
        )
        self.day_of_timket = self.find_day_name("ጥር 11")
        self.tsome_gehad = (
            f"{self.find_day_name('ጥር 10')} ጥር 10"
            if self.day_of_timket == "አርብ" or self.day_of_timket == "ረቡዕ"
            else "የለም"
        )
        self.tsome_filseta = f"{self.find_day_name('ነሐሴ 1')} ነሐሴ 1"
        self.tsome_filseta_mefchiya = f"{self.find_day_name('ነሐሴ 16')} ነሐሴ 16"
        self.debre_zeyit = self.find_debrezeyt()

    def find_beale_metk(self):
        """A Function For Finding the Beale metk"""
        metk = self.metk
        if metk > 30:
            metk = metk - 30
        if metk >= 15 and metk <= 30:
            self.beale_metk = f"መስከረም {metk}"
        elif metk >= 2 and metk <= 14:
            self.beale_metk = f"ጥቅምት {metk}"
        return self.beale_metk
    def find_new_year(self) -> str:
        "A function for finding the name of the day of Ethiopian New Year according to Ethiopian Calendar."
        self.tnte_kemer = ((self.amete_alem // 4) + self.amete_alem) % 7
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

    def find_day_name(self, month_date_string: str) -> str:
        """A function for finding the name of the day of a given date in mm/dd format"""
        tnte_yon_new_year = {"ረቡዕ":1,"ሐሙስ":2,"አረብ":3,"ቅዳሜ":4,"እሀድ":5,"ሰኞ":6,"ማግሰኞ":7}
        self.new_year = self.find_new_year()
        days = {1: "እሁድ", 2: "ሰኞ", 3: "ማክሰኞ", 4: "ረቡዕ", 5: "ሐሙስ", 6: "አርብ", 0: "ቅዳሜ"}
        month, date = [_ for _ in month_date_string.split()]
        date = int(date)
        tnte_yon = (((self.amete_alem // 4) + (self.amete_alem)) % 7)-1
        months = self.months
        doubled_month = 2 * (months[month])
        sum_akt = doubled_month + date + tnte_yon
        if sum_akt > 7:
            sum_akt %= 7
        self.day = days[sum_akt]
        return self.day

    def find_mebaja_hamer(self) -> int:
        beale_metk = self.beale_metk
        TEWSAK = {"ቅዳሜ": 8, "እሁድ": 7, "ሰኞ": 6, "ማግሰኞ": 5, "ረቡዕ": 4, "ሐሙስ": 3, "አርብ": 2}
        self.day = self.find_day_name(month_date_string= beale_metk)
        metk = self.metk
        tewsak = TEWSAK[self.day]
        print(metk)
        self.mebaja_hamer = tewsak + metk if tewsak + metk < 30 else tewsak
        return self.mebaja_hamer 

    def find_neneweh(self) -> str:
        "A function for finding the day of tsome Neneweh"
        if 15 <= self.mebaja_hamer <= 30:
            month = "ጥር"
        else:
            month = "የካቲት"
        self.neneweh = f"{month} {self.mebaja_hamer}"
        return self.neneweh

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
        hosaena_month = "መጋቢት" if (month == "ጥር" and 17<= hosaena_date <= 28) else "ሚያዚያ"
        self.hosaena = f"{hosaena_month} {hosaena_date}"
        return self.hosaena

    def find_seklet(self) -> str:
        "A function for calculating the date of Sklet(Crufication) in Ethiopian Calendar."
        month, date = [_ for _ in self.hosaena.split()]
        date = int(date)
        sklet_date = date + 5
        if sklet_date > 30:
            sklet_date %= 30
        self.sklet = f"{month} {sklet_date}"
        return self.sklet

    def find_tnsae(self) -> str:
        "A function for calculating the date of Tnsae(The end of Great lent) in Ethiopian Calendar."
        month, date = [_ for _ in self.hosaena.split()]
        tnsae_month = month
        date = int(date)
        tnsae_date = date + 7
        if tnsae_date > 30 :
            tnsae_date %= 30
            if month == "መጋቢት":
                tnsae_month="ሚያዚያ"
        self.tnsae = f"{tnsae_month} {tnsae_date}"
        return self.tnsae
    def find_rkbe_kahnat(self) -> str:
        "A function for calculating the date of rkbe kahnat(The meeting of Priests) in Ethiopian Calendar."
        month, date = [_ for _ in self.tnsae.split()]
        date = int(date)
        rkbe_kahnat_date = date + 24
        if (
            (month == "መጋቢት"
            and (54 >=rkbe_kahnat_date >= 50))
            or (month == "ሚያዚያ" and 30 >=rkbe_kahnat_date >= 25)
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
        if (month == "ሚያዚያ" and 45 >= erget_date >= 35) or (
            month == "ግንቦት" and 15 >= erget_date >= 1
        ):
            erget_month = "ግንቦት"
        else:
            erget_month = "ሰኔ"
        erget_date %= 30
        self.erget = f"{erget_month} {erget_date}"
        return self.erget
    def find_beale_hamsa(self):
        "A function for calculating the date of Beale hamsa in Ethiopian Calendar."
        month,date = [_ for _ in self.erget.split()]
        date = int(date)
        beale_hamsa_date = date + 10
        if month == "ግንቦት" and 20 >= beale_hamsa_date >= 5:
            beale_hamsa_month = "ግንቦት"
        else:
            beale_hamsa_month = "ሰኔ"
        beale_hamsa_date %= 30
        self.beale_hamsa = f"{beale_hamsa_month} {beale_hamsa_date}"
        return self.beale_hamsa
    def find_tsome_hawaryat(self):
        "A function for finding the date of Tsome Hawaryat (Lent of The Apostels) in Ethiopian Calendar"
        month, date = [i for i in self.beale_hamsa.split()]
        date = int(date)
        tsome_hawaryet_date = date + 1
        if tsome_hawaryet_date > 30 and month == "ግንቦት":
            tsomeHawaryatWer = "ሰኔ"
        else:
            tsomeHawaryatWer = month
        tsome_hawaryet_date %= 30
        self.tsome_hawaryat = f"{tsomeHawaryatWer} {tsome_hawaryet_date}"
        return self.tsome_hawaryat
    def find_tsome_dhnet(self):
        month, date = [i for i in self.tsome_hawaryat.split()]
        date = int(date)
        tsome_dhnet_date = date + 2
        if tsome_dhnet_date > 30 and month == "ግንቦት":
            tsome_dhnet_month = "ሰኔ"
        else:
            tsome_dhnet_month = month
        self.tsome_dhnet = f"{tsome_dhnet_month} {tsome_dhnet_date}"
        return self.tsome_dhnet

