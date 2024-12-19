MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,  # 필요한 물 양 (ml)
            "coffee": 18,  # 필요한 커피 양 (g)
        },
        "cost": 1.5,  # 가격 ($)
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,  # 필요한 우유 양 (ml)
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# 수익 초기화
profit = 0

# 머신의 현재 재료 상태
resources = {
    "water": 300,  # 물의 초기 양 (ml)
    "milk": 200,  # 우유의 초기 양 (ml)
    "coffee": 100,  # 커피의 초기 양 (g)
}