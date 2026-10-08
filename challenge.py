seconds = int(input("Enter seconds: "))

h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60

print(f"Hours: {h}")
print(f"Minutes: {m}")
print(f"Seconds: {s}")

print(f"{h:02}:{m:02}:{s:02}")