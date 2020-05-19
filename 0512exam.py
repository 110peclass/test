#攝氏溫度轉換器。fahrenheit212→clesius100
def convert_celsius():
    celsius_d = (fahrenheit_d - 32) * 5/9 #攝氏=(華氏-32) x 5/9
    print(celsius_d)
fahrenheit_d = eval(input('enter the num of celsius degree:'))
convert_celsius()

#正五邊形面積計算器，輸入r為中心到頂點的距離，
import math  #匯入數學模組，後面可以使用三角函數sin，以及運用數值π(這裡是指角度的π=180度)
def area_pentagon(r):
#定義函式 並定義輸入的變數是 r ，所以在使用函式的時候可以先指定 r = (數值) 然後再呼叫函式。也可以直接在括號內寫數字。
    s = 2 * r * math.sin(math.pi/5)  #正五邊形的邊長公式，不用鑽數學公式，直接轉用就好。
    area_pentagon = 5 * s ** 2 / (4 * math.tan(math.pi/5)) #正五邊形的邊心面積公式，一樣不用理他直接轉用。
    return area_pentagon  #呼叫面積結果這個值
r = eval(input('enter num of r:'))  #指定變數r的值 → (請輸入數字)
ans = 'the area of pentagon is: %0.2f' % area_pentagon(r)
#指定變數ans的值 → 字串(the area of pentagon is: 格式化顯示小數點2位) 格式化的值為代入 area_pentagon(r)的結果
print(ans)

# 飛機最短距離
def length(a, v):  #定義函式以及函式的輸入變數是 a 和 v
    length_flight = v **2 / (2 * a) #指定length_flight的值 → 那個速度公式
    return length_flight  #呼叫 length_flight 運算結果
a, v = eval(input('enter a & v :'))  #指定a 和 v的數值
ans = 'the length of flight are : %0.2f meters' % length(a,v)
print(ans)

#熱水加熱所需熱量
def energy_water(m_kg,ini_d,fin_d):
#定義函式 以及函式的變數有3個 我把它們取名為 m_kg(水的重量) ini_d(起始溫度)  fin_d(最後溫度)
    energy_q = m_kg * (fin_d - ini_d) * 4184  #帶入數學公式
    return energy_q
m_kg, ini_d, fin_d = eval(input('enter m_kg & ini_d & fin_d:'))  #一次輸入3個值
ans = 'the energy needed is : %0.2f' % energy_water(m_kg,ini_d,fin_d)
print(ans)

#計算圓柱體底面積與體積
import  math
def cylinder_area_volume(cylinder_r,cylinder_h):  #定義公式 以及2個變數
    area_cylinder = math.pi * cylinder_r ** 2  #帶入數學公式 這邊的math.pi 是圓周率， ** +數字 → 幾次方的意思
    volume_cylinder = area_cylinder * cylinder_h
    return area_cylinder , volume_cylinder  #可以呼叫不只1個的值 所以這個函式的結果 會產生2個值
cylinder_r, cylinder_h = eval(input('enter radius,height:'))  #使用函式前 輸入數值 給 指定的變數
ans = 'the area = %0.2f ,the volume = %0.2f' % (cylinder_area_volume(cylinder_r,cylinder_h))
print(ans)  #可以不用多設定ans 這個變數， 直接print上面那一串 ，只是覺得程式太長 給個變數 比較好找@@


# 一元二次方程式解
import math
def x_equation(a,b,c):
    x_j = math.sqrt(b ** 2 - 4 * a *c)  #math.sqrt = square root  算出平方根的意思
    #這個x_j變數  我的想法是 先用 一元二次方程式的 判斷式  先看看是 有2解 ,相同1個解, 還是無解
    x1 = (-b - x_j) / (2 * a)  #帶入公式 求其中一個解
    x2 = (-b + x_j) / (2 * a)  #求另一個解
    if x_j == 0:  #這邊先用if  如果判斷式 = 0   (雙等號是 數學運算的 等於 的意思)
        print('only one answer = %0.6f' % x1)  #有1個相同解  隨便抓一個 x1 或 x2 的答案輸出就好
    elif x_j < 0:  #再來用 elif  補充如果上面那個不成立 就是不等於1的話 再來看看 是不是小於0
        print('no solution')
    else:  #最後 用 else 如果上面所有的情況 都不是  那就輸出下面的東西  (也是可以繼續用elif 寫成 elif x_j > 0:)
        print('two answer = %0.6f , %0.6f' % (x1, x2))
