# 간단한 딕셔너리 정의
capitals = {
    "France": "paris",
    "Korea": "seoul",
}

# 중첩 딕셔너리 예시
# travel_log = {
#     "France": ["paris", "lille", "dijon"],
#     "Korea": ["seoul", "busan", "gangwon"]
# }
# print(travel_log["France"][1])

# 중첩 리스트 예시
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])  # 중첩 리스트에서 특정 값 출력

# 중첩 딕셔너리 정의 및 사용
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

# 중첩 딕셔너리에서 특정 값 출력
print(travel_log["Germany"]["cities_visited"][2])