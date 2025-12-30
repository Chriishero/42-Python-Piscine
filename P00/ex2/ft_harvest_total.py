
def ft_harvest_total():
    days = []
    for i in range(3):
        days.append(int(input(f"Day {i + 1} harvest: ")))
    totals = 0
    [totals := totals + d for d in days]
    print("Total harvest:", totals)
