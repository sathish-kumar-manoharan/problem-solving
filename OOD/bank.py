class Account:
    def __init__(self, timeStamp, accountId):
        self.timeStamp = timeStamp
        self.accountId = accountId
        self.balance = 0
        self.transactionValue = 0

def create_account(timeStamp, accountId, accounts):
    if not timeStamp or not accountId:
        return ""
    
    if accountId not in accounts:
        accounts[accountId] = Account(timeStamp, accountId)
        return "true"
    
    return "false"

def deposit(timeStamp, accountId, accounts, amount):
    if not timeStamp or not accountId:
        return ""
    
    if accountId not in accounts:
        return ""
    
    amount = int(amount)
    accounts[accountId].balance += amount
    accounts[accountId].transactionValue += amount

    return str(accounts[accountId].balance)

def withdraw(timeStamp, accountId, accounts, amount):
    if not timeStamp or not accountId:
        return ""
    
    if accountId not in accounts:
        return ""
    
    amount = int(amount)

    if accounts[accountId].balance >= amount:
        accounts[accountId].balance -= amount
        accounts[accountId].transactionValue += amount
        return str(accounts[accountId].balance)

    return ""

def account_compator(account):
    return (account.transactionValue, account.accountId)

def top_activity(number, accounts):

    number = int(number)

    if number > 0:
        sorted_list = sorted(accounts.values(), key=account_compator, reverse=True)[:number]
        temp_list = [x.accountId + "(" +str(x.transactionValue) + ")" for x in sorted_list]
        return temp_list


def solution(queries):
    result = []
    accounts = {}

    for query in queries:
        operation = query[0] if len(query) >= 1 else ""
        timeStamp = query[1] if len(query) >= 2 else ""
        accountId = query[2] if len(query) >= 3 else ""
        number = query[2] if len(query) >= 3 else ""
        amount = query[3] if len(query) >= 4 else ""

        if operation == "CREATE_ACCOUNT":
            result.append(create_account(timeStamp, accountId, accounts))
        elif operation == "DEPOSIT":
            result.append(deposit(timeStamp, accountId, accounts, amount))
        elif operation == "PAY":
            result.append(withdraw(timeStamp, accountId, accounts, amount))
        elif operation == "TOP_ACTIVTY":
            result.append(top_activity(number, accounts))

    return result

print(solution([ 
    ["CREATE_ACCOUNT", "1", "account1"], 
    ["CREATE_ACCOUNT", "2", "account2"],
    ["DEPOSIT", "3", "account1", "500"], 
    ["DEPOSIT", "4", "account1", "500"], 
    ["DEPOSIT", "5", "account2", "1000"], 
    ["PAY", "6", "account1", "500"],
    ["CREATE_ACCOUNT", "7", "account3"],
    ["DEPOSIT", "8", "account3", "2000"],
    ["TOP_ACTIVTY", "9", "2"]
]))
