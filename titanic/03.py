# numpy

import numpy as np

# notes from students

notes = np.array([10,5,6,3,1,7])

print('Media: ',np.mean(notes))
print('Sum: ',np.sum(notes))
print('Standard Deviation: ',np.std(notes, ddof=1))

# another notes at school

notes2 = np.array([
    [2, 8, 7],
    [7, 9, 6],
    [10, 1, 5]
])

media_student = np.mean(notes2, axis=1)
print(f'Media for student: {np.round(media_student, 2)}')


deviation_student = np.std(notes2, axis=1)
print(f'Standard Deviation for student: {np.round(deviation_student, 2)}')


media_discipline = np.mean(notes2, axis=0)
print(f'Media for Discipline: {np.round(media_discipline, 2)}')

deviation_discipline = np.std(notes2, axis=0)
print(f'Standard Deviation for discipline: {np.round(deviation_discipline, 2)}')

# # calculate products

prices = []
N = 60 * 60 * 24 * 365
for i in range(N):
    prices.append(100 + i/100)

print(prices[:5])

avg = 0.0
for p in prices:
    avg += p/len(prices)

print(avg)
