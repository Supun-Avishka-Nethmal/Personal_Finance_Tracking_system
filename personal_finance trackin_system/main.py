import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date,get_amount,get_category,get_description

class csv_convert:
    csv_file="finance_data.csv"
    COLUMNS=["date","Amount","category","description"]
    format="%d-%m-%Y"

    @classmethod
    def initialise_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
            
        except FileNotFoundError:
            df= pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.csv_file,index=False)

    @classmethod
    def add_new_finance(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "Amount":amount,
            "category":category,
            "description":description,
        }

        with open(cls.csv_file,"a",newline="") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("New Entry Insert Success.")

    @classmethod
    def all(cls):
           csv_convert.initialise_csv()
           daten=get_date("Enter the date for transcation(dd-mm-yyyy) or Press Enter to add Today's date ",allow_default=True)   
           amountn=get_amount()
           categoryn=get_category()
           descriptionn=get_description()  
           csv_convert.add_new_finance(daten,amountn,categoryn,descriptionn)

    
    @classmethod
    def get_transcations(cls,startdate,enddate):
            df=pd.read_csv(cls.csv_file)
            df["date"]=pd.to_datetime(df["date"],format=csv_convert.format)
            startdate=datetime.strptime(startdate,csv_convert.format)
            enddate=datetime.strptime(enddate,csv_convert.format)

            date_condition=(df["date"]>=startdate) & (df["date"]<=enddate)
            filterd_date=df.loc[date_condition]

            if filterd_date.empty:
                 print("No Transcation found in the given date.")
            else:
                 print(f"\nTransactions From {startdate.strftime(csv_convert.format)} To {enddate.strftime(csv_convert.format)}")
                 print()
                 print(filterd_date.to_string(index=False))

                 total_income=filterd_date[filterd_date["category"]=="Income"]["Amount"].sum()
                 total_expences=filterd_date[filterd_date["category"]=="Expences"]["Amount"].sum()
                 print("\nSummary:")
                 print()
                 print(f"Total Income: ${total_income:.2f}")
                 print(f"Total Expence: ${total_expences:.2f}")
                 if (total_income-total_expences)>0:
                  print(f"Net Savings: {(total_income-total_expences):.2f}")
                 else:
                      print("Net Savings: Your Expences more than Income")

            return filterd_date
    
    
    def main():
        while True:
            print("\n1.Add a New Transaction.")
            print("2.view a Transactions and summery within a date range")
            print("3.Exit.")
            choise=int(input("Enter Your Choise(1-3) ") )
            if choise==1:
                 all()
            elif choise==2:
                startdate=get_date("Enter the Start date (dd-mm-yyyy) or Press Enter to add Today's date " ) 
                enddate=  get_date("Enter the End date (dd-mm-yyyy) or Press Enter to add Today's date " )
                csv_convert.get_transcations(startdate,enddate)
            elif choise==3:
                 print("Exit..")
                 quit()    
            else:
                 print("Invalid Number")    

csv_convert.main() 
 