import pyperclip
from tkinter import *
from customModelSettingsAts1 import *



def scanProduct():
    root = Tk()
    root.geometry("800x150")
    root.title("ATS Bot")
    label = Label(root, text="Escanee la pieza del modelo a configurar:")
    label.config(font=('ARIAL', '30'), fg='blue')
    global product
    product = StringVar()
    textBox = Entry(root, textvariable=product, width=20)
    textBox.config(font=('Arial', 30), bd=4)

    def enterEvent(event):
        global workOrder
        workOrder = StringVar()
        workOrder.set(product.get())
        root.destroy()

    root.bind('<Return>', enterEvent)

    label.pack()
    textBox.pack()
    textBox.focus()

    root.mainloop()


def mes():
    showDesktop()
    findAndClick(mesIconPic, 5, 0.9, True)
    findAndClick(mesLoginBtnPic, 10, 0.9, False)
    findAndClick(mesSideMenuBtnPic,10, 0.9,False)
    findAndClick(startWorkingSideMenuPic,10, 0.9,False)
    time.sleep(0.2)
    pag.press('tab')
    pag.write(workOrder.get())
    pag.press('enter')
    findAndClick(blueOKbtnPic,4, 0.9,False)
    time.sleep(0.2)
    pag.press('enter')
    findAndClick(processScanSearchPic, 5, 0.9, False)
    findAndClick(processScanSearchTextBoxPic, 5, 0.9, False)
    time.sleep(0.2)

    pag.write(workOrder.get())
    findAndClick(mesSearchBtnPic, 5, 0.9, False)
    time.sleep(0.5)
    pag.press('tab', presses=5)
    time.sleep(0.2)
    pag.keyDown('ctrlleft')
    pag.press('c')
    pag.keyUp('ctrlleft')
    global model
    model = pyperclip.paste()
    model = eval(model.replace('-',''))
    time.sleep(0.2)
    showDesktop()


def ats():
    # Open ATS
    findAndClick(atsShortcutPic,10, 0.90, True)
    time.sleep(0.2)

    #findAndClick(runBtnPic, 5, 0.9, False)
    findAndClick(settingsBtnPic, 20, 0.9, False)
    if findAndBool(barcodeLabelPic, 10, 0.9):
        time.sleep(1)
        pag.press('tab', presses=2, interval=0.1)
        pag.press('enter')
    findAndClick(botTestFilesPic, 5, 0.95, True)
    findAndClick(ATS1FolderPic if AtsModel() else ATS2FolderPic, 5, 0.95, True)

    # FIRST TIME OPENING FILE
    while pag.locateCenterOnScreen(modelAtsFile, confidence=0.95) is None:
        print('Encontré el archivo')
        pag.scroll(-300)
    # LOAD FILE
    pag.doubleClick(pag.locateCenterOnScreen(modelAtsFile, confidence=0.95))
    print('cargué el archivo')
    time.sleep(0.3)
    while pag.locateCenterOnScreen(atsOpenBtnPic, confidence=0.95) is None:
        print('no encuentro el boton de abrir')
        pag.scroll(-300)
    time.sleep(0.5)
    pag.click(pag.locateCenterOnScreen(atsOpenBtnPic))
    print('Ya encontré el botón de abrir y le piqué')
    findAndClick(botTestFilesPic, 5, 0.95, True)
    findAndClick(ATS1FolderPic if AtsModel() else ATS2FolderPic, 5, 0.95, True)


    # SECOND TIME OPENING FILE
    while pag.locateCenterOnScreen(modelAtsFile, confidence=0.95) is None:
        pag.scroll(-300)
    pag.doubleClick(pag.locateCenterOnScreen(modelAtsFile, confidence=0.95))
    print('Ya cargué el segundo archivo')
    time.sleep(0.3)


    print('termine proceso normal ats')
    # FINISHED LOADING FILE
    # NEXT COMES CUSTOM MODEL SETTINGS
    print('antes de custom settings')
    setSettings(model.writeCurrent, model.dwSwitch)
    print('despues de custom settings')

    ### VALIDATE EVERYTHINGS OK
    if findAndBool(inventronicsLogoPic, 5, 0.95):
      pag.alert('¡Configuración Exitosa! Puede comenza a probar.')



# killTasks()
# scanProduct()
# mes()
# print(model)
# print(model.get_data)
# modelAtsFile = model.ssAts1 if AtsModel() else model.ssAts2
# print(modelAtsFile)
# print(model)
# ats()

















