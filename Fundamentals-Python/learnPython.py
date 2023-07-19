condition1 = True
condition2 = False

not condition1  # False
condition1 and condition2  # False
condition1 or condition2  # True

0 or 1  # 1
False or "hey"  # 'hey'
'hi' or 'hey'  # 'hi'
[] or False  # False
False or []  # []

0 and 1  # 0
1 and 0  # 0
False and "hey"  # False
'hi' and 'hey'  # 'hey'
[] and False  # []
False and []  # False
