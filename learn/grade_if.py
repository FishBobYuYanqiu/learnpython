score=input("Enter score:")
score=float(score)
if score<0 or score>1:
	print("score has to be between 0 and 1")
	quit()
elif score>=0.9:
	grade="A"
elif score>=0.8:
	grade="B"
elif score>=0.7:
	grade="C"
elif score >=0.6:
	grade="D"
else:
	grade="F"
print(grade)