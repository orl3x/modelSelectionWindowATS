from tkinter import *

firstTime = 1

def chooseModelWindow():
    modelWindow = Tk()
    # MAIN TITLE
    modelWindow.title("Selección de modelo")
    title = Label(modelWindow, text="Selección de modelo")
    title.config(font=('ARIAL', '30'), fg='blue')

    # FAMILY TITLE
    familyTitle = Label(modelWindow, text="Familia: ")
    familyTitle.config(font=('ARIAL', '25'), fg='black')

    # MODEL TITLE
    modelTitle = Label(modelWindow, text="Modelo: ")
    modelTitle.config(font=('ARIAL', '25'), fg='black')

    # DROP DOWN LIST FOR FAMILY
    familyOptionList = ["EUD", "EUG", "ESD"]


    # DROPDOWN LIST FOR MODEL
    #EUD FAMILY MODELS
    eudOptions = ["EUD075S180DT", "EUD075S280DT", "EUD150S350DTA", "EUD150S560DTA", "EUD600S12ADT"]

    #EUG FAMILY MODELS
    eugOptions = ["EUG150S105DTFT02", "EUG150S350DT"]

    #ESD FAMILY MODELS
    esdOptions = ["ESD600S12ADT", "ESD320S620DT", "ESD240S460DT", "ESD240S660DT"]

    #EMPTY OPTION
    emptyOption = [" "]

    #FUNCTION TO UPDATE MODEL DROPDOWN
    def updateListContent(*args):
        if familyVariable.get() == "EUD":
            setDropdownModelList(eudOptions)
        elif familyVariable.get() == "EUG":
            setDropdownModelList(eugOptions)
        elif familyVariable.get() == "ESD":
            setDropdownModelList(esdOptions)
        else:
            setDropdownModelList(emptyOption)



    #SETTING DROPDOWN LIST FOR FAMILY
    familyVariable = StringVar()
    familyVariable.trace("w", updateListContent)
    familyDropdown = OptionMenu(modelWindow, familyVariable, *familyOptionList)
    familyDropdown.config(width=30, font=('Helvetica', 12))



    #SETTING DROPDOWN LIST FOR MODELS
    def setDropdownModelList(familyName):
        modelsVariable = StringVar()
        modelsDropdown = OptionMenu(modelWindow, modelsVariable, *familyName)
        modelsDropdown.config(width=30, font=('Helvetica', 12))

        modelsDropdown.pack()

    def setDropdownModelListFirstTime(familyName):
        modelsVariable = StringVar()
        modelsDropdown = OptionMenu(modelWindow, modelsVariable, *familyName)
        modelsDropdown.config(width=30, font=('Helvetica', 12))
        modelsDropdown.pack()




    title.pack()
    familyTitle.pack()
    familyDropdown.pack()
    modelTitle.pack()
    setDropdownModelListFirstTime(emptyOption)




    modelWindow.mainloop()

chooseModelWindow()