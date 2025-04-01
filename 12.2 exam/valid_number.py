phone_number = input().strip()
number_parts = phone_number.split("-")
number_str = "".join(number_parts)

if not number_str.isdigit():
    print("NO")
    quit()

if len(number_parts) == 3:
    if len(number_parts[0]) == 3 and len(number_parts[1]) == 3 and len(number_parts[2]) == 4:
        print("YES")
    else:
        print("NO")
elif len(number_parts) == 4 and number_parts[0] == "7":
    if len(number_parts[1]) == 3 and len(number_parts[2]) == 3 and len(number_parts[3]) == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
