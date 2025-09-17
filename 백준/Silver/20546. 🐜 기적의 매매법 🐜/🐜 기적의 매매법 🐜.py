cash = int(input())
stock_prices = list(map(int, input().split()))

def jun_plan(cash_amount, stock_prices):
    cash = cash_amount
    stock_count = 0
    for stock_price in stock_prices:
        if cash >= stock_price:
            stock_count = stock_count + (cash // stock_price)
            cash = cash % stock_price

    return stock_count * stock_prices[-1] + cash
    
def sung_plan(cash_amount, stock_prices):
    cash = cash_amount
    stock_count = 0
    up_days = 0
    down_days = 0
    standard_price = 0
    for i, stock_price in enumerate(stock_prices):
        if i == 0:
            standard_price = stock_price
            continue
        else:
            if standard_price < stock_price:
                up_days += 1
                down_days = 0
            elif standard_price > stock_price:
                down_days += 1
                up_days = 0
            else:
                up_days = 0
                down_days = 0
                
            standard_price = stock_price
            
            if down_days >= 3:
                stock_count = (cash // standard_price) + stock_count
                cash = cash % standard_price
            elif up_days >= 3 and stock_count >= 1:
                cash = cash + (standard_price * stock_count)
                stock_count = 0
        
    return stock_count * stock_prices[-1] + cash
                
jun_amount = jun_plan(cash, stock_prices)
sung_amount = sung_plan(cash, stock_prices)

if jun_amount > sung_amount:
    print("BNP")
elif sung_amount > jun_amount:
    print("TIMING")
elif sung_amount == jun_amount:
    print("SAMESAME")