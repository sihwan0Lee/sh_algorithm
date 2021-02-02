# Hash Table
# key 에 데이터(value)를 저장하는 데이터 구조
# 파이썬은 딕셔너리 타입을 사용하면 되므로 별도로 해쉬를 구현 안해도됌.

# 용어정리
# 해쉬(Hash): 임의 값을 고정 길이로 변환하는것
# 해쉬테이블 : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
# 해싱 함수 : key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
# 해쉬 값 : key를 해상 함수로 연산해서 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 key에 대한 데이터의 위치를 일관성 있게 찾을 수 있음
# 슬롯 : 한 개의 데이터를 저장할 수 있는 공간
# 저장할 데이터에 대해 key를 추출할수 있는 별도 함수도 존재할 수 있음.

# 장점
# 데이터 저장/읽기 속도가 빠르다(검색 속도가 빠르다)
# 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉽다

# 단점
# 일반적으로 저장 공간이 좀더 많이 필요하다
# 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요하다

# 주요 용도: 검색이 많이 필요한 경우 // 저장, 삭제, 읽기가 빈번한 경우


hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_func(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_func(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_func(get_key(data))
    return hash_table[hash_address]


save_data('dave', '01020202020')
save_data('andy', '01030303030')
print(read_data('dave'))
print(hash_table)
