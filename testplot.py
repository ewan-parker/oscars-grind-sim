import matplotlib.pyplot as plt

plt.plot(range(len(bankroll_history)), bankroll_history)
plt.xlabel('Bet number')
plt.ylabel('Bankroll')
plt.title('Oscar\'s Grind Simulation')
plt.show()