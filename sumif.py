# -*- coding: utf-8 -*-
import openpyxl


def sumif_Excel(path, sheet_name, row, *col):
    # 默认从第二行开始,因为很多表都有表头
    if row == '':
        row = 2
    else:
        row = int(row)
    workbook = openpyxl.load_workbook(path)
    # 默认打开当前激活的工作表
    if sheet_name == "":
        sheet0 = workbook.active  # 获取当前激活的工作表
    else:
        sheet0 = workbook[sheet_name]  # 如果制定了工作表，就打开指定的工作表
    highest = sheet0.max_row
    case_list = {}
    # title 所在列，对比的那一列，假设A列
    title = col[0]
    for i in range(row, highest + 1):  # 遍历行
        value_list = []
        if sheet0[title + str(i)].value is None:  # 如果A5是空的，pass
            pass
        else:
            v1 = sheet0[title + str(i)].value  # 忽略大小写和前后空格
            v2 = sheet0[col[1] + str(i)].value
            if v1 in case_list.keys():
                case_list[v1] = v2 + case_list[v1]
            else:
                case_list[v1] = v2

    print (case_list)
    return case_list


def manual():
    info1 = raw_input('Read from fileName,[sheetName],[row],columns:\n')
    file1, sheet_name1, row1, list1 = info1.split(',')
    r1 = sumif_Excel(file1, sheet_name1, row1, *list1)
    print (r1)
    print('Done.')


if __name__ == "__main__":
    manual()
