import re

# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

ind_name = 0
for i in contacts_list:
  lastname = re.split(r"\s", contacts_list[ind_name][0])
  firstname = re.split(r"\s", contacts_list[ind_name][1])
  contacts_list[ind_name][0] = lastname[0]
  if len(lastname) == 2:
    contacts_list[ind_name][1] = lastname[1]
  elif len(lastname) == 3:
    contacts_list[ind_name][1] = lastname[1]
    contacts_list[ind_name][2] = lastname[2]
  if len(firstname) == 2:
    contacts_list[ind_name][1] = firstname[0]
    contacts_list[ind_name][2] = firstname[1]
  ind_name += 1

pattern_phone = r"(\+7|8)\s*\(*(\d)(\d)(\d)\)*(\s+|-?)(\d)(\d)(\d)(\s+|-?)(\d)(\d)(\s+|-?)(\d+)(\s*)\(*([доб.]*)\s*(\d*)\)*"
substitution = r"+7(\2\3\4)\6\7\8-\10\11-\13\14\15\16"
ind_phone = 0
for user in contacts_list:
  phone = re.sub(pattern_phone, substitution, user[5])
  contacts_list[ind_phone][5] = phone
  ind_phone += 1


for contact_1 in contacts_list:
  for contact_2 in contacts_list:
    if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1] and contact_1 != contact_2:
      for i in range(7):
        if contact_1[i] == '':
          contacts_list[contacts_list.index(contact_1)][i] = contacts_list[contacts_list.index(contact_2)][i]
      del(contacts_list[contacts_list.index(contact_2)])


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)