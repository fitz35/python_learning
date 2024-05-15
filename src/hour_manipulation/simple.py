# The goal is to use only simple tool to interpret hour and say if it is breackfast (7-10h), launch (11h30 - 14h) or diner (19-20h)
# NOTE : I will use type anotation for readibility
# NOTE : this version has a major issue, the string isn't checked, so if the user nter a string with a bad fpormating it will crash. and it is not 
# easy to check this. The regular expression (regex) solve this problem

# the main !
def main():
    input_str = input("Enter the hour (format HH:MM or HH:MM a.m. or HH:MM p.m.): ").strip()

    # try to see if the input is in the format HH:MM or HH:MM a.m. or HH:MM p.m.

    input_strs = input_str.split(" ")
    hour, minute = extract_hour_and_minute(input_strs[0])
    if len(input_strs) == 2:
        if input_strs[1] == "a.m.":
            pass
        elif input_strs[1] == "p.m.":
            hour = convert_pm_to_24h(hour)
        else:
            print("Invalid format")
            return
    
    fract = convert_24h_to_fraction(hour, minute)
    print(fract)
    if 7 <= fract <= 10:
        print("breackfast")
    elif 11.5 <= fract <= 14:
        print("launch")
    elif 19 <= fract <= 21:
        print("diner")
    else:
        print("not the time to eat")


# convert the input string to a 24h format if it is in 12h format pm (am doesn't need to be converted)
def convert_pm_to_24h(hour: int) -> int:
    if hour == 12:
        return 0
    else:
        return hour + 12

# Extract the hour and minute from an input string formated like this HH:MM
# return a tuple of int (tuple is a fixed sized (here 2 element) list that can't be modified) corresponding to the hour and minute
def extract_hour_and_minute(input_str: str) -> tuple[int, int]:
    hour, minute = input_str.split(":")

    return int(hour), int(minute)

# Convert a 24h hour to an hour and a fraction of hour
def convert_24h_to_fraction(hour: int, minute: int) -> float:
    return hour + (minute * 100 / 60) / 100


# the following line (the if) is only a security relatively to the "import" keyword
if __name__ == "__main__":
    # The call to a main function is a good practice to keep the code clean, and can be call inside an other file
    main()