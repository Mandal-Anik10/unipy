# Content of the LocalModule:

import pandas as pd
from tabulate import tabulate


def Show():
    sheet = pd.read_excel(r'C:\Users\Anik Mandal\PycharmProjects\Local-Packages\LocalModule\Module Content.xlsx')

    sheet = sheet.fillna("")

    print(tabulate(sheet, showindex=False, headers=sheet.columns))
    return
