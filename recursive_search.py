import os

path = 'C:\\Program Files (x86)'


def obxodFile(path, level=1):
    print('Level = ', level, 'Content: ', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            obxodFile(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)
obxodFile(path)
