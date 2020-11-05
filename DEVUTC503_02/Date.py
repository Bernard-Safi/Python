class Date:
     def __init__(self,day,month,year):
         self.day=day
         self.month=month
         self.year=year
     def __repr__(self):
          return f"{self.day}/{self.month}/{self.year}"
#test
d1=Date(6,12,1991)
print(d1)