a ,b , c = eval(input('enter a,b,c:'))
print(x_equation(a,b,c))


# 給定做標判斷是否在圓內、圓外、圓上
import math
def coordinates_circle_distence(x,y):  #定義函式 以及2個變數 x , y
    distence = math.sqrt(x ** 2 + y ** 2)  #座標距離公式 這裡是算 (x,y)到原點(0,0)的距離
    if distence > 8:  #用if 先判斷 如果距離大於8  就輸出下面那段
        print('(%d , %d)此點在圓外' % (x , y))
    elif distence < 8:  #再來用 elif 來判斷  如果距離小於8 就輸出下面那段
        print('(%d , %d)此點在圓內' % (x , y))
    else:  #最後用 else 來判斷  如果不是上面 大於8 和小於8的情況 就輸出下面那段  (一樣可以用elif 來寫)
        print('(%d , %d)此點在圓上' % (x , y))
x , y = eval(input('enter the coordinates (x , y) :'))
print(coordinates_circle_distence(x,y))


# 判斷亂數是否為3或5的倍數
import random  #匯入亂數模組
def random_divided_three_or_five(random_num):  #定義函式 以及1個變數
    divided_three = random_num % 3  #這邊先指定變數divided_three → 是運算random_num  除以3之後的"餘數"是多少
    divided_five = random_num % 5  #指定divided_five 的值 → 亂數除以5之後 的餘數是多少
    if divided_three != 0 and divided_five != 0 :  #先用if判斷  如果 除以3的餘數 且 除以5的餘數 "不等於0"的時候
        print('%d 不是3或5的倍數' % random_num)
    elif divided_three == 0 and divided_five == 0:  #再來用elif判斷 如果 除以3 且 除以5 的餘數"等於0"的時候
        print('%d 是3與5的倍數' % random_num)
    elif divided_three == 0:  #然後用 elif判斷  除以3 的 餘數等於0 的時候
        print('%d 是3的倍數' % random_num)
    elif divided_five == 0:  #一樣判斷 除以5的餘數情況
        print('%d 是5的倍數' % random_num)
# 這邊要補充說明 if的判斷是由上依序往下 所以後面3,5這兩個判斷式 不能在第2個判斷式的前面
random_num = random.randint(1,101)  #亂數輸出的範圍是(起始值,終止值-1)
print(random_divided_three_or_five(random_num))


# 十六進位轉十進位
def convert_hex_to_dec(num_hex):  #定義函式，以及1個變數num_hex → 這個是取名來表示要輸入的十六進位
    num_dec = int(num_hex, base = 16)  #int(要被轉換的數值 , base = 這個數值是幾進位)
    return  num_dec
num_hex = str.upper(input('enter hexodecimal number:'))
#這邊的str.upper是自動調整輸入的值 全部大寫  因為十六進位的ABCDEFG表示法要用大寫英文字
print(convert_hex_to_dec(num_hex))


# 輸入一整數，判斷是否能被5或8整除(被5與8整除)
def divided_five_and_eight(num_int):
    if num_int % 5 ==0 and num_int % 8 == 0:
        print('%d 能被5與8整除' % num_int)
    elif num_int % 5 == 0 or num_int % 8 ==0:
        print('%d 能被5或8整除' % num_int)
    else:
        print('%d 不能被5或8整除' % num_int)
num_int = eval(input('enter number:'))
print(divided_five_and_eight(num_int))