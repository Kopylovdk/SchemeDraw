from pandas import read_sql_query, DataFrame
import psycopg2
from const import EXCEPTION


def sql_data_parser(spec_id):
    conn = psycopg2.connect(
        database='app',
        user='postgres',
        password='eshoongoo',
        host='db',
        port='5432',
    )

    sql = f""" SELECT header_id, module_name, comment
            FROM temp_pro.spec_lines
            where header_id={spec_id}
            order by line_id desc;"""

    pars_data = DataFrame(read_sql_query(sql, conn))
    result = {'header_id': pars_data.iloc[0]['header_id'],
              'spec': []}
    group_id = 0
    spec_len = len(pars_data.index)
    i = 0
    while i < spec_len:
        group_to_insert = {'group_id': group_id + 1, 'data': []}
        comment = pars_data.iloc[i]['comment']
        module_name = pars_data.iloc[i]['module_name']
        if comment in EXCEPTION:
            i += 1
            continue
        first_line = {'line': 1, 'line_data': {'module_name': module_name, 'comment': comment}}
        second_line = {'line': 2, 'line_data': []}
        if i + 1 < spec_len:
            raw_cnt = 0
            for j in range(i, spec_len):
                if comment in EXCEPTION:
                    j += 1
                    continue
                elif j + 1 == spec_len:
                    second_line.get('line_data').append({'module_name': pars_data.iloc[j + 1]['module_name'],
                                                         'comment': pars_data.iloc[j + 1]['comment']})
                    raw_cnt += 1
                    break
                elif comment in pars_data.iloc[j + 1]['comment']:
                    second_line.get('line_data').append({'module_name': pars_data.iloc[j + 1]['module_name'],
                                                         'comment': pars_data.iloc[j + 1]['comment']})
                    raw_cnt += 1
                else:
                    break
            i += raw_cnt
            group_to_insert['data'].append(first_line)
            if second_line.get('line_data'):
                group_to_insert['data'].append(second_line)
            group_id += 1
        else:
            group_to_insert['data'].append(first_line)
        i += 1
        if group_to_insert['data']:
            result.get('spec').append(group_to_insert)
    return result
