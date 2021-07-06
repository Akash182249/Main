import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

akashsApplication = RailwayForm()
akashsApplication.name = "Veda"
akashsApplication.train = "Rajdhani Express"
akashsApplication.printData()