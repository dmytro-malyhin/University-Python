import math
import csv
from openpyxl import Workbook

KytLop1 = float(input('Введіть кут лопатей для експеременту №1,alpha:'))  # кут лопатей№1
KytLop2 = float(input('Введіть кут лопатей для експеременту №2,alpha:'))  # кут лопатей№2
KytLop3 = float(input('Введіть кут лопатей для експеременту №3,alpha:'))  # кут лопатей№3
print(
    f"Ви  ввели такі кути:перший експеремент={KytLop1},другий експеремент={KytLop2},третій експеремент={KytLop3}")  # вивід кута лопатей
Oberval1 = float(input('Введіть частоту обертання валу для експеременту №1,n:'))  # частота обертання валу№1
Oberval2 = float(input('Введіть частоту обертання валу для експеременту №2,n:'))  # частота обертання валу№2
Oberval3 = float(input('Введіть частоту обертання валу для експеременту №3,n:'))  # частота обертання валу№3
print(
    f"Ви  ввели такі частоти обертання валу:перша швидкість для експеременту №1,n={Oberval1},друга швидкість для експеременту №2,n={Oberval2},третя швидкість для експеременту №3,n={Oberval3}")  # вивід частоти обертання
PotHhod1 = float(input('Введіть потужність холостого ходу для експеременту №1,Nx:'))  # потужність холостого ходу№1
PotHhod2 = float(input('Введіть потужність холостого ходу для експеременту №2,Nx:'))  # потужність холостого ходу№2
PotHhod3 = float(input('Введіть потужність холостого ходу для експеременту №3,Nx:'))  # потужність холостого ходу№3
print(
    f"Ви  ввели такі потужності холостого ходу:потужність для експеременту №1,Nx={PotHhod1},потужність для експеременту №2,Nx={PotHhod2},потужність для експеременту №3,Nx={PotHhod2}")  # вивід потужності холостого ходу
PotRhod1 = float(input('Введіть потужність робочого ходу для експеременту №1,Npx:'))  # потужність робочого ходу№1
PotRhod2 = float(input('Введіть потужність робочого ходу для експеременту №2,Npx:'))  # потужність робочого ходу№2
PotRhod3 = float(input('Введіть потужність робочого ходу для експеременту №3,Npx:'))  # потужність робочого ходу№3
print(
    f"Ви  ввели такі потужності робочого ходу:потужність для експеременту №1,Nx={PotRhod1},потужність для експеременту №1,Nx={PotRhod2},потужність для експеременту №1,Nx={PotRhod3}")  # вивід потужності робочого ходу
