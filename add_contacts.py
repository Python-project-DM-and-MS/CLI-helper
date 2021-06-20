from validation import *


def add_contact():
    record, value = {}, []
    value.append(add_phone())
    value.append(add_email())
    value.append(add_birthday())
    value.append(add_note())
    record[add_name()] = value


def add_name():
    name = input('INPUT YOUR CONTACT NAME >> ')
    return name


def add_phone():
    phone = []
    while True:
        contact_phone = input('INPUT YOUR CONTACT PHONE IN FORMAT +380 >> ')
        # здесь будет валидация
        if not check_phone(contact_phone):
            print('YOU ENTERED WRONG NUMBER! RE-ENTER, PLEASE')
            continue
        else:
            phone.append(contact_phone)
            print('DO YOU WANT TO ADD ANOTHER NUMBER? Y/n >> ')
            answer = input()
            if answer.lower() == 'y':
                continue
            else:
                break
    return phone


def add_email():
    email = []
    while True:
        contact_email = input('INPUT YOUR CONTACT EMAIL >> ')
        # здесь будет валидация
        if not check_email(contact_email):
            print('YOU ENTERED WRONG EMAIL! RE-ENTER, PLEASE')
            continue
        else:
            email.append(contact_email)
            print('DO YOU WANT TO ADD ANOTHER EMAIL? Y/n >> ')
            answer = input()
            if answer.lower() == 'y':
                continue
            else:
                break
    return email


def add_birthday():
    while True:
        birthday = input('INPUT YOUR CONTACT BIRTHDAY (DD/MM/YYYY) >> ')
        # здесь будет валидация
        if not check_birthday(birthday):
            print('YOU ENTERED WRONG BIRTHDAY DATE! RE-ENTER, PLEASE')
            continue
        else:
            break
    return birthday


def add_note():
    note = input('INPUT YOUR CONTACT NOTE >> ')
    return note


def add_note_tag():
    tags = input('INPUT TAGS FOR YOUR NOTE >> ')
    return tags
