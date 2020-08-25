import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from predict import pred
from matplotlib import pyplot as plt

class mainMenu(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 3#attribute of GridLayout
        self.path = TextInput(text = "C:\\Users\\anshs\\Desktop\\study\\py\\datasets\\input\\pothole-detection-dataset\\potholes\\1.jpg")#create an instance of TextInput in class page
        self.label = Label(text = "Enter Path")#create an instance of label in class page
        self.submit = Button(text = "Submit")
        self.submit.bind(on_press = self.find)
        self.add_widget(self.label)#add label to gridlayout (add_widget is funct of GridLayout)
        self.add_widget(self.path)#add textinput
        self.add_widget(self.submit)

    def find(self, instance):
        img, result = pred(self.path.text)
        predictor.outmenu.setData(img1 = self.path.text, result1 = f"{result}")
        predictor.screenmanager.current = "OutMenu"
        #print("result is: ", result)
        #plt.imshow(img)
        #plt.show()

class outMenu(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.setData()
        #self.img = predictor.mainmenu.img
        #self.result = predictor.mainmenu.result
        #print(self.result)
        self.rows = 3
        self.label = Label(text = "your image was:")

        self.image = Image()
        self.score = Label()
        self.HLayout = GridLayout(cols = 2)
        self.HLayout.add_widget(self.image)
        self.HLayout.add_widget(self.score)

        self.back = Button(text = "Back")
        self.back.bind(on_press = self.goBack)

        self.add_widget(self.label)
        self.add_widget(self.HLayout)
        self.add_widget(self.back)
        #self.add_widget(self.score)

    def setData(self, img1, result1):
        self.image.source = img1
        self.score.text = "pothole score is: "+result1+"%"

    def goBack(self, instance):
        predictor.screenmanager.current = "MainMenu"

class application(App):#calling function
    def build(self):#.run() funct  of App class (inherited by application) calls the build function. if not found, there is a default definition of a black screen
        self.screenmanager = ScreenManager()

        self.mainmenu = mainMenu()
        MainMenu = Screen(name = 'MainMenu')
        MainMenu.add_widget(self.mainmenu)
        self.screenmanager.add_widget(MainMenu)

        self.outmenu = outMenu()
        OutMenu = Screen(name = 'OutMenu')
        OutMenu.add_widget(self.outmenu)
        self.screenmanager.add_widget(OutMenu)

        return self.screenmanager#return an object of class page

if __name__ == "__main__":
    predictor = application()
    predictor.run()
