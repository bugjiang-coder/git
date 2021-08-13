import os


def FindMethod(file, output_fd, root):
    # 跳过alipay包
    # if(file.find('ali') != -1):
    #     return
    # 写入文件名
    # output_fd.write('\n'+file_name+'\n')
    file_written_counter = 0
    r = len(root)
    print(file[r:])
    with open(file) as f:
        line_array = f.readlines()
        for line in line_array:
            if (((line.find('alert') != -1
                    or line.find('toast') != -1
                    or line.find('Alert') != -1)
                 and line.find('invoke') != -1
                 and line.find('String') != -1)
                    or line.find('Error') != -1
                    or line.find('warn') != -1):

                if(file_written_counter == 0):
                    output_fd.write('\n'+file[r:]+'\n')
                file_written_counter += 1
                output_fd.write('[%d'%(file_written_counter) + ']' + line)
                


def GetNameAndMethod(rootDir):
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root, file)
            FindMethod(file_name, output_fd, rootDir)
        for dir in dirs:
            GetNameAndMethod(dir)


def getStrings(rootDir):
    compact_file = r'E:\ImmuneDroid_script\apkstrings.txt'
    output_fd = open(compact_file, 'a+')
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            # 获取smali文件名
            file_name = os.path.join(root, file)
            # 写入文件名
            # output_fd.write('\n'+file_name+'\n')
            file_written = 0
            print(file_name)
            with open(file_name) as f:
                line_array = f.readlines()
                for line in line_array:
                    str_begin = 0
                    while(str_begin != -1 or str_begin < len(line)):
                        str_begin = line.find('\"', str_begin)
                        if(str_begin != -1):
                            str_end = line.find('\"', str_begin+1)
                            if(file_written == 0):
                                file_written = 1
                                output_fd.write('\n'+file_name+'\n')
                            output_fd.write(line[str_begin:str_end]+'\n')
                            str_begin = str_end+1
                        else:
                            break


if __name__ == '__main__':
    # smali文件路径，文件夹下面的文件都是smali文件
    root = r'D:\文件\学习\课程\曦源项目\com.eg.android.AlipayGphone\支付宝_10.2.20.7000_390_com.eg.android.AlipayGphone_main_standalone\smali0'

    # 保存文件名，可以一开始没有会自动创建
    compact_file = r'D:\文件\学习\课程\曦源项目\com.eg.android.AlipayGphone\ali.txt'
    output_fd = open(compact_file, 'a+')

    # try:
    GetNameAndMethod(root)

    # 下面函数未测试成功，不要使用
    # getStrings(root)
    # finally:
    output_fd.close()
