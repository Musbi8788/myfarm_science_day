def get_grade_score(score):
    if score > 100:
        return 'Extra Credit'
    
    if score < 0 :
        return 'Invalid Grade'
    
    if  90 <= score <= 100:
        return 'A'
    
    elif 80 <= score <= 89:
        return 'B'
    
    elif 70 <= score <= 79:
        return 'C'
    
    elif 60 <= score <= 69:
        return 'D'
    
    else:
        return 'F'


# Test Results
print(get_grade_score(95)) # A
print(get_grade_score(88)) # B
print(get_grade_score(188)) # Extra Credit
print(get_grade_score(75)) # C
print(get_grade_score(65)) # D
print(get_grade_score(50)) # F
print(get_grade_score(-8)) # Invalid