Chaszmish = [30, 90, 180]  # час зумішування,с
Mi = 4  # завантаження
Pv = 1520  # густина матеріалу, кг/
print('Час змішування:', Chaszmish)
Zalnasyti1 = [70, 67, 65]  # залишок на сітці експеремента№1
Zalnasyti2 = [53, 51, 49]  # залишок на сітці експеремента№2
Zalnasyti3 = [75, 65, 56]  # залишок на сітці експеремента№3
C11 = Zalnasyti1[0] / 100
C12 = Zalnasyti1[1] / 100
C13 = Zalnasyti1[2] / 100
print('Концетрація для першого експеременту:', C11, C12, C13)
Kc11 = 100 * (math.sqrt(((C11 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№1
Kc12 = 100 * (math.sqrt(((C12 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№1
Kc13 = 100 * (math.sqrt(((C13 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№1
print("Оцінка якості суміші для експеременту №1:", Kc11)
print("Оцінка якості суміші для експеременту №1:", Kc12)
print("Оцінка якості суміші для експеременту №1:", Kc13)
C21 = Zalnasyti2[0] / 100
C22 = Zalnasyti2[1] / 100
C23 = Zalnasyti2[2] / 100
print('Концетрація для другого експеременту:', C21, C22, C23)
Kc21 = 100 * (math.sqrt(((C21 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№2
Kc22 = 100 * (math.sqrt(((C22 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№2
Kc23 = 100 * (math.sqrt(((C23 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№2
print("Оцінка якості суміші для експеременту №2:", Kc21)
print("Оцінка якості суміші для експеременту №2:", Kc22)
print("Оцінка якості суміші для експеременту №2:", Kc23)
C31 = Zalnasyti3[0] / 100
C32 = Zalnasyti3[1] / 100
C33 = Zalnasyti3[2] / 100
print('Концетрація для третего експеременту:', C31, C32, C33)
Kc31 = 100 * (math.sqrt(((C31 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№3
Kc32 = 100 * (math.sqrt(((C32 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№3
Kc33 = 100 * (math.sqrt(((C33 / 0.5) - 1) ** 2))  # якість механічних коефіцієнтами неоднорідності експеремента№3
print("Оцінка якості суміші для експеременту №3:", Kc31)
print("Оцінка якості суміші для експеременту №3:", Kc32)
print("Оцінка якості суміші для експеременту №3:", Kc33)
PotZm1 = PotRhod1 - PotHhod1  # Фактична потужність змішування для експеременту №1
PotZm2 = PotRhod2 - PotHhod2  # Фактична потужність змішування для експеременту №2
PotZm3 = PotRhod3 - PotHhod3  # Фактична потужність змішування для експеременту №3
print("Фактична потужність змішування для експеременту №1:", PotZm1)
print("Фактична потужність змішування для експеременту №2:", PotZm2)
print("Фактична потужність змішування для експеременту №3:", PotZm3)
Pvi1 = Mi / (Pv * Chaszmish[0])  # продуктивність
Pvi2 = Mi / (Pv * Chaszmish[1])  # продуктивність
Pvi3 = Mi / (Pv * Chaszmish[2])  # продуктивність
print("Продуктивність для експеременту ,перша:", Pvi1, ",друга:", Pvi2, ",третя:", Pvi3)
Npyt1One = (PotZm1 / Pvi1)  # питомі витрати експеремент №1,100000-перенес запятую
Npyt1Two = (PotZm1 / Pvi2)  # питомі витрати експеремент №1,100000-перенес запятую
Npyt1Thr = (PotZm1 / Pvi3)  # питомі витрати експеремент №1,100000-перенес запятую
print("перша питома витрата енергії для експеременту №1:", Npyt1One,
      ",друга питома витрата енергії для експеременту №1:", Npyt1Two,
      ", третя питома витрата енергії для експеременту №1:", Npyt1Thr)
Npyt2One = (PotZm2 / Pvi1)  # питомі витрати експеремент №2,100000-перенес запятую
Npyt2Two = (PotZm2 / Pvi2)  # питомі витрати експеремент №2,100000-перенес запятую
Npyt2Thr = (PotZm2 / Pvi3)  # питомі витрати експеремент №2,100000-перенес запятую
print("перша питома витрата енергії для експеременту №2:", Npyt2One,
      ",друга питома витрата енергії для експеременту №2:", Npyt2Two,
      ", третя питома витрата енергії для експеременту №2:", Npyt2Thr)
Npyt3One = (PotZm3 / Pvi1)  # питомі витрати експеремент №3,
Npyt3Two = (PotZm3 / Pvi2)  # питомі витрати експеремент №3,
Npyt3Thr = (PotZm3 / Pvi3)  # питомі витрати експеремент №3,
print("перша питома витрата енергії для експеременту №3:", Npyt3One,
      ",друга питома витрата енергії для експеременту №3:", Npyt3Two,
      ", третя питома витрата енергії для експеременту №3:", Npyt3Thr)
L = 0.45  # Довжина внутрішньої частини змішувача
n = 0.95  # КПД змішувача
g = 9.8  # швидкість вілного падіння
SpPLZ = (Mi * L * Oberval1 * g) / n
print('Теоретична розрахована потужність на змішування:', SpPLZ)

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Кут нахилу лопатей,Alpha"
sheet["A2"] = KytLop1
sheet["A3"] = KytLop2
sheet["A4"] = KytLop3
sheet["B1"] = "Частота обертання робочого валу"
sheet["B2"] = Oberval1
sheet["B3"] = Oberval2
sheet["B4"] = Oberval3
sheet["C1"] = "Фактична потужність перемішування"
sheet["C2"] = PotZm1
sheet["C3"] = PotZm2
sheet["C4"] = PotZm3
sheet["D1"] = 'Час змішування'
sheet["D2"] = Chaszmish[0]
sheet["D3"] = Chaszmish[1]
sheet["D4"] = Chaszmish[2]
sheet["E1"] = 'Коефіціент неоднорідності Кс для експеременту №1'
sheet["E2"] = Kc11
sheet["E3"] = Kc12
sheet["E4"] = Kc13
sheet["F1"] = 'Коефіціент неоднорідності Кс для експеременту №2'
sheet["F2"] = Kc21
sheet["F3"] = Kc22
sheet["F4"] = Kc23
sheet["G1"] = 'Коефіціент неоднорідності Кс для експеременту №3'
sheet["G2"] = Kc31
sheet["G3"] = Kc32
sheet["G4"] = Kc33
sheet["H1"] = 'Продуктивність'
sheet["H2"] = Pvi1
sheet["H3"] = Pvi2
sheet["H4"] = Pvi3
sheet["I1"] = 'Питома витрата енергії'
sheet["I1"] = 'Питома витрата енергії для експеременту №1'
sheet["I2"] = Npyt1One
sheet["I3"] = Npyt1Two
sheet["I4"] = Npyt1Thr
sheet["J1"] = 'Питома витрата енергії для експеременту №2'
sheet["J2"] = Npyt2One
sheet["J3"] = Npyt2Two
sheet["J4"] = Npyt2Thr
sheet["K1"] = 'Питома витрата енергії для експеременту №3'
sheet["K2"] = Npyt3One
sheet["K3"] = Npyt3Two
sheet["K4"] = Npyt3Thr
workbook.save(filename='D:\\lAB1.xlsx')
