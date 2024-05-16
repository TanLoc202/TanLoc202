import pyperclip
import keyboard
import random

tinh_list = [
    "TP Hồ Chí Minh",
    "Bà Rịa Vũng Tàu",
    "Bình Dương",
    "Bình Phước",
    "Đồng Nai",
    "Tây Ninh",
    "An Giang",
    "Bạc Liêu",
    "Bến Tre",
    "Cà Mau",
    "Cần Thơ",
    "Đồng Tháp",
    "Hậu Giang",
    "Kiên Giang",
    "Long An",
    "Sóc Trăng",
    "Tiền Giang",
    "Trà Vinh",
    "Vĩnh Long"
]

names = [
    "Nguyễn Minh Đăng",
    "Huỳnh Phúc Đạt",
    "Phạm Quyển Đình",
    "Nguyễn Minh Đức",
    "Trần Thái Hưng",
    "Phan Vĩ Khang",
    "Trần Thị Mỹ Khánh",
    "Huỳnh Tấn Lộc",
    "Tăng Xuân Lộc",
    "Nguyễn Huỳnh Nhiên",
    "Nguyễn Nhựt Ninh",
    "Trương Sơn Sô Phát",
    "Lê Thị Hiếu Thảo",
    "Nguyễn Trọng Tín",
    "Nguyễn Xuân Vinh",
    "Nguyễn Thị Mỹ Yến",
    "Từ Quốc Cảnh",
    "Thạch Lâm Oanh Đi",
    "Nguyễn Thái Điền",
    "Nguyễn Trần Hoàng Hiếu",
    "La Diễn Kha",
    "Nguyễn Quốc Huy Khanh",
    "Nguyễn Tuấn Kiệt",
    "Lâm Chí Nhân",
    "Trần Thị Quỳnh Như",
    "Nguyễn Hoàng Phúc",
    "Thân Anh Tài",
    "Phạm Kim Thọ",
    "Lê Dương Nhựt Thoại",
    "Trần Ngô Quốc Thuận"
]

def get_name():
    name = random.choice(names)
    names.remove(name)
    return name

phone_ramdom = lambda: "0" + "".join(str(random.randint(0, 9)) for _ in range(9))
address_ramdom = lambda: random.choice(tinh_list)
date_ramdom = lambda: f"{random.randint(1, 12)}/{random.randint(1, 30)}/{random.randint(1990, 2010)}"

def tti(text):
    ls = text.split(".")
    key = {
        "dt" : "DATETIME",
        "nv" : "NVARCHAR",
        "v"  : "VARCHAR",
        "c"  : "CHAR",
        "f"  : "FLOAT",
        "i"  : "INT",
        "X"  : "x",
    }
    key2 = {
        "pk" : "PRIMARY KEY",
        "nn" : "NOT NULL",
        "id" : "IDENTITY(1, 1)" 
    }
    if len(ls) >= 3:
        sl = f"({ls[2]})"
    else:
        sl = ""
    if len(ls) > 3:
        pk = " " + " ".join(key2[l] for l in ls[3:])
    else:
        pk = ""
    return f"{ls[0]} {key[ls[1]]}{sl}{pk}"

def cretable():
    content = pyperclip.paste().split("/")
    if len(content) > 3 and content[0] == "ctb":
        tenbang = content[1]
        thuoctinh = content[2].split(",")
        if len(content) == 4: 
            khoangoai = [i.split(".") for i in content[3].split(",")]
        else: 
            khoangoai = []
        sql = \
        f"""CREATE TABLE {tenbang} (
            {", ".join(tti(i) for i in thuoctinh)}{"".join(f", CONSTRAINT FK_{tenbang}{fk[0]} FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[0]})" for fk in khoangoai)}
        );"""
        pyperclip.copy(sql)
        print(sql)

def insertinto():
    content = pyperclip.paste().split("/") 
    if len(content) == 5 and content[0] == "ci":
        soluong = int(content[1])
        bang = content[2]
        thuoctinh = content[3]
        dulieu = content[4]
        
        sqls = ""
        for i in range(1, soluong + 1):
            sql = f"INSERT INTO {bang} ({thuoctinh}) VALUES ({dulieu});"
            sql = sql.replace("#i#", str(i))
            sql = sql.replace("#ten#", get_name())
            sql = sql.replace("#sdt#", phone_ramdom())
            sql = sql.replace("#diachi#", address_ramdom())
            sql = sql.replace("#ngay#", date_ramdom())

            sqls += "\n" + sql
        pyperclip.copy(sqls)
        print(sqls)

keyboard.add_hotkey("s+c", cretable)
keyboard.add_hotkey("s+i", insertinto)
keyboard.wait("esc")

'''
ctb/SinhVien/MSSV.nv.5,TenSV.nv.30,MaLop.nv.5/Malop.Lop
ci/10/sinhvien/mssv, tensv, malop/'st0#i#', '#ten#', '#sdt#', '#diachi#', '#ngay#'


'''