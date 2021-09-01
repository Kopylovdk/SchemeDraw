def p_draw(main_list, p=1, x=0, y=0):
    # Рисуем полюса в зависимости от их количества
    uzo_up = []
    uzo_down = []
    if p == 1:
        main_list.line(xy=((10 + x, 30 + y), (10 + x, y), (5 + x, -10 + y)), fill='black')
        main_list.line(xy=((10 + x, -10 + y), (10 + x, -20 + y)), fill='black')
        uzo_up.append((10 + x, -20 + y))
        uzo_down.append((10 + x, 30 + y))
    else:
        step = 0
        for i in range(p):
            main_list.line(xy=((7 + x + step, 30 + y), (7 + x + step, y), (2 + x + step, -10 + y)), fill='black')
            main_list.line(xy=((7 + x + step, -10 + y), (7 + x + step, -20 + y)), fill='black')
            uzo_up.append((7 + x + step, -20 + y))
            uzo_down.append((7 + x + step, 30 + y))
            step += 11
    return uzo_up, uzo_down


def uzo(main_list, x=0, y=0, p=1, v=220):
    # По умолчанию полюсов 1, 220в
    el_x_2 = 0
    el_y_2 = 0
    if p == 1:
        el_x_2 = 20 + x
        el_y_2 = 15 + y
        main_list.line(xy=((8 + x, 25 + y), (12 + x, 22 + y)), fill='black')
        main_list.line(xy=((8 + x, 23 + y), (12 + x, 20 + y)), fill='black')
        if v == 380:
            main_list.line(xy=((8 + x, 27 + y), (12 + x, 24 + y)), fill='black')
            main_list.line(xy=((8 + x, 21 + y), (12 + x, 18 + y)), fill='black')
    elif p == 2:
        el_x_2 = 25 + x
        el_y_2 = 15 + y
        # Пунктир от левой полосы до 2-го полюса
        main_list.line(xy=((12 + x, -5 + y), (16 + x, -5 + y)), fill='black')
    elif p == 4:
        el_x_2 = 48 + x
        el_y_2 = 15 + y
        main_list.line(xy=((12 + x, -5 + y), (16 + x, -5 + y)), fill='black')
        main_list.line(xy=((19 + x, -5 + y), (23 + x, -5 + y)), fill='black')
        main_list.line(xy=((26 + x, -5 + y), (30 + x, -5 + y)), fill='black')
        main_list.line(xy=((33 + x, -5 + y), (37 + x, -5 + y)), fill='black')
    # Эллипс
    main_list.ellipse(xy=(x, 5 + y, el_x_2, el_y_2), outline=(0, 0, 0), )
    # Левая полоса
    main_list.line(xy=((x, 10 + y), (-5 + x, 10 + y), (-5 + x, -5 + y), (8 + x, -5 + y)), fill='black')

    uzo_up, uzo_down = p_draw(main_list, x=x, y=y, p=p)
    return uzo_up, uzo_down


def av(main_list, x=0, y=0, p=1):
    # p - Количество полюсов, default=1
    main_list.line(xy=((x, 30 + y), (x, 20 + y), (-8 + x, 5 + y)), fill='black')
    main_list.line(xy=((x, 5 + y), (x, -10 + y)), fill='black')
    # Крест
    main_list.line(xy=((-2 + x, 7 + y), (2 + x, 3 + y)), fill='black')
    main_list.line(xy=((-2 + x, 3 + y), (2 + x, 7 + y)), fill='black')
    # Прямоугольник
    main_list.line(xy=((-3 + x, 16 + y), (-6 + x, 19 + y), (-10 + x, 10 + y), (-7 + x, 7 + y)), fill='black')
    # Наклонные линии
    step = 0
    for i in range(p):
        main_list.line(xy=((-2 + x, -6 + y + step), (2 + x, -9 + y + step)), fill='black')
        step += 2
    av_up = (x, -10 + y)
    av_down = (x, 30 + y)
    return av_up, av_down
