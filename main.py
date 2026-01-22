# 1
lst = [1, 2, 3]
match lst:
    case []:
        print("Empty list")
    case [a]:
        print("One element")
    case [a, b]:
        print("Two elements")
    case _:
        print("Three or more elements")


# 2
credentials = ("admin", "1234")
match credentials:
    case ("admin", "1234"):
        print("Login successful")
    case _:
        print("Login failed")


# 3
status = 404
match status:
    case 200: print("OK")
    case 201: print("Created")
    case 400: print("Bad Request")
    case 401: print("Unauthorized")
    case 403: print("Forbidden")
    case 404: print("Not Found")
    case 500: print("Server Error")
    case _: print("Unknown status")


# 4
text = "abc123"
match text:
    case _ if text.isdigit():
        print("Only digits")
    case _ if text.isalpha():
        print("Only letters")
    case _:
        print("Mixed")


# 5
month = "April"
match month.lower():
    case "december" | "january" | "february":
        print("Winter")
    case "march" | "april" | "may":
        print("Spring")
    case "june" | "july" | "august":
        print("Summer")
    case "september" | "october" | "november":
        print("Autumn")
    case _:
        print("Invalid month")

