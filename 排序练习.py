jobs = []
while True:
    prom = input('请输入任何名称/do: ')
    if prom == 'do':
        if jobs:
            print('请完成任务:' + jobs.pop(0))
        else:
            print('任务已经完成了，可以放心下班了。')
            break
    else:
        jobs.append(prom)