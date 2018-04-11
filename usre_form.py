#用户信息表
#功能：增、删除、改、查、查询名字
usres = []
usres.append((1, 'lurenjia', 20, '195xxxxxxx'))
usres.append((2, 'lisi', 30, '189xxxxxxx'))
usres.append((3, 'zhangsan',25, '180xxxxxxx'))
tp_title = '|{0:^10s}|{1:^10s}|{2:^15s}|{3:^10s}|'
col_title = ('ID', 'Name', 'Age', 'Tel')
tpl_body = '|{0:^10d}|{1:^10s}|{2:^15d}|{3:^10s}|'
title = tp_title.format(col_title[0], col_title[1], col_title[2], col_title[3])
# ss = usres.append(input('请输入用户名、年龄、手机号: '))
splitline = '-' * len(title)


while True:
    op = input('请输入操作(add/list/edit/del/find)')
    if op == 'list':
        print(splitline)
        print(title)
        print(splitline)
        for i in usres:
            print(tpl_body.format(i[0], i[1], i[2], i[3]))
    elif op == 'add':
        txt = input('请输入用户信息:(name,age,tel)')
        nodes = txt.split(',')
        if len(nodes) != 3:
            print('输入信息错误，请重新输入！')
        else:
            uid = 0
            for user in usres:
                if uid < user[0]:
                    uid = user[0]
            nodes[1] = int(nodes[1])
            usres.append((uid + 1,) + tuple(nodes))
            print('用户添加成功')
    elif op == 'find':
        name = input('请输入用户信息:')
        print(splitline)
        print(title)
        print(splitline)
        for u in usres:
            if u[1] == name:
                print(tpl_body.format(i[0], i[1], i[2], i[3]))
        print(splitline)
    elif op == 'del':
        uid = input("请输入删除用户ID:")
        uid = int(uid)
        for u in usres:
            if uid == u[0]:
                usres.remove(u)
                print('删除成功')
                break
    elif op == 'edit':
        uid = input('请输入用户ID:')
        uid = int(uid)
        exi = False
        exi_usre = None
        for u in usres:
            if uid == u[0]:
                exi_usre = u
                break
        if exi_usre:
            txt = input('请输入用户信息:(name,age,tel)')
            nodes = txt.split(',')
            if len(nodes) != 3:
                print('输入信息错误，请重新输入！')
            else:
                usres.remove(exi_usre)
                nodes[1] = int(nodes[1])
                usres.append((uid,) + tuple(nodes))
                print('修改成功')
        else:
            print('用户信息不存在')