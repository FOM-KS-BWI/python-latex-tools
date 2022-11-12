def make_latex_table(tabelle):
    '''

    :param tabelle:
    :return:
    '''

    table_width = 0
    row_content = ''
    for row in tabelle:
        cur_len = len(row)
        if cur_len > table_width:
            table_width = cur_len
        row_content += ' & '.join(row)+'\\\\\n'
    latex_code = r'''
\begin{tabular}{COLUMNS}
CONTENT
\end{tabular}'''\
        .replace('COLUMNS', 'l'*table_width)\
        .replace('CONTENT', row_content)
    return latex_code


if __name__ == '__main__':
    print('LaTeX-Tools')
    import csv
    with open('ExcelTest1.CSV') as f:
        csv_reader = csv.reader(f, delimiter=';')
        tabelle = [line for line in csv_reader]
    latex_tabelle = make_latex_table(tabelle)
    print(latex_tabelle)