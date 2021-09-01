# import pandas
#
# spec = pandas.read_csv('spec 2268.csv')
# dict_spec = spec.to_dict()
# my_dict = {}
# for i in spec.index:
#     my_dict[i] = {j: 0 for j in spec.head()}
#     for k in my_dict[i]:
#         my_dict[i][k] = spec.get(k).get(i)

# SPEC_ONE = {0: {'line_id': 4903, 'header_id': 2269, 'module_name': 'АВ 1п 16А C', 'qty': 1, 'comment': 'Резерв 1'},
#             1: {'line_id': 4904, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1,
#                 'comment': 'Наружное электроснабжение'},
#             2: {'line_id': 4905, 'header_id': 2269, 'module_name': 'УЗО 50А 30мА AC M 2п', 'qty': 1,
#                 'comment': 'Наружное электроснабжение'},
#             3: {'line_id': 4906, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1,
#                 'comment': 'Посудомоечная машина'},
#             4: {'line_id': 4907, 'header_id': 2269, 'module_name': 'УЗО 50А 30мА AC M 2п', 'qty': 1,
#                 'comment': 'Посудомоечная машина'},
#             5: {'line_id': 4908, 'header_id': 2269, 'module_name': 'АВ 2п 32А C', 'qty': 1,
#                 'comment': 'Варочная поверхность'},
#             6: {'line_id': 4909, 'header_id': 2269, 'module_name': 'УЗО 50А 30мА AC M 2п', 'qty': 1,
#                 'comment': 'Варочная поверхность'},
#             7: {'line_id': 4910, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1, 'comment': 'Духовой шкаф'},
#             8: {'line_id': 4911, 'header_id': 2269, 'module_name': 'УЗО 50А 30мА AC M 2п', 'qty': 1,
#                 'comment': 'Духовой шкаф'},
#             9: {'line_id': 4912, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1,
#                 'comment': 'Сан.узел 1 Линия 1'},
#             10: {'line_id': 4913, 'header_id': 2269, 'module_name': 'УЗО 50А 30мА AC M 2п', 'qty': 1,
#                  'comment': 'Сан.узел 1'},
#             11: {'line_id': 4914, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1,
#                  'comment': 'Розеточная группа 2 Линия 2'},
#             12: {'line_id': 4915, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1,
#                  'comment': 'Розеточная группа 2 Линия 1'},
#             13: {'line_id': 4916, 'header_id': 2269, 'module_name': 'УЗО 50А 30мА AC M 2п', 'qty': 1,
#                  'comment': 'Розеточная группа 2'},
#             14: {'line_id': 4917, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1,
#                  'comment': 'Розеточная группа 1 Линия 2'},
#             15: {'line_id': 4918, 'header_id': 2269, 'module_name': 'АВ 2п 16А C', 'qty': 1,
#                  'comment': 'Розеточная группа 1 Линия 1'},
#             16: {'line_id': 4919, 'header_id': 2269, 'module_name': 'УЗО 50А 30мА AC M 2п', 'qty': 1,
#                  'comment': 'Розеточная группа 1'},
#             17: {'line_id': 4920, 'header_id': 2269, 'module_name': 'АВ 1п 10А C', 'qty': 1,
#                  'comment': 'Освещение группа 2'},
#             18: {'line_id': 4921, 'header_id': 2269, 'module_name': 'АВ 1п 10А C', 'qty': 1,
#                  'comment': 'Освещение группа 1'},
#             19: {'line_id': 4922, 'header_id': 2269, 'module_name': 'РН 2п 63А', 'qty': 1,
#                  'comment': 'Реле напряжения'},
#             20: {'line_id': 4923, 'header_id': 2269, 'module_name': 'УЗО 50А 300мА AC M 2п', 'qty': 1,
#                  'comment': 'Противопожарное УЗО'},
#             21: {'line_id': 4924, 'header_id': 2269, 'module_name': 'УЗИП 2п 20кА', 'qty': 1, 'comment': 'УЗИП'},
#             22: {'line_id': 4925, 'header_id': 2269, 'module_name': 'АВ 2п 50А C', 'qty': 1, 'comment': 'Ввод'}}

