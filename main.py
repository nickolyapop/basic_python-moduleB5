def func_proverka(g):   #функция проверки на выигрыш
    if (arr[1][1] == g and ((arr[0][0] == g and arr[2][2] == g) or (arr[0][2] == g and arr[2][0]==g) or (
            arr[0][1] == g and arr[2][1] == g) or (arr[1][0] == g and arr[1][2] == g))) or (
            arr[0][0] == g and (
            (arr[1][0] == g and arr[2][0] == g) or (arr[0][1] == g and arr[0][2] == g))) or (
            arr[2][2] == g and ((arr[0][2] == g and arr[1][2] == g) or (arr[2][0] == g and arr[2][1] == g))):
        return True
#====================================
#фунция для ввода координат игроком
def gamer_input(gamer):
    while True:
        x_y =  input(f"введите номер поля, через пробел в виде y_x, для игрока {gamer}:")
        if not (x_y[0].isdigit() and x_y[2].isdigit()):
            print("ошибка, повторите ввод, введите числа")
            continue
        x = int(x_y[0])
        y = int(x_y[2])
        if x < 0 or x > 2 or y < 0 or y > 2: #проверка допустимого диапазона
            print("Ошибка, координаты вне  допустимой области")
            continue
        if arr[x][y] == ' ':
            arr[x][y] = flag
            break
        else:
            print("Это поле уже заполнено, повторите ввод координаты для пустой клетки")
            continue
#===========================================================
def print_field():
    print("  0 1 2")
    print("________")
    for yl in range(3):
        print(f"{yl}", end="|")
        for xl in range(3):
            print(f"{arr[yl][xl]}", end="|")
        print()

arr=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #пустое поле 3х3
flag = 'x' #ход X или O
i = 1   #счетчик хода
print(" Первый ход делает игрок, ставящий крестики.")
print_field()
while i < 10:    # играем до тех пор пока не заполнятся все 9 полей
    flag = 'o' if i % 2 == 0 else 'x'   #определяем чей ход, по шагу (игрок x или о)

    gamer_input(flag) #ввод координат
    print_field() #---строим поле
     # проверка после 5 ходов, нет ли поебедителя (заполнение ряда)
    if i > 4:
        if func_proverka(flag) is True:
            print(f"Победа игрока {flag}")
            break
    if i == 9:
        print("Ничья!!!")
    i += 1





