# oscars-grind-sim
a look into results of oscars grind betting strategy during repeated coin flips.

### Oscar's Grind algorithm from [Oscar's Grind Wiki](https://en.wikipedia.org/wiki/Oscar%27s_grind):

```
unit := 1
betsize := unit
profit := 0

repeat
    bet
    if bet_won then
        profit := profit + betsize
        if profit < unit then
            if profit + betsize + unit > unit then
                betsize := unit − profit
            else
                betsize := betsize + unit
    else
        profit := profit − betsize
until profit = unit
```

### One example run, plotted with matplotlib:
<img width="646" height="555" alt="Screenshot 2026-07-07 at 5 33 40 PM" src="https://github.com/user-attachments/assets/82343ef0-c154-4df0-84f3-0d7eac1df400" />

