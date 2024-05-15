import pyperclip
import keyboard


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

keyboard.add_hotkey("s+c", cretable)
keyboard.wait("esc")
"""sc"""
