from datetime import datetime

date_format="%d-%m-%Y"
def get_date(prompt,allow_default=False):
    date_value=input(prompt)
    if allow_default and  not date_value:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date=datetime.strptime(date_value,date_format)
        return valid_date.strftime(date_value)
    except ValueError:
        print("Invalid date Formate. Please Try Again With 'dd-mm-yyyy'")
        return get_date(prompt,allow_default)
 
def get_amount():
        try:
             amount=float(input("Enter Amount If you wish to Enter: "))
             if amount<=0:
                  print("Amount cannot be minus value or zero value.")
             else:
                  return amount

        except ValueError as e:
             print(e)   
             return get_amount()       
    

def get_category():
     category=input("Enter Category('I' for Income and 'E' for Expences.) ")
     if category.lower()=="i":
          return "Income"
     elif category.lower()=="e":
          return "Expences"
     else:
          print("Invalid category.('I' for Income and 'E' for Expences.) ")
          return get_category()
    
    

def get_description():
    description=input("Enter description for Expences or Income(optional): ")
    return description
