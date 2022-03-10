# in : 멤버연산자  
# 반환 : bool 값
# iterable 자료형에서만 사용

# """"  기본단위  in  iterable  """"

# 1. str
# 문자열에 문자가 있으면 True, 아니면 False
print("s" in "str")

# 2. list
# 리스트에 자료가 있으면 True, 아니면 False
print(1 in [10,2,3,4])

# 3. tuple
# 튜플에 자료가 있으면 True, 아니면 False
print(2 in (2,3,4))

# 4. set
# 세트에 자료가 있으면 True, 아니면 False
print(4 in {"a","b"})

# 5. dict
# 딕셔너리에 키가 있으면 True, 아니면 False
print(1 in {1:"one", 2:"two"})


