# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# ⋀ конюнкция (and)

# ˅ дизьюнкция (or)

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:

            print ("x = ", {x}, ", y = ", {y}, ", z = ", {z})
            if not(x or y or z) == (not x and not y and not z):
                print ("истина")
            else:
                print("ложь")

