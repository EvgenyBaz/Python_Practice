# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_str = "ылваыв фбвв длдлоабв длоаб абволло"

text_list = text_str.split(" ")
# print(text_list )

text_str_new = ''
for i in text_list:
    if not((lambda x: 'абв' in x)(i)):
       text_str_new = text_str_new+i+' '

print(text_str_new)