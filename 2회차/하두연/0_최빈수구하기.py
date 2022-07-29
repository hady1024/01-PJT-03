import sys

sys.stdin = open("_최빈수구하기.txt")


T = int(input())   # 첫번째 줄에 테스트케이스 T가 주어짐

for _ in range(T):
    tc = int(input())        # 테스트 케이스에 번호 입력
    score = list(map(int, input().split()))
    data = []                                    # 리스트 저장소

    for i in score:
        data[i] += 1                                # data 리스트에 score 값을 하나씩 확인하여 1씩 증가

    test = max(data)                                # 점수 최빈값 구하기? 예전 실습에서 영어단어 문제에서 알파벳 사용빈도 찾을때 max 썻던 기억이나서 써봄, 
                                                    # 문제에서도 최빈값이 여러개일 경우 가장큰 값 사용이라 나와있음

    count = []                                      # 최빈값 데이터 저장소

    for i in range(len(data)):                      # 저장된 리스트값 확인
        if data[i] == test:                         # 최대값이 리스트 값이랑 같은가?? 음 .. 일단 맞으면 count에 저장
            count.append(i)
    
    print('#%x %x' % (tc, count)) 
