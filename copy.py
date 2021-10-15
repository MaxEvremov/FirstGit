filename1=input("Введите название копируемого файла")
filename2=input("Впишите название файла-копии")

file1=open(filename1,'rb')
file2=open(filename2,'wb')

file2.write(file1.read())

file1.close()
file2.close()

print("Копирование успешно завершено")