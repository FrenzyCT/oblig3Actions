import sys
sys.path.append(r"C:\Users\ct\PycharmProjects\oblig3_actions")

def calculate_if_leap_year(leapyear):
    if leapyear % 400 == 0:
        return True
    elif leapyear % 4 == 0:
        if leapyear % 100 != 0:
            return True
        #return True
    return False



if __name__ == "__main__":
    print("Type the year you want to check if it's a leap year: ")
    year = int(input())

    isLeapyear = calculate_if_leap_year(year)
    print(f"Is {year} a leap year?: {isLeapyear}")