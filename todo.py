Найти текст какой-то речи 
Цель провести анализ речи
Искать в инете как делать анализ речи, тут может быть признаки (словарный запас, слова паразиты, и другое)
https://muzei-moskvy.ru/analiz-reci-ponyatie-i-metody/#:~:text=Анализ%20речи%20–%20это%20процесс,медицину%20и%20даже%20судебные%20процессы
Анализ устной речи
     https://dzen.ru/a/Wz0emrRjlgCqyDhF
Что такое психолингвистический анализ речи?
https://blog.studylie.ru/psiholingvisticheskij-analiz-rechi/
https://spravochnick.ru/psihologiya/psihologicheskiy_analiz/psihologicheskiy_analiz_rechi/
https://anticoach.org/speech-analysis

https://vc.ru/begovatovd/722188-5-rossiyskih-servisov-dlya-rechevoy-analitiki-svodnaya-tablica-resheniy-s-cenami
import sqlite3
import subprocess,os
import flet as ft

def main(page):

    tabel = ft.TextField(label="Табельный номер", autofocus=True, width = 200)
    fio = ft.TextField(label="ФИО", width = 400)
    Computer = ft.TextField(label="Имя ПК", width = 400)
    unit=ft.TextField(label="Подразделение", width = 400)
    root_unit = ft.TextField(label="Структурное", width = 400)
    TipCart = ft.TextField(label="Карты сертификаты", width = 400)
    greetings = ft.Column()

    def btn_click(e):
        con = sqlite3.connect("db.sqlite3")
        cursor = con.cursor()
        page.update()
        tabel.focus()
        if not fio.value:
            tabel.error_text = "Please enter your name"
            page.update()
        else:
            cursor.execute(f"""SELECT FIO, COMPUTER, unit, root_unit, TipCart FROM polls_PERSON
                                   WHERE fio like '{fio.value}%'  
                               """)
            rows = cursor.fetchall()
            cursor.close()
            con.close()
            for r in rows:
                fio.value, Computer.value, unit.value, root_unit.value, TipCart.value = r[0], r[1], r[2], r[3], r[4]
                page.update()

    def btn_clickDMWare(e):
        if (Computer.value != ''):
            print(Computer.value)
            subprocess.call(f"C:\Program Files (x86)\DameWare Development\DameWare NT Utilities\DWRCC.exe -c: -h: -m:{Computer.value} -a:1")


    page.add(
        tabel, fio, Computer, unit, root_unit, TipCart,
        ft.ElevatedButton("Искать!", on_click=btn_click),
        ft.ElevatedButton("DMWare!", on_click=btn_clickDMWare),
        greetings,
    )

ft.app(target=main)




