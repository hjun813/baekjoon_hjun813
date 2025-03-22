class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # 고정된 크기의 배열

    def hash_function(self, key):
        return hash(key) % self.size  # 해시 함수 (간단한 모듈로 연산)

    def insert(self, key, value):
        index = self.hash_function(key)  # 키를 해싱하여 인덱스 계산
        self.table[index] = value  # 해당 위치에 값 저장

    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]  # 해당 위치에서 값 반환

    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")

# 사용 예제
ht = HashTable()
ht.insert("apple", 10)
ht.insert("banana", 20)
print(ht.search("apple"))  # 10 출력
print(ht.search("banana"))  # 20 출력
ht.display()


#연결 리스트

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)