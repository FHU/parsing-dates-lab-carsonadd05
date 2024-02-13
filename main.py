#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    months = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    return months.get(month, "Invalid month")


#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    parts = user_string.split()
    month = parse_month(parts[0])
    day = parts[1][:-1] 
    if int(day) < 10:
        day = "0" + day 
    year = parts[2]
    return f"{month}/{day}/{year}"

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
 while True:
        user_input = input().strip()
        if user_input == "-1":
            break
        print(parse_date(user_input))