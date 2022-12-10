

def name_file(lst):
    max_len = 0
    # Находим максимальную длину названия.
    # В задании сказано: "Важно, в название файла не должны дублироваться символы"
    # но не сказано, что делать, если они дублируются, то что делать???
    # Затем нужно дополнить имя файла нижним подчекиванием, до максимальной длины,
    # не будет ли это дублированием символом если нужно добавить больше 2?

    for i in lst:
        if len(i) > max_len:
            max_len = len(i)

    lst = [i if len(i) == max_len else i + ("_" * (max_len-len(i))) for i in lst]
    print(lst)
