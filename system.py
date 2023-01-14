import os
def main():
    while True:
        menm()
        choice = int(input("请选择您需要的功能:"))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("您确定退出系统码？y/n:")
                if answer == 'y ' or  'Y':
                    print("感谢您的使用！")
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def menm():
    print("--------------------学生信息管理系统-----------------")
    print("------------------------功能菜单---------------------")
    print("\t\t\t1.录入学生信息")
    print("\t\t\t2.查找学生信息")
    print("\t\t\t3.删除学生信息")
    print("\t\t\t4.修改学生信息")
    print("\t\t\t5.排序")
    print("\t\t\t6.统计学生总人数")
    print("\t\t\t7.显示所有学生信息")
    print("\t\t\t0.退出")
    print("----------------------------------------------------")

def insert():
    while True:
        student_list = []
        id = int(input("请输入学生ID(如1001)："))
        if not id :
            break
        name = input("请输入学生姓名：")
        if not name:
            break
        try:
            English = int(input("请输入英语成绩："))
            Python = int(input("请输入Python成绩："))
            Math = int(input("请输入数学成绩："))
        except:
            print("您输入的成绩有误，请输入整数^-^:")
            continue
        student = {"ID": id, "姓名": name, "English": English, "Python": Python, "Math": Math}
        # 保存文件
        student_list.append(student)
        save(student_list)
        answer = input("是否继续添加？y/n:")
        if answer == "y" or answer == "Y":
            continue
        else:
            break

    print("学生成绩录入完毕！")

def save(lis):

    with open(filename, "a", encoding="utf-8") as f:
        for item in lis:
            f.write(str(item) + '\n')

def search():

    while True:
        student_query = []
        if os.path.exists(filename):
            model = input("按ID查询请输入1，按姓名查询请输入2：")
            if model == "1":
                id = int(input("请输入ID信息："))
            elif model == "2":
                name = input("请输入姓名：")
            else:
                print("您输入的有误，请重新输入")
                search()
            with open(filename, "r", encoding='utf-8') as f:
                student_info = f.readlines()
                for item in student_info:
                    exist_id = False
                    exist_name = False
                    student = dict(eval(item))
                    if model =="1" :
                        if student["ID"] == id:
                            exist_id = True
                            exist_name = True
                            student_query.append(student)
                            break
                        else:
                            continue

                    elif model == "2":
                        if student["姓名"] == name:
                            exist_name = True
                            exist_id = True
                            student_query.append(student)
                            break

                if  not exist_id:
                    answer = input("您查找的ID不存在,是否即需查找?y/n:")
                    if answer == "y" or answer == "Y":
                        search()
                    else:
                        return
                if  not exist_name:
                    answer = input("您查找的姓名不存在,是否即需查找?y/n:")
                    if answer == "y" or answer == "Y":
                        search()
                    else:
                        return

                #展示查询内容
                show_student(student_query)
                answer = input("您是否继续查找?y/n：")
                if answer == 'y' or answer == "Y":
                    continue
                else:
                    return

def show_student(lis):
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_title.format("ID","姓名","Eenlish","Python","Math","总分"))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    for item in lis:
        print(format_data.format(item.get("ID"),
                                item.get("姓名"),
                                item.get("English"),
                                item.get("Python"),
                                item.get("Math"),
                                int(item.get("English"))+int(item.get("Python"))+int(item.get("Math"))))

def delete():
    while True:
        student_id = int(input("请输入要删除的学生ID："))
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    student_old = f.readlines()
            else:
                student_old = []
            flag = False #标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as f:
                    d ={}
                    for item in student_old:
                        d = dict(eval(item)) #将字符串传话为字典
                        if d["ID"] != student_id:
                            f.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生')
            else:
                print("无学生信息")
                break
            show()
            answer = input("是否继续删除？y/n\n")
            if answer =='y' or answer == 'Y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r' ,encoding='utf-8') as f :
            student_old = f.readlines() #list
    else:
        return
    student_new = []
    for item in student_old:
        item = dict(eval(item))
        student_new.append(item)
    with open(filename, 'w', encoding='utf-8') as f:
        while True:
            student_id = int(input("请选择您要修改的ID信息："))
            id_exist = False
            for student_info in student_new:
                if student_info["ID"] == student_id:
                    id_exist = True
                    while True:
                        modify_info = str(input("请选择您要修改的信息："))
                        if modify_info == "姓名":
                            modify_content = input("请输入您要修改的内容：")
                            student_info[modify_info] = modify_content
                        elif modify_info in student_info:
                            modify_content = int(input("请输入您要修改的内容："))
                            student_info[modify_info] = modify_content
                        else:
                            print("您选的修改信息不存在！")
                            continue
                        answer = input("您要继续修改该学生信息吗？y/n")
                        if answer == 'y' or answer == 'Y':
                            continue
                        else:
                            break
            if not id_exist:
                print("您输入的ID不存在！")
            answer = input("您要继续修改信息吗？y/n")
            if answer == "y" or answer == "Y":
                continue
            else:
                print("修改完毕")
                break
        for item in student_new:
            f.write(str(item) + '\n')

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            student_info = []
            student = f.readlines()
            for item in student:
                student_info.append(dict(eval(item)))
        if student_info:
            asc_sort_dce = input("请选择(升序/1，降序/2)：")
            if asc_sort_dce =="1":
                asc_sort_bool = False
            elif asc_sort_dce == "2":
                asc_sort_bool = True
            else:
                print("您输入的有误，请重新输入！")
                sort()
        else:
            print("暂无录入学生信息！")
            return
        model = input("请您选择排序方式(1.按English成绩排序 2.按Python成绩排序 3.按Math成绩排序 0.按总成绩排序 ：")
        if model =="1":
            student_info.sort(key=lambda student: int(student['English']), reverse=asc_sort_bool)
        elif model == "2":
            student_info.sort(key=lambda student: int(student['Python']), reverse=asc_sort_bool)
        elif model == "3":
            student_info.sort(key=lambda student: int(student['Math']), reverse=asc_sort_bool)
        elif model == "0":
            student_info.sort(key=lambda student: int(student['English']+int(student['Python'])+int(student['Math']), reverse=asc_sort_bool))
        else:
            print("您输入的有误，请重新输入！")
            sort()
        show_student(student_info)
    else:
        print("暂无学生信息！")
        return
def total():
    if os.path.exists(filename):
        with open(filename, "r", encoding='utf-8') as f:
            student = f.readlines()
            if student:
                print(f"一共有{len(student)}学生")
            else:
                print("还没有录入学生信息")
    else:
        print("暂未保存数据信息")

def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, "r", encoding='utf-8') as f:
            student = f.readlines()
            for item in student:
                student = dict(eval(item))
                student_list.append(student)
            if student_list:
                show_student(student_list)
            else:
                print("暂无录入学生信息！")
    else:
        print("暂无学生信息！")

if __name__ == '__main__':
    filename = "Student"
    main()
