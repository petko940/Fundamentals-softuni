quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
pig_weight = float(input()) * 1000

for day in range(1, 31):
    quantity_food -= 300
    if day % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if day % 3 == 0:
        quantity_cover -= pig_weight / 3
    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, "
          f"Hay: {quantity_hay / 1000:.2f}, "
          f"Cover: {quantity_cover / 1000:.2f}.")

