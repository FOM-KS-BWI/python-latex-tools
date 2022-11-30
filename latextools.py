def make_latex_table(tabelle, booktab=False):
    '''

    :param booktab: If true, the table will get booktab-style lines.
    :param tabelle: A list of lists representing the table content.
    :return:
    '''

    table_width = 0
    row_content = ''
    if booktab:
        row_content += '\\toprule\n'
    for row in tabelle:
        cur_len = len(row)
        if cur_len > table_width:
            table_width = cur_len
        row_content += ' & '.join(row)+'\\\\\n'
    if booktab:
        row_content += r'\bottomrule'
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