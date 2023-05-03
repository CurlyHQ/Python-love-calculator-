from datetime import datetime, timedelta

def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

def calculate_days_passed(date1, date2):
    return abs((date2 - date1).days)

def calculate_love_percentage(total_days, love_days):
    return (love_days / total_days) * 100

if __name__ == "__main__":
    birthday = get_date_input("Enter your birthday (YYYY-MM-DD): ")
    met_date = get_date_input("Enter the day you two met (YYYY-MM-DD): ")

    current_date = datetime.now()
    total_days = calculate_days_passed(birthday, current_date)
    love_days = calculate_days_passed(met_date, current_date)

    love_percentage = calculate_love_percentage(total_days, love_days)

    print(f"\nDays since your birthday: {total_days}")
    print(f"Days since you met: {love_days}")
    print(f"This person has loved you for {love_days} days, which is {love_percentage:.2f}% of your life.")
