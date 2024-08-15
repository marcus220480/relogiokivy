from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from datetime import datetime

class Relogio(MDApp):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.layout.canvas.before.clear()
        with self.layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
            self.layout.bind(size=self._update_rect, pos=self._update_rect)

        self.data_label = Label(
            text=self.get_date(),
            font_size='70sp',
            halign='center',
            color=(1, 1, 1, 1)
        )

        self.hora_label = Label(
            text=self.get_time(),
            font_size='64sp',
            halign='center',
            color=(1, 1, 1, 1)
        )

        self.layout.add_widget(self.data_label)
        self.layout.add_widget(self.hora_label)

        Clock.schedule_interval(self.update_time, 1)
        return self.layout

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def get_date(self):
        return datetime.now().strftime('%d/%m/%Y')

    def get_time(self):
        return datetime.now().strftime('%H:%M:%S')

    def update_time(self, *args):
        self.hora_label.text = self.get_time()
        self.data_label.text = self.get_date()

if __name__ == "__main__":
    Relogio().run()
