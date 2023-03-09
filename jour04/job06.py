langages = ["Python", "PHP", "Java", "C#"]

print("la première liste :", langages)

alter = langages[0]
langages[0] = langages[-1]
langages[-1] = alter

print("Et enfin :", langages)