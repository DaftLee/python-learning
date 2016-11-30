import login,bank_system

if __name__ == '__main__':
    account=login.login()
    if account!=False:
        bank_system.bank_system(account)
