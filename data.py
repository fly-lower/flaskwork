import datetime
import calendar
class Getcalender(object):
    def __init__(self):
        date_now = datetime.datetime.now()
        month = date_now.month
        year = date_now.year
        ra = calendar.monthrange(year,month)
        self.wd = calendar.weekday(year,month,1)
        self.lstweek = []
        self.lstresult = []
        self.lstmonth = [day for day in range(1,ra[1])]
    def getlst(self):
        for i in range(7):
            if i<self.wd:
                self.lstweek.append('empty')
            else:
                self.lstweek.append(self.lstmonth.pop(0))
        self.lstresult.append(self.lstweek)

        while self.lstmonth:
            self.lstweek = []
            for i in range(7):
                if self.lstmonth:
                    self.lstweek.append(self.lstmonth.pop(0))
                else:
                    self.lstweek.append('empty')
            self.lstresult.append(self.lstweek)
        return self.lstresult

if __name__ == '__main__':
    g = Getcalender()
    print(g.getlst())