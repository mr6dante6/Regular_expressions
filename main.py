import csv
import re


def format_phone(num_phone):
    num_phone = re.sub(r'[^0-9]', '', num_phone)
    if len(num_phone) == 11:
        return f'+7({num_phone[1:4]}){num_phone[4:7]}-{num_phone[7:9]}-{num_phone[9:]}'
    else:
        return f'+7({num_phone[:3]}){num_phone[3:6]}-{num_phone[6:8]}-{num_phone[8:10]} доб.{num_phone[10:]}'


with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contacts_list = []

for contact in contacts_list:
    fio = f'{contact[0]} {contact[1]} {contact[2]}'.split()
    if len(fio) == 2:
        fio.append('')
    elif len(fio) == 1:
        fio.extend(['', ''])
    phone = format_phone(contact[5])
    for new_contact in new_contacts_list:
        if new_contact[0] == fio[0] and new_contact[1] == fio[1]:
            if new_contact[2] == '' and fio[2] != '':
                new_contact[2] = fio[2]
            if new_contact[3] == '' and contact[3] != '':
                new_contact[3] = contact[3]
            if new_contact[4] == '' and contact[4] != '':
                new_contact[4] = contact[4]
            if new_contact[5] == '' and phone != '':
                new_contact[5] = phone
            if new_contact[6] == '' and contact[6] != '':
                new_contact[6] = contact[6]
            break
    else:
        new_contacts_list.append(fio + [contact[3], contact[4], phone, contact[6]])

new_contacts_list[0][5] = "phone"

with open("phonebook.csv", "w", encoding="utf8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
