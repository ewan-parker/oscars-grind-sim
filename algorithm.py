import random

def oscar_session():
    unit = 1
    betsize = unit
    profit = 0
    profit_history = []

    while profit != unit:
        profit_history.append(profit)

        if coinflip():
            profit += betsize
            if profit < unit:
                if profit + betsize + unit > unit: # if you will overshoot
                    betsize = unit - profit # then make the betsize aim to set profit to 1 unit
                else:
                    betsize += unit #not overshooting, double your bet
        else:
            profit -= betsize # standard loss

    profit_history.append(profit) # capture final val of profit
    return profit_history


def coinflip():
    return random.randint(0, 1) == 0