# SPEC = {
#     'header_id': 2269,
#     'spec': [
#         {'group_id': 1, 'data': [{'group_line_id': 1, 'line_data': ('АВ 4п 25А C', 'Ввод')}]},
#         {'group_id': 2, 'data': [{'group_line_id': 1, 'line_data': ('УЗИП 4п 20кА', 'УЗИП')}]},
#         {'group_id': 3, 'data': [{'group_line_id': 1, 'line_data': ('УЗО 25А 300мА AC M 4п', 'Противопожарное УЗО')}]},
#         {'group_id': 4, 'data': [{'group_line_id': 1, 'line_data': ('РН 3п 63А', 'Реле напряжения')}]},
#         {'group_id': 5, 'data': [{'group_line_id': 1, 'line_data': ('АВ 1п 10А C', 'Освещение группа 1')}]},
#         {'group_id': 6, 'data': [{'group_line_id': 1, 'line_data': ('АВ 1п 10А C', 'Освещение группа 2')}]},
#         {'group_id': 7, 'data': [{'group_line_id': 1, 'line_data': ('УЗО 25А 30мА AC M 2п', 'Розеточная группа 1')},
#                                  {'group_line_id': 2, 'line_data': [('АВ 2п 16А C', 'Розеточная группа 1 Линия 1'),
#                                                                     ('АВ 2п 16А C', 'Розеточная группа 1 Линия 2'),
#                                                                     ('АВ 2п 16А C', 'Розеточная группа 1 Линия 3')]}]},
#         {'group_id': 8, 'data': [{'group_line_id': 1, 'line_data': ('УЗО 25А 30мА AC M 2п', 'Сан.узел 1')},
#                                  {'group_line_id': 2, 'line_data': [('АВ 2п 16А C', 'Сан.узел 1 Линия 1'),
#                                                                     ('АВ 2п 16А C', 'Сан.узел 1 Линия 2')]}]},
#         {'group_id': 9, 'data': [{'group_line_id': 1, 'line_data': ('УЗО 25А 30мА AC M 2п', 'Духовой шкаф')},
#                                  {'group_line_id': 2, 'line_data': ('АВ 2п 16А C', 'Духовой шкаф')}]},
#         {'group_id': 10, 'data': [{'group_line_id': 1, 'line_data': ('УЗО 25А 30мА AC M 2п', 'Варочная поверхность')},
#                                   {'group_line_id': 2, 'line_data': ('АВ 2п 16А C', 'Варочная поверхность')}]},
#         {'group_id': 11, 'data': [{'group_line_id': 1, 'line_data': ('УЗО 25А 30мА AC M 2п', 'Посудомоечная машина')},
#                                   {'group_line_id': 2, 'line_data': ('АВ 2п 16А C', 'Посудомоечная машина')}]},
#         {'group_id': 12, 'data': [{'group_line_id': 1, 'line_data': ('УЗО 25А 30мА AC M 2п', 'Наружное электроснабжение')},
#                                   {'group_line_id': 2, 'line_data': ('АВ 2п 16А C', 'Наружное электроснабжение')}]},
#         {'group_id': 13, 'data': [{'group_line_id': 1, 'line_data': ('АВ 1п 16А C', 'Резерв 1')}]},
#         {'group_id': 14, 'data': [{'group_line_id': 1, 'line_data': ('АВ 1п 16А C', 'Резерв 2')}]}
#     ]
# }


SPEC = {
'header_id': 2269,
'spec': [
    {'group_id': 1, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'АВ 4п 25А C', 'comment': 'Ввод'}}]},
    {'group_id': 2, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗИП 4п 20кА', 'comment': 'УЗИП'}}]},
    {'group_id': 3, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗО 25А 300мА AC M 4п', 'comment': 'Противопожарное УЗО'}}]},
    {'group_id': 4, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'РН 3п 63А', 'comment': 'Реле напряжения'}}]},
    {'group_id': 5, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'АВ 1п 10А C', 'comment': 'Освещение группа 1'}}]},
    {'group_id': 6, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'АВ 1п 10А C', 'comment': 'Освещение группа 2'}}]},
    {'group_id': 7, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗО 25А 30мА AC M 4п', 'comment': 'Розеточная группа 1'}},
                             {'line': 2, 'line_data': [{'item_id': 2, 'module_name': 'АВ 1п 16А C', 'comment': 'Розеточная группа 1 Линия 1'},
                                                       {'item_id': 3, 'module_name': 'АВ 2п 16А C', 'comment': 'Розеточная группа 1 Линия 2'},
                                                       {'item_id': 4, 'module_name': 'АВ 3п 16А C', 'comment': 'Розеточная группа 1 Линия 3'},
{'item_id': 4, 'module_name': 'АВ 3п 16А C', 'comment': 'Розеточная группа 1 Линия 3'},
                                                       {'item_id': 4, 'module_name': 'АВ 3п 16А C', 'comment': 'Розеточная группа 1 Линия 3'},
                                                       {'item_id': 5, 'module_name': 'АВ 4п 16А C', 'comment': 'Розеточная группа 1 Линия 4'}]}]},
    {'group_id': 8, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗО 25А 30мА AC M 2п', 'comment': 'Сан.узел 1'}},
                             {'line': 2, 'line_data': [{'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Сан.узел 1 Линия 1'},
                                                       {'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Сан.узел 1 Линия 1'},
                                                       {'item_id': 3, 'module_name': 'АВ 2п 16А C', 'comment': 'Сан.узел 1 Линия 2'}]}]},
    {'group_id': 9, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗО 25А 30мА AC M 2п', 'comment': 'Духовой шкаф'}},
                             {'line': 2, 'line_data': [{'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Духовой шкаф'}]}]},
    {'group_id': 10, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗО 25А 30мА AC M 1п', 'comment': 'Варочная поверхность'}},
                              {'line': 2, 'line_data': [{'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Варочная поверхность'}]}]},
    {'group_id': 11, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗО 25А 30мА AC M 2п', 'comment': 'Посудомоечная машина'}},
                              {'line': 2, 'line_data': [{'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Посудомоечная машина'}]}]},
    {'group_id': 12, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'УЗО 25А 30мА AC M 2п', 'comment': 'Наружное электроснабжение'}},
                              {'line': 2, 'line_data': [{'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Наружное электроснабжение'},
                                                        {'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Наружное электроснабжение'},
                                                        {'item_id': 2, 'module_name': 'АВ 2п 16А C', 'comment': 'Наружное электроснабжение'}]}]},
    {'group_id': 13, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'АВ 1п 16А C', 'comment': 'Резерв 1'}}]},
    {'group_id': 14, 'data': [{'line': 1, 'line_data': {'item_id': 1, 'module_name': 'АВ 1п 16А C', 'comment': 'Резерв 2'}}]}
]
}