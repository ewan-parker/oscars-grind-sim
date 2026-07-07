from algorithm import oscar_session
import matplotlib.pyplot as plt

profit_history = oscar_session()

plt.plot(profit_history)
plt.xlabel('Bet number')
plt.ylabel('Profit')
plt.title("Oscar's Grind Session")
plt.show()