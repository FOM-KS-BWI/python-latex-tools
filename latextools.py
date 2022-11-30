def make_latex_table(tabelle,
                     booktab=False,
                     first_row_changed=False,
                     last_row_changed=False):
    '''

    :param booktab: If true, the table will get booktab-style lines.
    :param first_row_changed: If true, a line will be inserted after first line
    :param last_row_changed: If true, a line will be inserted before last line
    :param tabelle: A list of lists representing the table content.
    :return:
    '''

    table_width = 0
    table_length = len(tabelle)
    row_content = ''
    if booktab:
        row_content += '\\toprule\n'
    for i, row in enumerate(tabelle):
        cur_len = len(row)
        if cur_len > table_width:
            table_width = cur_len
        row_content += ' & '.join(row)+'\\\\\n'
        if first_row_changed and i == 0:
            if booktab:
                row_content += '\\midrule\\\\\n'
            else:
                row_content += '\\hrule\\\\\n'
        elif last_row_changed and i == table_length - 2:
            # Second last row, so add rule
            row_content += '\\' + ('mid' if booktab else 'h') + 'rule\\\\\n'
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
    latex_tabelle = make_latex_table(tabelle, booktab=True, first_row_changed=True, last_row_changed=True)
    print(latex_tabelle)