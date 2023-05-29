class CashBook:
    def __init__(self, name:str) -> None:
        self.name = name
        self.balance=0
        self.debits = {}
        self.credits = {}
    
    def __repr__(self):
        header = f"{70*'#'} {self.name.upper()} CASH BOOK {70*'#'}\n"
        debits_description =f"\n{35*'#'} DEBITS: \n"
        credits_description = f"\n{35*'#'} CREDITS: \n"
        balance_descritption = f"\n{35*'#'} BALANCE: {self.balance} \n"
        for i in self.debits:
            debits_description += f'Cod: {i}, Date {self.debits[i][0]}, Description: {self.debits[i][1]}, Value: ${self.debits[i][2]}\n'
       
        for i in self.credits:
            credits_description += f'Cod: {i}, Date {self.credits[i][0]}, Description: {self.credits[i][1]}, Value: ${self.credits[i][2]}\n'


        return header + debits_description +credits_description +balance_descritption
    
class AccountingEntry:
    cod = 0
    def __init__(self,date,description, is_debit:bool, value,cash_book: CashBook) -> None:
        self.date = date
        self.description=description
        self.is_debit = is_debit
        self.value = float(value)
        AccountingEntry.cod +=1
        self.cash_book = cash_book

    def set_entry(self) -> None:
        if self.is_debit:
            self.cash_book.balance += self.value
            self.cash_book.debits[self.cod] = [self.date, self.description, self.value]
        else:
            self.cash_book.balance -= self.value
            self.cash_book.credits[self.cod] = [self.date, self.description, self.value]
