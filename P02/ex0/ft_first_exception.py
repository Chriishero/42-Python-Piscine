
def check_temperature(temp_str):
    """
    Check is the parameter 'temp_str' is a valid temperature for plants.

    :param temp_str: temperature of type string
    """
    temp_nbr = None
    print(f"Testing temperature: {temp_str}")
    try:
        temp_nbr = int(temp_str)
    except (ValueError, TypeError):
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if temp_nbr > 40:
        print(f"Error: {temp_nbr}°C is too hot for plants (max 40°C)\n")
        return
    elif temp_nbr < 0:
        print(f"Error: {temp_nbr}°C is too cold for plants (min 0°C)\n")
        return
    print(f"Temperature {temp_nbr}°C is perfect for plants!\n")
    return (temp_nbr)


# if __name__ == "__main__":
#     print("=== Garden Temperature Checker ===\n")
#     check_temperature("abc")
#     check_temperature("12")
#     check_temperature("100")
#     check_temperature("-11")
#     print("All tests completed - program didn't crash!")
