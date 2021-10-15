from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from math import pi as p


Config.set('graphics', 'resizable', '0')  # Команда скажет Киви , что окно не должно менять размер
Config.set('graphics', 'width', '800')  # Ширина окна
Config.set('graphics', 'height', '500')  # Высота окна

class Raschet (App):
    def update_label1(self):
        self.lbl1.text = self.formula1
    def update_label2 ( self):
        self.lbl2.text = self.formula2
    def update_label3 (self):
        self.lbl3.text = self.formula3
    def update_label4 (self):
        self.lbl4.text = self.formula4

    # Функция расчета площади круга
    def ras_kr(self, instance):
        self.formula1 = 'p*('+str(instance.text)+'**2)'
        print(self.formula1)
        self.formula1 = str("%.2f" % (eval(self.formula1)))
        self.update_label1()
        self.formula1 = ""

    # Функция расчета площади цилиндра
    def ras_cill(self,instance):
        self.formula2=str(self.lbl1.text)+'*'+str(instance.text)
        print(self.formula2)
        self.formula2=str("%.2f" %(eval(self.formula2)))
        self.update_label2()
        self.formula2 = ""

    # Функция расчета суммарной пллощади образцов
    def ras_obs(self,instance):
        self.formula3=str(self.lbl2.text)+'*'+str(instance.text)
        print(self.formula3)
        self.formula3=str("%.2f" %(eval(self.formula3)))
        self.update_label3()
        self.formula3=""

    # Функция расчета веса цилиндров в зависимости от материала
    def ras_ves(self,instance):
        if (str(instance.text).lower() == "алюминий"):
            self.formula4=str(self.lbl3.text)+'*2.7'
        elif (str(instance.text).lower() == "свинец"):
            self.formula4=str(self.lbl3.text)+'*11.35'
        elif (str(instance.text).lower() == "золото"):
            self.formula4=str(self.lbl3.text)+'*19.32'
        else:
            self.formula4 = str(self.lbl3.text) + '*4.54'
        print(self.formula4)
        self.formula4 = str(str("%.2f" %(eval(self.formula4)))+'\n'"Граммов")
        self.update_label4()
        self.formula4 = ""



    def build(self):

        # Добавляем переменную Formula1, которая расчитывает площадь круга
        self.formula1 = ""

        # Добавляем переменную Formula2, которая расчитывает площадь цилиндрА по длине
        self.formula2 = ""

        # Добавляем переменную Formula, которая расчитывает площадь цилиндрОВ по кол-ву цилиндров
        self.formula3 = ""

        # добавляем переменную Formula4, которая будет считать вес циолиндров в зависимости от материала
        self.formula4 = ""


        # Основной бокс, делит поле окна на 2 части по горизонтали Orientation=Vertical
        bl1 = BoxLayout(
                    orientation='horizontal'
                    )

        # Второй бокс, делит правое поле основного бокса на 4 части по вертикали Orientation=Horizontal
        bl2 = BoxLayout(
                    orientation='vertical',
                    size_hint=(.3, 1)
                    )

        gl = GridLayout(cols=4, spacing=0, size_hint=(.7,1))  # Грид для кнопок 4 ряда 4 колонны, 16 кнопок
        # сайзхинт (1=100% по вертикали и .7=70% по горизонтали, остальные 30% отданы BL1 с лэйблами


        self.lbl1=Label(text='ничего не выбрано', font_size=20) # лэй вывода Площади круга Pi*(r^2)
        self.lbl2=Label(text='ничего не выбрано', font_size=20) # лэй вывода Площади цилиндра Pi*(r^2)*l
        self.lbl3=Label(text='ничего не выбрано', font_size=20) # лэй вывода Площади суммы цилиндров Pi*(r^2)*l*n
        self.lbl4=Label(text='ничего не выбрано', font_size=20) # лэй вывода Общего веса, относительно материала

        gl.add_widget((Label(text='Расчет площади\nсреза\nв см^2\n\nВыберите радиус')))
        gl.add_widget((Button(text='3', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_kr)))
        gl.add_widget((Button(text='4', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_kr)))
        gl.add_widget((Button(text='5', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_kr)))

        gl.add_widget((Label(text='Расчет площади\nцилиндра\nв см^3\n\nВыберите длину\n цилиндра')))
        gl.add_widget((Button(text='3', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_cill)))
        gl.add_widget((Button(text='4', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_cill)))
        gl.add_widget((Button(text='5', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_cill)))

        gl.add_widget((Label(text='Расчет площади\nобразцов\nв см^3\n\nВыберите \nколичество\nобразцов')))
        gl.add_widget((Button(text='1', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_obs)))
        gl.add_widget((Button(text='2', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_obs)))
        gl.add_widget((Button(text='3', font_size=40, background_color=[1, 1, 0, 1], on_press=self.ras_obs)))

        #   Материалы
        #   Al = алюминий, плотность 2.7 г/см^3
        #   Pb = свинец, плотность 11,35 г/см^3
        #   Au = золото, плотность 19,32 г/см^3
        #   Ti = титан, удельная плотность 4,54 г/см^3

        gl.add_widget((Button(text='Алюминий', font_size=20, background_color=[1, 1, 0, 1], on_press=self.ras_ves)))
        gl.add_widget((Button(text='Свинец', font_size=20, background_color=[1, 1, 0, 1], on_press=self.ras_ves)))
        gl.add_widget((Button(text='Золото', font_size=20, background_color=[1, 1, 0, 1], on_press=self.ras_ves)))
        gl.add_widget((Button(text='Титан', font_size=20, background_color=[1, 1, 0, 1], on_press=self.ras_ves)))

        # добавляем в BL1 - Gl
        bl1.add_widget(gl)

        # Добавляем в BL2 - Label
        bl2.add_widget(self.lbl1)
        bl2.add_widget(self.lbl2)
        bl2.add_widget(self.lbl3)
        bl2.add_widget(self.lbl4)

        # добавляем в BL1 - BL2
        bl1.add_widget(bl2)

        # Возвращаем BL1
        return bl1

if __name__ == "__main__":
    Raschet().run()