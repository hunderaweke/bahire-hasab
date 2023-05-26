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

    def find_beale_metk(self):
        """A Function For Findein"""
        metk = self.metk
        metk = metk -30 if metk>30
        if metk >= 15 and metk <= 30:
            self.beale_metk = f"መስክረም {metk}"
        elif metk >= 2 and metk <= 14:
            self.beale_metk = f"ጥቅምት{metk}"
        return self.beale_metk
    def find_day_name(self,month_date_string:str):
        """A function for finding the name of the day of a given date in mm/dd format"""
        days = {1: "እሁድ", 2: "ሰኞ", 3: "ማክሰኞ", 4: "ረቡዕ", 5: "ሐሙስ", 6: "አርብ", 0: "ቅዳሜ"}
        month,date = [_ for _ in month_date_string.split()]
        date  = int(date)
        tnte_yon=(((self.amete_alem//4)+(self.amete_alem))%7)-1
        months  = self.months
        doubled_month = 2*(months[month])
        sum_akt = doubled_month+date+tnte_yon
        sum_akt %=7
        self.day = days[sum_akt]
        return self.day
    def find_mebaja_hamer(self):
        beale_metk = self.beale_metk
        TEWSAK = {"ቅዳሜ": 8, "እሁድ": 7, "ሰኞ": 6, "ማግሰኞ": 5, "ረቡዕ": 4, "ሐሙስ": 3, "አርብ": 2}
        day =Calendar.find_day_name(self,beale_metk) 
        metk = self.metk
        tewsak = TEWSAK[day]
        self.mebaja_hamer = tewsak+metk if tewsak+metk<30 else tewsak
        return self.mebaja_hamer
