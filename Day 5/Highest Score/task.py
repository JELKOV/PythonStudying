# 학생 점수 리스트
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# range 객체를 생성하고 출력 (1부터 9까지)
print(range(1, 10))

# 학생 점수 총합 계산 (내장 함수 sum 사용)
total_exam_score = sum(student_scores)

# 학생 점수 총합 계산 (반복문 사용)
sum = 0
for score in student_scores:
    sum += score

print(sum)

# 학생 점수 중 가장 높은 점수 (내장 함수 max 사용)
max_score = max(student_scores)
print(max_score)

# 학생 점수 중 가장 높은 점수 (반복문 사용)
value = student_scores[0]
for score in student_scores:
    if score > value:
        value = score
