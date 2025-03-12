print('Hello Mars')

try:
    with open('mission_computer_main.log', 'r') as file:
        log_file = file.readlines()
except:
    print('Error in reading file.')
else:
    log = [i.strip() for i in log_file[1:]]
    log.sort(key = lambda k: k.strip().split(',')[0], reverse = True)

    print(log_file[0].strip())
    for i in log:
        print(i)

    log_from = int(input('사고의 원인 시작: '))
    log_to = int(input('사고의 원인 끝: '))
    
    with open('log_analysis.md', 'w') as md_file:
        md_file.write(f'{log_file[0]}')
        for i in log[log_from - 1:log_to]:
            md_file.write(f'{i}\n')
