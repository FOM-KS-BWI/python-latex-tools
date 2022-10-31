import csv

f = open('ExcelTest1.CSV', encoding='ISO-8859-1')
csv_reader = csv.reader(f)
for line in csv_reader:
    print(line)
f.close()
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
    tabelle = [
        ['A', 'B', 'C', 'D'],
        ['Titel 1', 'wert 1', 'wert 2', 'wert 3'],
        ['Titel 2', 'wert 4', 'wert 5', 'wert 6'],
    ]
    latex_tabelle = make_latex_table(tabelle)
    print(latex_tabelle)

