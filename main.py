import cash_flow as cf

input_message = 'Select an option: \n [1]Accounting an Entry - [2]Exit: '
option= 0

book_name = input("What's the name of your Cash Book?: ")
cash_book = cf.CashBook(book_name)
option = int(input(input_message))

while option != 2 :
    
    date  = input("What's the date wich this entry occur? :")
    description = input("What's the description of this entry? :")
    is_debit = input('Is it a credit [C] or debit [D]? :')
    value = input("What's value?:")
    is_debit = is_debit.upper()

    if is_debit =="D":
        is_debit = True
    else: 
        is_debit = False

    accounting_entry = cf.AccountingEntry(date,description, is_debit, value, cash_book)     
    option = int(input(input_message))
    

print(cash_book)