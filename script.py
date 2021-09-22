from PIL import Image, ImageDraw, ImageFont
from const import BACK_WIDTH, BACK_HEIGHT, RGB, RIGHT_TAB, UP_TAB, LEFT_TAB, DOWN_TAB, COMMENT_POSITION, FONT_PATH,\
    MODULE_NAME_STEP, pictures_prop_dict, COMMENT_WIDTH, COMMENT_HEIGHT
from pictures import uzo, av
from data_parcer import sql_data_parser
# For buffer use
# import io


def text_split(to_split):
    eggs = to_split.split(' ')
    result = ''
    for j, k in enumerate(eggs):
        if j % 2 == 0:
            result += k + '\n'
        else:
            result += k + ' '
    return result if len(result) > 1 else 'ERROR\nno data\nto split'


def new_list():
    back = Image.new('RGB', (BACK_WIDTH, BACK_HEIGHT), RGB)
    draw = ImageDraw.Draw(back)
    font = ImageFont.truetype(f'{FONT_PATH}dejavu-sans-condensed.ttf', size=9, encoding='UTF-8')
    return back, draw, font


def next_list(old_back, current_prop_dict):
    old_back.save(f'Scheme_{current_prop_dict.get("spec_id")}_list_{current_prop_dict.get("list_number")}.jpg',
                  quality=100)
    current_prop_dict.get('list_names').append(f'Scheme_{current_prop_dict.get("spec_id")}'
                                               f'_list_{current_prop_dict.get("list_number")}.jpg')
    # Save to buffer BytesIO()
    # current_prop_dict['buffers'][f'list{current_prop_dict.get("list_number")}'] = io.BytesIO()
    # old_back.save(current_prop_dict['buffers'][f'list{current_prop_dict.get("list_number")}'], format='JPEG')
    current_prop_dict['list_number'] += 1
    new_back, new_draw, font = new_list()

    new_list_step = 0
    for _ in range(3):
        new_draw.text((LEFT_TAB, current_prop_dict.get('Ввод').get('xy_down')[1] - 10 + new_list_step),
                      text=current_prop_dict.get('params')[_], font=font, fill='black')
        new_draw.line(((LEFT_TAB, current_prop_dict.get('Ввод').get('xy_down')[1] + new_list_step),
                       (BACK_WIDTH - RIGHT_TAB, current_prop_dict.get('Ввод').get('xy_down')[1] + new_list_step)),
                      fill='black')
        new_list_step += 20
    new_draw.line(((LEFT_TAB, current_prop_dict.get('bottom_line').get('y')),
                   (BACK_WIDTH - RIGHT_TAB, current_prop_dict.get('bottom_line').get('y'))), fill='black')
    current_prop_dict['first_line_step'] = 15
    return new_back, new_draw, current_prop_dict


