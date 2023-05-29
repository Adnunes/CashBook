import cash_flow


cash_book_1 = CashBook('Empresa Abc')

lancamento_1 = AccountingEntry('29/05/2023', 'primeiro lancamento',True,124, cash_book_1)
lancamento_1.set_entry()

lancamento_2 = AccountingEntry('29/05/2023', 'segundo lancamento',True,134, cash_book_1)
lancamento_2.set_entry()

lancamento_3 = AccountingEntry('29/05/2023', 'terceiro lancamento',False,8, cash_book_1)
lancamento_3.set_entry()

lancamento_4 = AccountingEntry('29/05/2023', 'quarto lancamento',False,10, cash_book_1)
lancamento_4.set_entry()



print(cash_book_1)