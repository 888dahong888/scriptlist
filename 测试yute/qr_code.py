import segno
employees=[
    "刘备",
    "关羽",
    "张飞",
    "赵云",
]
with open("employees.txt","w") as f:
    for emp in employees:
        f.write(f"{emp}\n")
        qr=segno.make(emp,encoding="utf8",micro=False)
        qr.save(f"{emp}.png",scale=10)
     