def schema_save_to_jpg(spec_id):
    spec = sql_data_parser(spec_id)
    back, draw, font = new_list()

    prop_dict = {'spec_id': spec.get('header_id'),
                 'list_number': 1,
                 # 'buffers': {},  # For use with buffer BytesIO()
                 'list_names': [],
                 'first_line_step': 15}

    for group in spec.get('spec'):
        for line in group.get('data'):
            # Проверка вхождения блока в границы страницы
            if len(group.get('data')) == 1:
                if LEFT_TAB + prop_dict.get('first_line_step') + MODULE_NAME_STEP > BACK_WIDTH - RIGHT_TAB:
                    back, draw, prop_dict = next_list(back, prop_dict)
            elif len(group.get('data')) == 2:
                if LEFT_TAB + prop_dict.get('first_line_step') + MODULE_NAME_STEP * len(
                        group.get('data')[1].get('line_data')) > BACK_WIDTH - RIGHT_TAB:
                    back, draw, prop_dict = next_list(back, prop_dict)
            if line.get('line') == 1:
                to_draw = line.get('line_data')
                if to_draw.get('comment') in 'Ввод':
                    if '1п' in to_draw['module_name']:
                        p = 1
                        params = ('L', 'N', 'PE')
                    elif '2п' in to_draw['module_name']:
                        p = 2
                        params = ('L', 'N', 'PE')
                    elif '3п' in to_draw['module_name']:
                        p = 3
                        params = ('L1, L2, L3', 'N', 'PE')
                    elif '4п' in to_draw['module_name']:
                        p = 4
                        params = ('L1, L2, L3', 'N', 'PE')
                    else:
                        print('Значение полюса не обнаружено, либо не является 1п...4п')
                        break
                    av_up, av_down = av(draw, x=prop_dict.get('first_line_step') * 4 + LEFT_TAB, y=UP_TAB, p=p)
                    prop_dict['params'] = params
                    prop_dict['Ввод'] = {'xy_up': av_up,
                                         'xy_down': av_down}

                    text = to_draw.get('comment') + '\n' + text_split(to_draw.get('module_name'))
                    draw.text((prop_dict.get('Ввод').get('xy_up')[0] + pictures_prop_dict.get('AV')[0],
                               prop_dict.get('Ввод').get('xy_up')[1] - 10),
                              text=text, font=font, fill='black')
                    step = 0
                    for _ in range(3):
                        draw.text((LEFT_TAB, prop_dict.get('Ввод').get('xy_down')[1] - 10 + step),
                                  text=params[_], font=font, fill='black')
                        draw.line(((LEFT_TAB, prop_dict.get('Ввод').get('xy_down')[1] + step),
                                   (BACK_WIDTH - RIGHT_TAB, prop_dict.get('Ввод').get('xy_down')[1] + step)),
                                  fill='black')
                        step += 20
                    prop_dict['third_line'] = {'y': prop_dict.get('Ввод').get('xy_down')[1] + step}
                    # Нижняя горизонтальная черта
                    draw.line(((LEFT_TAB, BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + UP_TAB),
                               (BACK_WIDTH - RIGHT_TAB, BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + UP_TAB)),
                              fill='black')
                    prop_dict['bottom_line'] = {'y': BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + UP_TAB}
                else:
                    if 'АВ' in to_draw['module_name']:
                        if '1п' in to_draw['module_name']:
                            p = 1
                        elif '2п' in to_draw['module_name']:
                            p = 2
                        elif '3п' in to_draw['module_name']:
                            p = 3
                        elif '4п' in to_draw['module_name']:
                            p = 4
                        else:
                            print('Значение полюса не обнаружено, либо не является 1п...4п')
                            break
                        # Отрисовка АВ первого уровня
                        av_up, av_down = av(draw, x=LEFT_TAB + prop_dict.get('first_line_step'),
                                            y=prop_dict.get('third_line').get('y'),
                                            p=p)
                        # Описание модуля АВ первого уровня
                        draw.text((av_up[0] + pictures_prop_dict.get('AV')[0],
                                   av_up[1]), text=text_split(to_draw.get('module_name')), font=font, fill='black')
                        # Линия от верхнего контакта до L1,L2,L3
                        draw.line((av_up, (av_up[0], prop_dict.get('Ввод').get('xy_down')[1])),
                                  fill='black')
                        # Линия от нижнего контакта до комментария
                        draw.line((av_down, (av_down[0], prop_dict.get('bottom_line').get('y'))), fill='black')
                        # Комментарий в описании
                        draw.text((av_down[0] - 12, BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + 5 + UP_TAB),
                                  text=text_split(to_draw['comment']), font=font, fill='black')
                        # Отрисовка линии отделяющей комментарии в случае, когда АВ без УЗО.
                        if LEFT_TAB + pictures_prop_dict.get('AV')[0] + COMMENT_WIDTH + \
                                prop_dict.get('first_line_step') < BACK_WIDTH - RIGHT_TAB:
                            draw.line(((LEFT_TAB + pictures_prop_dict.get('AV')[0] + COMMENT_WIDTH +
                                        prop_dict.get('first_line_step'),
                                        BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + UP_TAB),
                                       (LEFT_TAB + pictures_prop_dict.get('AV')[0] + COMMENT_WIDTH +
                                        prop_dict.get('first_line_step'),
                                        BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + COMMENT_HEIGHT + UP_TAB)),
                                      fill='black')
                        # Увеличение отступа первой линии
                        prop_dict['first_line_step'] += MODULE_NAME_STEP + pictures_prop_dict.get('AV')[0]
                    elif 'УЗО' in to_draw['module_name']:
                        if '1п' in to_draw['module_name']:
                            p = 1
                        elif '2п' in to_draw['module_name']:
                            p = 2
                        elif '4п' in to_draw['module_name']:
                            p = 4
                        else:
                            print('Значение полюса не обнаружено, либо не является 1п...4п')
                            break
                        # Отрисовка УЗО первого уровня
                        uzo_up, uzo_down = uzo(draw, x=LEFT_TAB + prop_dict.get('first_line_step'),
                                               y=prop_dict.get('third_line').get('y') + 6, p=p)
                        # Используется ТОЛЬКО в случае, когда АВ на второй линии один.
                        prop_dict['to_draw_line_2'] = uzo_down[-1]
                        # Описание модуля УЗО
                        draw.text((uzo_up[0][0] + pictures_prop_dict.get(f'UZO{p}p')[0], uzo_up[0][1]),
                                  text=text_split(to_draw.get('module_name')), font=font, fill='black')
                        # Линии от верхних контактов до L1,L2,L3
                        for i in range(p):
                            draw.line((uzo_up[i], (uzo_up[i][0], prop_dict.get('Ввод').get('xy_down')[1])),
                                      fill='black')
                    else:
                        print('В module_name нет информации об УЗО или АВ.')
            elif line.get('line') == 2:
                to_draw = line.get('line_data')
                prop_dict['second_line_step'] = 0
                to_draw_line = []
                for i in to_draw:
                    if len(to_draw) > 1:
                        if '1п' in i['module_name']:
                            p = 1
                        elif '2п' in i['module_name']:
                            p = 2
                        elif '3п' in i['module_name']:
                            p = 3
                        elif '4п' in i['module_name']:
                            p = 4
                        else:
                            print('Значение полюса не обнаружено, либо не является 1п...4п')
                            break
                        # Отрисовка АВ второго уровня
                        av_up, av_down = av(draw, x=LEFT_TAB + prop_dict.get('first_line_step') + prop_dict.get(
                            'second_line_step'),
                                            y=prop_dict.get('third_line').get('y') + pictures_prop_dict.get('UZO1p')[1],
                                            p=p)
                        # Описание модуля АВ
                        draw.text((av_up[0] + (pictures_prop_dict.get('AV')[0] / 2), av_up[1] + 5),
                                  text=text_split(i.get('module_name')), font=font, fill='black')
                        # Добавление координат нового модуля АВ для соединения с УЗО
                        to_draw_line.append((av_up[0], av_up[1] - 1))
                        # Линия от нижнего контакта к описанию
                        draw.line((av_down, (av_down[0], prop_dict.get('bottom_line').get('y'))), fill='black')
                        # Отрисовка линии отделяющей комментарии в случае, когда несколько АВ для УЗО.
                        if LEFT_TAB + pictures_prop_dict.get('AV')[0] + COMMENT_WIDTH + \
                                prop_dict.get('first_line_step') + prop_dict.get('second_line_step') < BACK_WIDTH \
                                - RIGHT_TAB:
                            draw.line(((LEFT_TAB + pictures_prop_dict.get('AV')[0] + COMMENT_WIDTH
                                        + prop_dict.get('first_line_step') + prop_dict.get('second_line_step'),
                                        BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + UP_TAB),
                                       (LEFT_TAB + pictures_prop_dict.get('AV')[0] +
                                        COMMENT_WIDTH + prop_dict.get('first_line_step') +
                                        prop_dict.get('second_line_step'), BACK_HEIGHT - DOWN_TAB -
                                        COMMENT_POSITION + COMMENT_HEIGHT + UP_TAB)), fill='black')
                        # Комментарий
                        draw.text((av_down[0] - 12, BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + 5 + UP_TAB),
                                  text=text_split(i['comment']), font=font, fill='black')
                        # Увеличение отступа второй линии
                        prop_dict['second_line_step'] += MODULE_NAME_STEP + pictures_prop_dict.get('AV')[0]
                    else:
                        if '1п' in to_draw[0]['module_name']:
                            p = 1
                        elif '2п' in to_draw[0]['module_name']:
                            p = 2
                        elif '3п' in to_draw[0]['module_name']:
                            p = 3
                        elif '4п' in to_draw[0]['module_name']:
                            p = 4
                        else:
                            print('Значение полюса не обнаружено, либо не является 1п...4п')
                            break
                        # Отрисовка АВ второго уровня
                        av_up, av_down = av(draw, x=LEFT_TAB + prop_dict.get('first_line_step') + prop_dict.get(
                            'second_line_step'),
                                            y=prop_dict.get('third_line').get('y') + 48, p=p)
                        # Линия соединяющая верхний контакт АВ с последним нижним контактом УЗО
                        draw.line(((av_up[0], av_up[1] - 1), (prop_dict.get('to_draw_line_2')[0],
                                                              prop_dict.get('to_draw_line_2')[1] + 1)), fill='black')
                        # Описания модуля АВ
                        draw.text((av_up[0] + (pictures_prop_dict.get('AV')[0] / 2), av_up[1] + 5),
                                  text=text_split(i.get('module_name')), font=font, fill='black')
                        # Линия от нижнего контакта к комментарию
                        draw.line((av_down, (av_down[0], prop_dict.get('bottom_line').get('y'))),
                                  fill='black')
                        # Комментарий модуля АВ.
                        draw.text((av_down[0] - 12, BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + 5 + UP_TAB),
                                  text=text_split(to_draw[0]['comment']), font=font, fill='black')
                        # Увеличение отступа второй линии
                        prop_dict['second_line_step'] += MODULE_NAME_STEP + pictures_prop_dict.get('AV')[0] + 20
                        # Отрисовка линии отделяющей комментарии в случае, когда АВ в единичном экземпляре для УЗО.
                        if LEFT_TAB + pictures_prop_dict.get('AV')[0] + COMMENT_WIDTH + prop_dict.get(
                                'first_line_step') < BACK_WIDTH - RIGHT_TAB:
                            draw.line((
                                (LEFT_TAB + pictures_prop_dict.get('AV')[
                                    0] + COMMENT_WIDTH + prop_dict.get('first_line_step'),
                                 BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + UP_TAB),
                                (LEFT_TAB + pictures_prop_dict.get('AV')[
                                    0] + COMMENT_WIDTH + prop_dict.get('first_line_step'),
                                 BACK_HEIGHT - DOWN_TAB - COMMENT_POSITION + COMMENT_HEIGHT + UP_TAB)),
                                fill='black')
                # Отрисовка линии соединяющей контакты второй линии АВ с УЗО
                if to_draw_line:
                    draw.line((to_draw_line[0], to_draw_line[-1]), fill='black')
                # Увеличение отступа первой линии на отступ второй линии
                prop_dict['first_line_step'] += prop_dict.get('second_line_step')
    back.save(f'Scheme_{prop_dict.get("spec_id")}_list_{prop_dict.get("list_number")}.jpg', quality=100)
    prop_dict.get('list_names').append(f'Scheme_{prop_dict.get("spec_id")}'
                                       f'_list_{prop_dict.get("list_number")}.jpg')
    # Save to buffer BytesIO, if uncomment - change RETURN
    # prop_dict['buffers'][f'list{prop_dict.get("list_number")}'] = io.BytesIO()
    # back.save(prop_dict['buffers'][f'list{prop_dict.get("list_number")}'], format='JPEG')
    # return prop_dict.get('list_names'), prop_dict.get('buffers')
    return prop_dict.get('list_names')


if __name__ == "__main__":
    # names, buffers = schema_save_to_jpg(2269)
    names = schema_save_to_jpg(2269)
    # for list_name in buffers:
    #     print(f'{list_name} - {buffers[list_name]}')
    #     Image.open(buffers[list_name]).show()
    #     buffers[list_name].close()
    print(names)
