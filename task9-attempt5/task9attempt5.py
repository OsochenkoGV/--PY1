salary = 5000
spend = 6000
months = 10
increase = 0.03
need_money = 0
for i in range(months):
    need_money += spend - salary
    spend *= 1 + increase
print(round(need_money))
