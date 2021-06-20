''' normalize function transliterates Cyrillic characters into Latin;
    replaces all characters except letters of the Latin alphabet and numbers with the character '_';
    uppercase letters remain uppercase and lowercase letters remain lowercase after transliteration
'''


def normalize(text):
    dictionary = {ord('А'): 'A',ord('Б'): 'B',ord('В'): 'V',ord('Г'): 'H',ord('Ґ'): 'G',ord('Д'): 'D',ord('Е'): 'E',ord('Є'): 'Ye',ord('Ж'): 'Zh',\
    ord('З'): 'Z',ord('И'): 'Y',ord('І'): 'I',ord('Ї'): 'Yi',ord('Й'): 'Y',ord('К'): 'K',ord('Л'): 'L',ord('М'): 'M',ord('Н'): 'N',ord('О'): 'O',\
    ord('П'): 'P',ord('Р'): 'R',ord('С'): 'S',ord('Т'): 'T',ord('У'): 'U',ord('Ф'): 'F',ord('Х'): 'Kh',ord('Ц'): 'Ts',ord('Ч'): 'Ch',ord('Ш'): 'Sh',\
    ord('Щ'): 'Shch',ord('Ь'): '',ord('Ю'): 'Yu',ord('Я'): 'Ya',ord('а'): 'a',ord('б'): 'b',ord('в'): 'v',ord('г'): 'h',('ґ'): 'g',ord('д'): 'd',\
    ord('е'): 'e',ord('є'): 'ie',ord('ж'): 'zh',ord('з'): 'z',ord('и'): 'y',ord('і'): 'i',ord('ї'): 'i',ord('й'): 'i',ord('к'): 'k',ord('л'): 'l',\
    ord('м'): 'l',ord('н'): 'n',ord('о'): 'o',ord('п'): 'p',ord('р'): 'r',ord('с'): 's',ord('т'): 't',ord('у'): 'u',ord('ф'): 'f',ord('х'): 'kh',\
    ord('ц'): 'ts',ord('ч'): 'ch',ord('ш'): 'sh',ord('щ'): 'shch',ord('ь'): '',ord('ю'): 'iu',ord('я'): 'ia'}
    keys = []
    for key in dictionary:
        keys.append(key)
    normalized_text = []
    for letter in text:
        if ord(letter) in keys:
            letter = letter.translate(dictionary)
            normalized_text.append(letter)
        elif 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            normalized_text.append(letter)
        elif letter.isdigit():
            normalized_text.append(letter)
        else:
            normalized_text.append('_')
    normalized_text = ''.join(normalized_text)
    return normalized_text


'''create_folders function creates folders by main types of files: images, videos, documents, audio and archives'''


def create_folders(folder_path):
    os.mkdir(folder_path+'\\Images')
    os.mkdir(folder_path+'\\Videos')
    os.mkdir(folder_path+'\\Documents')
    os.mkdir(folder_path+'\\Audio')
    os.mkdir(folder_path+'\\Archives')


'''move_files function moves files from iterated folder to folders by their type
   unpack archives in 'Archive' folder creating new folder named exactly as archive file without extension
'''
def move_files(path, folder_path):
    for element in path.glob('**/*.*'):
        if element.suffix in ['.zip'] or element.suffix in ['.gz'] or element.suffix in ['.tar']:
            shutil.unpack_archive(element, folder_path+'\\Archives\\'+element.stem)  
        elif element.suffix in ['.png'] or element.suffix in ['.jpeg'] or element.suffix in ['.jpg'] or element.suffix in ['.svg']:
            shutil.move(element, folder_path+'\\Images')
        elif element.suffix in ['.avi'] or element.suffix in ['.mp4'] or element.suffix in ['.mov'] or element.suffix in ['.mkv']:
            shutil.move(element, folder_path+'\\Videos')
        elif element.suffix in ['.mp3'] or element.suffix in ['.ogg'] or element.suffix in ['.wav'] or element.suffix in ['.amr']:
            shutil.move(element, folder_path+'\\Audio')
        elif element.suffix in ['.doc'] or element.suffix in ['.docx'] or element.suffix in ['.txt'] or element.suffix in ['.pdf'] or element.suffix in ['.xlsx'] or element.suffix in ['.pptx']:
            shutil.move(element, folder_path+'\\Documents')


'''rename_files function transliterates file`s name according to normalize function description above and renames it'''


def rename_files(path):
    for element in path.glob('**/*.*'):
        if element.suffix != '':
            os.rename(element, f'{element.parent}\\{normalize(element.stem)}{element.suffix}')


'''rename_folders function transliterates folder`s name according to normalize function description above and renames it'''


def rename_folders(path):
    for directory in path.iterdir():
        if directory.is_dir():
            rename_folders(directory)
            os.rename(directory, f'{directory.parent}\\{normalize(directory.stem)}')
        else:
            continue


''' delete_empty_folders function deletes all empty subfolders'''

def delete_empty_folders(path, folder_path):
    for directory in os.listdir(path):
        checking_pass = os.path.join(path, directory)
        if checking_pass == (folder_path+'\\Images') or checking_pass == (folder_path+'\\Videos') or checking_pass == (folder_path+'\\Documents')\
        or checking_pass == (folder_path+'\\Audio') or checking_pass == (folder_path+'\\Archives'):
            continue
        elif os.path.isdir(checking_pass):
            if not os.listdir(checking_pass):
                os.removedirs(checking_pass)
            else:
                delete_empty_folders(checking_pass, folder_path)


''' sort_folder function renames all files and folders using the normalize function (described above).
    file extensions do not change after renaming.
    empty folders are deleted
    the script ignores the archives, video, audio, documents, images folders;
    the unpacked contents of the archive are moved to the archives folder in a subfolder named exactly the same as the archive, 
    but without the extension at the end;
    files with unknown extensions remain unchanged.
'''
def sort_folder():
    folder_path = input('Enter the folder path you need to sort: ') # input Windows folder path
    if os.path.exists(folder_path):
        path = pathlib.Path(folder_path)
    else:
        folder_path = input('Path does not exist. Please enter correct path: ')
        path = pathlib.Path(folder_path)
    try:
        create_folders(folder_path)
    except FileExistsError:
        pass    
    rename_files(path)
    rename_folders(path)
    move_files(path, folder_path)
    delete_empty_folders(path, folder_path)


if __name__ == '__main__':
    import pathlib
    import os
    import shutil

    sort_folder()
