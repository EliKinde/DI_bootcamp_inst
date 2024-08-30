#Exercise 5 : Amount Of Time Left Until January 1st


from datetime import datetime, timedelta

def time_until_new_year():
    # Get the current date and time
    now = datetime.now()

    # Define the target date for January 1st of the next year
    # If the current month is December, then the next year should be the next year
    if now.month == 12 and now.day > 31:
        target_year = now.year + 1
    else:
        target_year = now.year

    # Create a datetime object for January 1st of the target year
    target_date = datetime(target_year, 1, 1)

    # Calculate the difference between now and the target date
    time_difference = target_date - now

    # Get the total number of seconds in the difference
    total_seconds = time_difference.total_seconds()

    # Calculate days, hours, minutes, and seconds
    days = int(total_seconds // (24 * 3600))
    hours = int((total_seconds % (24 * 3600)) // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    # Print the result
    print(f"Time until January 1st: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

# Example usage
time_until_new_year()

