import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLUMNS = 3
SYMBOLS = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5,
    'E': 6
}
SYMBOL_VALUE ={
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'E': 0
}

def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        #amount = str(100)
        if amount.isdigit():
            amount = int(amount)
            if(amount>0):
                break
            else:
                print('amount must be greater than 0')
        else:
            print('Enter valid amount')
            
    return amount

def get_number_of_lines():
    while True:
        lines = input('Choose the number of lines between (1 - ' + str(MAX_LINES) + ' )? ' )
        #lines = str(2)
        if(lines.isdigit):
            if(1<=int(lines)<=MAX_LINES):
                lines = int(lines)
                break
            else:
                print('Enter valid number')
        else:
            print('Enter valid number')
            
    return lines

def get_bet():
    while True:
        bet = input('Enter your bet amount $')
        #bet = str(10)
        if(bet.isdigit):
            if(MIN_BET<= int(bet) <= MAX_BET):
                bet = int(bet)
                break
            else:
                print(f'Enter bet amount between {MIN_BET} to {MAX_BET}')
        else:
            print('Enter valid bet amount')
            
    return bet
                
def get_slots(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    cols = []
    for _ in range(COLUMNS):
        all_symbols_copy = all_symbols[:]        
        col = []
        for _ in range(ROWS):
            slot = random.choice(all_symbols_copy)
            col.append(slot)
            all_symbols_copy.remove(slot)
        cols.append(col)
        #cols = [['C','D','D'],['A','D','C'],['B','D','E']]
    return cols   


def print_slot(cols):
    for row in range(len(cols[0])):
        for i, col in enumerate(cols):
            print(col[row], end=' | ')
        print()

def check_winnings(cols):
    total_winnings = 0
    winning_values = []
    
    for row in range(len(cols[0])):
        for i, col in enumerate(cols):
            if(i==0):
                slot_value = col[row]
                #print('slot_value - '+slot_value)
            else:
                #print('col[row] - '+col[row])
                if(slot_value!=col[row]):
                    break
                else:
                    #print('len(col) - '+str(len(col)))
                    #print('col[row] - '+col[row])
                    if(i==len(col)-1):
                        total_winnings = total_winnings+1
                        winning_values.append(col[row])
                        
    #print('total_winnings is '+str(total_winnings))
    #print('winning_values is '+str(winning_values))
    winnings = {
        'total_wins': total_winnings,
        'winning_vals': winning_values
    }
    #print(winnings)
    return winnings
    
def announce_result(winning_result, bet):
    print(winning_result)
    total_win_amount = 0
    total_wins = int(winning_result.get('total_wins'))
    winning_symbols = str(winning_result.get('winning_vals'))
    for _ in range(total_wins):
        for win_val in winning_result.get('winning_vals'):
            win_symbol_value = int(SYMBOL_VALUE.get(win_val))
            total_win_amount = total_win_amount + (win_symbol_value*bet)
    print(f'You have won on {total_wins} lines {winning_symbols} and your tatal win amount is {total_win_amount}')
    return total_win_amount
    
def calaulate_balance(balance, total_win_amount):
    final_balance = balance + (total_win_amount)
    print(f'Your total balance is {final_balance}')
    return final_balance
                    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if(total_bet<=balance):
            print(f'You have bet of ${bet} for {lines} lines and your total bet amount is ${total_bet}')
            break
        else:
            print(f'Your total bet is {total_bet} which is more than your balance {balance}. Please enter lower bet amount')
            
    cols = get_slots(ROWS, COLUMNS, SYMBOLS)
    print_slot(cols)
    winning_result = check_winnings(cols)
    if(winning_result.get('total_wins')!=0):
        total_win_amount = announce_result(winning_result, bet)
        balance = calaulate_balance(balance, total_win_amount)
    else:
        print(f'Oops!! Bad luck:( Please try again')
        balance = balance - 5
        print(f'Your new balance is {balance}')
    
main()