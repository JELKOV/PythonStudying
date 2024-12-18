capitals = {
    "France": "paris",
    "Korea": "seoul",
}

# 중첩 딕셔너리

# travel_log = {
#     "France": ["paris", "lille", "dijon"],
#     "Korea": ["seoul", "busan", "gangwon"]
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# 테스트
# travel_log = {
#     "France": {
#         "num_timed_visited": 8,
#         "cities_visitied": ["paris", "lille", "dijon"]
#     },
#     "Korea": ["seoul", "busan", "gangwon"]
# }


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

print(travel_log["Germany"]["cities_visited"][2])