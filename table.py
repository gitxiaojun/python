usres ={
    1:{ 'name':'lurenjia', 'age': 20, 'tel': '195xxxxxxx'},
    2:{'name': 'wang', 'age': 30, 'tel':'156xxxxxxx'},
    3:{'name': 'zhangsan','age':25,'tel': '180xxxxxxx'}
}
tmp_user = []
tp_title = '|{0:^10s}|{1:^10s}|{2:^15s}|{3:^15s}|'
col_title = ('ID', 'Name', 'Age', 'Tel')
tpl_body = '|{0:^10d}|{1:^10s}|{2:^15d}|{3:^15s}|'
title = tp_title.format(col_title[0], col_title[1], col_title[2], col_title[3])
splitline = '-' * len(title)
while True:
    op = input('请输入操作(add/list/edit/del/find)')
    if op == 'list':
        print(splitline)
        print(title)
        print(splitline)
        for i in list(usres.items()):
            print(tpl_body.format(i[0],i[1]['name'],i[1]['age'],i[1]['tel']))
        if len(tmp_user) != 0:
            for i in tmp_user:
                print(tpl_body.format(i[0], i[1], i[2], i[3]))
    elif op == 'add':
        txt = input('请输入用户信息:(name,age,tel)')
        nodes = txt.split(',')
        if len(nodes) != 3:
            print('输入信息错误，请重新输入！')
        else:
            uid = 0
            for user in list(usres.items()):
                if uid < user[0]:
                    uid = user[0]
            nodes[1] = int(nodes[1])
            tmp_user.append((uid + 1,) + tuple(nodes))
            print('用户添加成功')
    elif op == 'edit':
        