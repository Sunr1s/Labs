import pymorphy2
morph = pymorphy2.MorphAnalyzer(lang='uk')

Token_text = ['Отримано', 'аналіз', 'програмних', 'застосунків', 'конкурентів', '.', 'Створивши', 'таблицю', 'порівняли', 'плюси', 'мінуси', ',', 'визначили', 'необхідні', 'функіональні', 'вимоги', '.', 'Вимоги', 'конфеденційності', 'безпеки', '.', 'Визначили', 'можливі', 'проблеми', 'вразливості', 'ринку', 'вирішення', 'привести', 'нововедення', 'ринок', 'IT', 'послуг', '.', 'Також', 'отпримаємо', 'список', 'вимог', 'розробки', ',', 'можливо', 'уникнимо', 'допрацювання', 'ПЗ', ',', 'виконавши', 'повне', 'ТЗ', 'одразу', '.']

for ele in Token_text:
    p = morph.parse(ele)[0]
    print(p.normal_form, end=' ')