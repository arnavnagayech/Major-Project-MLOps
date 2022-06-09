import joblib
mind = joblib.load('marks.pk1')

print(mind.predict([[2]]))