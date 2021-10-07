def solution(numbers):
    numbers = list(map(str, numbers))
    print('33' > '3030')
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))
