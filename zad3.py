
A = {"a": 1, "b": 2, "c": 3, "d": 4, "f": "hello", "g": "app"}
B = {"b": 3, "d": 5, "e": 7, "m": 9, "g": "le", "k": "world"}

C = {}

for key in A:
    if key in B:
        if isinstance(A[key], int) and isinstance(B[key], int):
            C[key] = A[key] + B[key]
        else:
            C[key] = str(A[key]) + str(B[key])
    else:
        C[key] = A[key]

for key in B:
    if key not in A:
        C[key] = B[key]

print(C)
#Nie wiem czy to jest obliagatoryjne ale mozesz to jeszcze przysorotwac zeby bylo alfabetycznie. 
sorted_result = {k: C[k] for k in sorted(C)}
print(sorted_result)

