import os
import hashlib
import xlsxwriter

def search_duplicate_files():
    file_name = 'task2'
    files = os.listdir(file_name)
    nums = []
    for file in files:
        with open(file_name + '\\' + file) as file:
            nums.append(hashlib.md5(file.read().encode('utf-8')).hexdigest())
            workbook = xlsxwriter.Workbook('duplicates.xlsx')
            worksheet = workbook.add_worksheet()
            
    for i in range(len(files) - 1):
        for j in range(i + 1, len(files)):
            if nums[i] == nums[j]:
                print('Группа дубликатов:', files[i], files[j])
                worksheet.write(i, 0, files[i])
                worksheet.write(i, 1, files[j])
                workbook.close()
                
search_duplicate_files()