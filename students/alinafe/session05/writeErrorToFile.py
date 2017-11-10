import traceback

try:
    raise Exception('This is an error!!!')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback infor was written to errorInfo.txt')