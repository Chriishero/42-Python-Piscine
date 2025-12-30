
def ft_count_harvest_recursive(days=None, i=None):
    if days is None:
        days = int(input("Days until harvest: "))
        i = 1
    if i <= days:
        print(f"Day {i}")
        ft_count_harvest_recursive(days, i + 1)
    else:
        print("Harvest time!")
