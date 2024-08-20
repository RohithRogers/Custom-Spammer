import flet as ft
import pyautogui as pg
import time

customlist = []

def coutnt(l):
    c = 0
    for elem in l:
        c += 1
    return c


def main(page):
    page.title = "Message Spammer"
    page.window_width = 550
    page.window_height = 550
    page.window_maximizable = False
    page.bgcolor = "#A7E6FF"

    nums = ft.Text("0",size=20,color="black")
    hel = ft.Text("0",size=20,color="black")
    anot = ft.Text("0",color="black",size=20)
    anot1 = ft.Text("0",color="black",size=20)
    def increase(e):
        num = int(nums.value)
        if num < 10:
            num += 1
            nums.value = str(num)
            page.update() 
    def decrease(e):
        num = int(nums.value)
        if num > 0:
            num -= 1
            nums.value = str(num)
            page.update()
        
    def inc(e):
        num = int(anot.value)
        if num < 10:
            num += 1
            anot.value = str(num)
            page.update() 

    def dec(e):
        num = int(anot.value)
        if num > 0:
            num -= 1
            anot.value = str(num)
            page.update() 

    def incr(e):
        helo = int(anot1.value)
        if helo < 100:
            helo += 1
            anot1.value = str(helo)
            page.update()

    def decr(e):
        helo = int(anot1.value)
        if helo > 0:
            helo -= 1
            anot1.value = str(helo)
            page.update()
    
    def increaset(e):
        helo = int(hel.value)
        if helo < 100:
            helo += 1
            hel.value = str(helo)
            page.update()

    def decreaset(e):
        helo = int(hel.value)
        if helo > 0:
            helo -= 1
            hel.value = str(helo)
            page.update()
        
    text = ft.TextField(autofocus=True,max_length=50,text_size=15,label="Message",color="black")

    def submit(e):
        if text.value and nums.value != "0" and hel.value != "0":
            string = text.value
            string += "\n"
            timet = int(nums.value)
            threads = int(hel.value)
            time.sleep(timet)
            for i in range(threads):
                pg.write(string)            
                pg.click()
            
    text2 = ft.TextField(max_length=50,text_size=15,label="Message",color="black")
    listobj = ft.TextField(text_size=15,label="Custom list",color="black")
    texts = ft.Column(controls=[ft.Text("Welcome to the App",size=30,weight="w600"),
                        ft.Text("Default Tab: ",size=25,weight="w250"),
                        ft.Text("Step 1: Type your message in the message box \nStep 2: Set the timer to wait for (recommended 10) and no of threads to send (maximum 100) \nStep 3: Press the start button and navigate to the application(whatsapp,instagram) to type the message \n Step 4: After that all would be taken care by the application ",size=12),
                        ft.Text("Advanced Tab: ",size=25,weight="w250"),
                        ft.Text("Step 1: Type your message in the message box \nStep 2: Now add some words to the custom list which is iterated on each message you send and click add button to add your words to the custom list \nStep 3: Set the timer to wait for and no of threads to send \nStep 4: Press the start button and navigate to the application(whatsapp,instagram) to type the message \nStep 5: After that all would be taken care by the application ",size=12),
                      ])

    def submit2(e):
        if coutnt(customlist) != 0:
            if text2.value and anot.value != "0" and anot1.value != "0":
                string = text2.value
                timet = int(anot.value)
                threads = int(anot1.value)
                time.sleep(timet)
                for i in range(threads):
                    for elem in customlist:
                        newstring = string + "  " + elem + "\n"
                        pg.write(newstring)
                        pg.click()
                        newstring = ""

        else:
            if text2.value and anot.value != "0" and anot1.value != "0":
                string = text2.value
                string += '\n'
                timet = int(anot.value)
                threads = int(anot1.value)
                time.sleep(timet)
                for i in range(threads):
                    pg.write(string)
                    pg.click()

    def add(e):
        if listobj.value:
            customlist.append(listobj.value)
        listobj.value = ""
        page.update()

    def listitems(e):
        for elem in customlist:
            print(elem)

    def clearall(e):
        text2.value = ""
        anot.value = "0"
        anot1.value = "0"
        customlist.clear()
        page.update()

    def clearall2(e):
        text.value = ""
        nums.value = "0"
        hel.value = "0"
        page.update()



    default = ft.Column(controls=[ft.Row(controls=[ft.Text("MESSAGE SPAMMER",color="black",size=30,weight="w600")],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[text],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[ft.Text("Timer : ",size=20,color="black")],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[nums,ft.IconButton(icon=ft.icons.ARROW_UPWARD_ROUNDED,data="inc",on_click=increase),ft.IconButton(icon=ft.icons.ARROW_DOWNWARD_ROUNDED,on_click=decrease)],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[ft.Text("Threads : ",size=20,color="black")],alignment= ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[hel,ft.IconButton(icon=ft.icons.ARROW_UPWARD_ROUNDED,on_click=increaset),ft.IconButton(icon=ft.icons.ARROW_DOWNWARD_ROUNDED,on_click=decreaset)],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[ft.ElevatedButton(text="Start",color="white",bgcolor="#3ABEF9",width=100,height=50,on_click=submit),ft.ElevatedButton(text="Clear",color="white",bgcolor="#3ABEF9",width=100,height=50,on_click=clearall2)],alignment=ft.MainAxisAlignment.CENTER)
                        ])
    
    advanced = ft.Column(controls=[ft.Row(controls=[ft.Text("CUSTOM MESSAGE SPAMMER",color="black",size=30,weight="w600")],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[text2],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[listobj,ft.IconButton(icon=ft.icons.ADD,width=75,height=50,on_click=add)],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[ft.Text("Timer",size=20,color="black")],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[anot,ft.IconButton(icon=ft.icons.ARROW_UPWARD_ROUNDED,on_click=inc),ft.IconButton(icon=ft.icons.ARROW_DOWNWARD_ROUNDED,on_click=dec)],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[ft.Text("Threads",size=20,color="black")],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[anot1,ft.IconButton(icon=ft.icons.ARROW_UPWARD_ROUNDED,on_click=incr),ft.IconButton(icon=ft.icons.ARROW_DOWNWARD_ROUNDED,on_click=decr)],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[ft.ElevatedButton(text="List",color="white",bgcolor="#3ABEF9",width=100,height=50,on_click=listitems),ft.ElevatedButton(text="Clear",color="white",bgcolor="#3ABEF9",width=100,height=50,on_click=clearall),ft.ElevatedButton(text="Start",color="white",bgcolor="#3ABEF9",width=100,height=50,on_click=submit2)],alignment=ft.MainAxisAlignment.SPACE_AROUND)
                        ])
    
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Default",
                content=ft.Container(
                    content=default,
                    gradient= ft.LinearGradient(begin=ft.alignment.top_left,end=ft.alignment.bottom_right,colors=["#A7E6FF","white"]),
                    ink_color="red"
                   
                ),
                
            ),
            ft.Tab(
                text="Advanced",
                content=ft.Container(
                    content=advanced,
                     gradient= ft.LinearGradient(begin=ft.alignment.top_left,end=ft.alignment.bottom_right,colors=["#A7E6FF","white"]),
                )

            ),
            ft.Tab(
                text="Help",
                icon=ft.icons.HELP,
                content=texts,
            ),
        ],
        expand=1,
    )
    page.add(t)
    
ft.app(target=main)  