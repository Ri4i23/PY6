# Пам-парам

poem = input("Введите фразу ").lower()
vowels= ('а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я')
if poem.isdigit():
    print("Введите стихотворение ")
list2 = poem.split()
new_list = []

for words in list2:
    a = 0
    for letter in words:
        if letter in vowels:
            a = a + 1
    new_list.append(a)
if len(set(new_list)) == 1:
    print('True ')
else:
    print('False ')