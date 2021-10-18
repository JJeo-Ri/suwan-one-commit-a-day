def solution(record):
    names = dict()
    for r in record:
        commands = r.split(" ")
        if len(commands) == 3:
            uid = commands[1]
            name = commands[2]
            names[uid] = name
    result = []
    for r in record:
        commands = r.split(" ")
        if commands[0] == 'Enter':
            result.append(f"{names[commands[1]]}님이 들어왔습니다.")
        elif commands[0] == 'Leave':
            result.append(f"{names[commands[1]]}님이 나갔습니다.")
    return result
