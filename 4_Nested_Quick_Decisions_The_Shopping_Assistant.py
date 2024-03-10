#Task 1

weather = input("Enter the weather: sunny, rainy, or cold: ")

clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)


#Task 2

weather = input("Enter the weather: sunny, rainy, or cold: ")

clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)
additional_items = "hat" if weather == "sunny" else "boots"
print(additional_items)


#Task 3

weather = input("Enter the weather: sunny, rainy, or cold: ")

clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)
accessory = "sunscreen" if clothing == "sunglasses" else "beenie" if weather == "rainy" else "jacket"
print(accessory)
