girls = [
    ("Evelyn", 17, 5.5, 80), ("Jessica", 16, 6.0, 85), ("Somto", 17, 5.4, 70), 
    ("Edith", 18, 5.9, 60), ("Liza", 18, 5.6, 76), ("Madonna", 17, 6.5, 66), 
    ("Waje", 20, 5.6, 87), ("Tola", 19, 6.0, 95), ("Aisha", 17, 5.7, 50), ("Latifa", 17, 5.5, 49)
]

boys = [
    ("Chinedu", 19, 5.7, 74), ("Liam", 16, 5.9, 87), ("Wale", 18, 5.8, 75), 
    ("Gbenga", 17, 6.1, 68), ("Abiola", 20, 5.9, 66), ("Kola", 19, 5.5, 78), 
    ("Kunle", 16, 6.1, 87), ("George", 18, 5.4, 98), ("Thomas", 17, 5.8, 54), ("Wesley", 19, 5.7, 60)
]

data = girls + boys

headers = ["Name", "Age", "Height", "Score"]

col_width = [max(len(str(row[i])) for row in data + [headers]) for i in range(len(headers))]
total_width = sum(col_width) + (3 * (len(headers) - 1))
print('-'*total_width)
print(" | ".join(str(headers[i]).ljust(col_width[i]) for i in range(len(headers))))
print('-'*total_width)

for row in data:
    print(" | ".join(str(row[i]).ljust(col_width[i]) for i in range(len(row))))
