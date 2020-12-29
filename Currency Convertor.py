class Conversion(object):
    symbol_list = [] #a list of every currency we have added as an object
    name_list = [] #list of names
    def __init__(self,name,symbol,conversion_factor):
        self.conversion_factor = conversion_factor  #assume conversion factor as 1 X = C.F Rupees
        self.name = name
        self.symbol = symbol
        Conversion.symbol_list.append(symbol) #inserts the symbol into the list
        Conversion.name_list.append(name) #inserts name into the list
    def conv_to_inr(self,amount):
        rupees = amount * self.conversion_factor    #to convert X USD to INR
        return rupees
    def inr_to_currency(self,amount_of_rupees):
        final_val = amount_of_rupees/self.conversion_factor  #to convert Y INR to Pounds
        return final_val

def convert(currency1,amount,currency2):
    intermediate_value = currency1.conv_to_inr(amount)
    final = currency2.inr_to_currency(intermediate_value)
    return round(final,2)
USD = Conversion("US Dollar","USD",73.66)
INR = Conversion("Indian Rupee","INR",1.00)
CHF = Conversion("Swiss Franc","CHF",81.96)
GBP = Conversion("Pound Sterling","GBP",98.57)
EUR = Conversion("Euro","EUR",90.49)
JPY = Conversion("Japanese Yen","JPY",0.71)
CNY = Conversion("Chinese Yuan Reniminbi","CNY",11.26)
CAD = Conversion("Canadian Dollar","CAD",57.22)
AUD = Conversion("Australian Dollar","AUD",55.98)
TRY = Conversion("Turkish Lira","TRY",9.75)
NZD = Conversion("New Zealand Dollar","NZD",52.47)
SGD = Conversion("Singapore Dollar","SGD",55.44)
HKD = Conversion("Hong Kong Dollar","HKD",9.5)
KWD = Conversion("Kuwaiti Dinar","KWD",241.46)
BRL = Conversion("Brazilian Real","BRL",14.12)
MYR = Conversion("Malaysian Ringgit","MYR",18.14)
PKR = Conversion("Pakistani Rupee","PKR",0.46)
BDT = Conversion("Bangladeshi Taka","BDT",0.87)
AFN = Conversion("Afghan Afghani","AFN",0.95)
NPR = Conversion("Nepalese Rupee","NPR",0.63)

while True:
    print("Available Currencies:")
    for i in range(len(Conversion.symbol_list)):
        print(Conversion.name_list[i]+": "+Conversion.symbol_list[i])
    while True:
        inputCurrency = input("Enter the symbol of the currency you wish to convert (input): ").upper()
        if inputCurrency not in Conversion.symbol_list:
            print("Invalid input. Please try again.")
        else:
            break
    while True:
        amount = input("Enter the amount you wish to convert: ")
        if amount.isdigit():
            break
        else:
            print("Please enter an integer value only.")
    while True:
        outputCurrency = input("Enter the symbol of the currency you wish to convert to (output): ").upper()
        if outputCurrency not in Conversion.symbol_list:
            print("Invalid currency. Please try again.")
        else:
            break
    converted_value = convert(eval(inputCurrency),eval(amount),eval(outputCurrency))
    print(str(amount)+" "+inputCurrency+" is equal to "+str(converted_value)+" "+outputCurrency)
    flag = 0
    while flag==0:
        again = input("Would you like to convert another value? (enter y/n only)")
        if again.upper() == "Y":
            flag = 1
        elif again.upper() == "N":
            break
        else:
            print("Please enter a valid response")
    if flag == 1:
        continue
    elif flag == 0:
        break
