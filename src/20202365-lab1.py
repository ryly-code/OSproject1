def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("성적 grade 확인")
score=int(input("성적을 입력하시오: "))
print("학점 = ", grade(score))

print("-------------------------------------------------------")

def check_bmi(height,weight):

    bmi=weight/(height/100)**2

    if bmi >= 40:
        return bmi, "고도비만입니다."
    elif bmi >= 30:
        return bmi, "비만입니다."
    elif bmi >= 25:
        return bmi, "경도 비만입니다."
    elif bmi >= 20:
        return bmi, "정상 체중입니다."
    else:
        return bmi, "저체중입니다."

print("BMI를 이용하여 건강진단하기")

height=int(input("키가 몇 cm인가요? "))
weight=int(input("몸무게가 몇 kg인가요? "))

bmi, message = check_bmi(height,weight)
print("당신의 BMI(체질량지수) = %0.2f, %s" %(bmi,message)) 
