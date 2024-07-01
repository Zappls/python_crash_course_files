names = ["alex", "ambra", "andi", "thomas", "sophie"]
message = "Good Morning,"
print(message,names[0].title())
print(message,names[1].title())
print(message,names[2].title())
print(message,names[3].title())
print(message,names[4].title())

# using an f-string for a clean print call
message = f"Good Morning, {names[0].title()}"
print(message)
message = f"Good Morning, {names[1].title()}"
print(message)
message = f"Good Morning, {names[2].title()}"
print(message)
message = f"Good Morning, {names[3].title()}"
print(message)
message = f"Good Morning, {names[4].title()}"
print(message)
