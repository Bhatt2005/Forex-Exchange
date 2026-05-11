#Forex Exchange Using API:
import requests
def get_exchange_rate(base_currency,target_currency):

    url=f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
    #send GET Request
        response=requests.get(url)
        data=response.json()
        rate=data['rates'][target_currency]
        return rate
    except KeyError:
        print("Invalid currency code entered.")
        return None
    except Exception as e:
        print("An error occured:",e)
        return None
        
#Main Currency Converter Program

#User inputs

base_currency=input("Enter the base currency ").upper()
target_currency=input("Enter the target currency ").upper()

#Amount

amount=float(input("Enter the amount: "))

#Fetch exchange rate

rate= get_exchange_rate(base_currency,target_currency)

#Perform Conversion

if rate:
    converted_amount=amount*rate
    print("\nConversion Result")
    print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
