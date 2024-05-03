#          PYTHON BASIC DATA TYPE
'''
+ Str (String): Kiểu chuỗi hay gọi là kiểu ký tự chữ
+ Int (integer): Kiểu số nguyên, số nguyên dương hoặc âm chứ không phải thập phân hay số phẩy
+ Bool (Boolean): Kiểu true/false, đúng sai
'''

# GIẢI QUYẾT BÀI TOÁN VẤN ĐỀ
"""Dữ liệu đầu vào thí sinh"""
print("============= Bài toán \"Đặt vấn đề\" [START] ===========")
name = "Nam"
year = 2007
mark = 10

if(mark < 5):
    print("Trượt rồi thím, đóng 600 học lại")
if(mark > 5): 
    print("Quá đỉnh, quá xuất sắc, xuất sắc cái con khỉ, bạn đã đỗ")

print("============= Bài toán \"Đặt vấn đề\" [END] =============")


# KIỂM TRA DATA TYPE CỦA 1 BIẾN
"""Sử dụng lệnh: type"""
print(type(name))
"""Trong đó biến \"name\" là 1 kiểu chuỗi ===> Output: str (string/chuỗi)"""

# GÁN NHIỀU BIẾN VÀO MỘT GIÁ TRỊ
a = b = c = 10
print("a = ", a)
print("b = ", b)
print("c = ", c)

# GÁN LIÊN TIẾP GIÁ TRỊ VÀO CÁC BIẾN
d, e, f = 99, True, "HALLO"
print("d = ", d)
print("e = ", e)
print("f = ", f)

# TOP CÁC TỪ KHÓA KHÔNG ĐƯỢC ĐẶT THEO HÀM
'''
AND - AS - BREAK - CLASS - CONTINUE - DEF - ELIF - ELSE - IF - FALSE - FOR - GLOBAL - IMPORT - IN - IS - NOT - OR - RETURN - TRUE - TRY - WHILE
'''
