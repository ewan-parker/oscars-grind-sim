# oscars-grind-sim
a look into results of oscars grind betting strategy during repeated coin flips.

### Oscar's Grind algorithm from [Oscar's Grind Wiki](https://en.wikipedia.org/wiki/Oscar%27s_grind)

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
