import csv

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
    file = open("ExcelTest1.CSV", "r")
    data = list(csv.reader(file, delimiter=";"))
    file.close()
    print(data)

    tabelle = [
        ['A', 'B', 'C', 'D'],
        ['Titel 1', 'wert 1', 'wert 2', 'wert 3'],
        ['Titel 2', 'wert 4', 'wert 5', 'wert 6'],
    ]
    latex_tabelle = make_latex_table(tabelle)
    print(latex_tabelle)