import codecs
import linecache


def listDbConf(fileList):
    listContent = []
    for file in fileList:
        # print(file)
        # print(file)
        fn_read = codecs.open(file, 'r+b', encoding='utf-8', errors='ignore')
        content = fn_read.readlines()
        fn_read.close()
        a = "行"
        for string_db in content:
            result = {}

            if a in string_db.strip():

                result[string_db.strip().split('行第')[0]] = string_db.strip().split('行第')[0]

                listContent.append(result)

        # print(listContent)

    return listContent


def listNumber(listContent):
    num = []
    for l in listContent:
        for item in l.values():
            num.append(item.split("第")[1])
            # print(item)
        # print(num)
    return num


def addLine(file):
    n = 1
    listCon = []
    fn_read = codecs.open(file, 'r+b', encoding='utf-8', errors='ignore')
    content = fn_read.readlines()
    fn_read.close()

    for string_db in content:
        result = {n: string_db}
        n += 1
        # print(result)
        listCon.append(result)
        # print(listCon.)
    return listCon


def outputResult(listCon,num):
    # print(num)
    file_obj = open("123.txt","w")
    # print(num)
    # for n in num:
    #     # print(n)
    for c in listCon:
        for k, v in c.items():
            # print(item)
            # print(num)
            if str(k) in num:
                print(k)
                file_obj.writelines(v)
    file_obj.close()


if __name__ == "__main__":
    # path = "D:\Test"
    # sname = "common.inc.php"
    # listDbConf(scanFolder_SearchFile(path,sname))

    paths = ['/Users/yuanyinhao/PycharmProjects/liuningning/22.txt']
    file = '2333.txt'
    # print(listNumber(listDbConf(paths)))
    # print(addLine(file))
    print(outputResult(addLine(file),listNumber(listDbConf(paths))))
    # print(get_line_context(paths,5))