import time

name = input("Hey! What's ypur name ? ")
print(f"Hello {name}! Nice to meet you.")
age = int(input("How old are you ? "))
time.sleep(3)
if age >= 55: print("You 're a boomer")
else: print("You 're not a boomer")