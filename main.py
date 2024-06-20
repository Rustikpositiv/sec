from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
import time

class StopWatchApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_time = None
        self.position = 0
    def build(self):
        Window.size = (720, 1280)  # Set window size

        self.layout = GridLayout(cols=1, padding=10)

        self.time_label = Label(
            text='00:00:00.000',
            font_size=48,
            halign='center',
            valign='middle'
        )
        self.layout.add_widget(self.time_label)

        self.start_button = Button(text='Старт', font_size=48)
        self.start_button.bind(on_press=self.start_stopwatch)  # Bind to the method
        self.layout.add_widget(self.start_button)

        self.stop_button = Button(text='Стоп', font_size=48)
        self.stop_button.bind(on_press=self.stop_stopwatch)
        self.stop_button.disabled = True
        self.layout.add_widget(self.stop_button)

        self.reset_button = Button(text='Сброс', font_size=48)
        self.reset_button.bind(on_press=self.reset_stopwatch)
        self.reset_button.disabled = True
        self.layout.add_widget(self.reset_button)

        return self.layout

    def start_stopwatch(self, instance):
        if self.start_time == None:
            self.start_time = time.time()
        self.layout.children[0].disabled = True
        self.stop_button.disabled = False
        self.reset_button.disabled = False
        if self.position == 0:
            self.position = 1
            self.stop_watch_event = Clock.schedule_interval(self.update_time_label, 0.001)


    def stop_stopwatch(self, instance):
        self.position = 0
        Clock.unschedule(self.stop_watch_event)
        self.start_button.disabled = False
        self.reset_button.disabled = False

    def reset_stopwatch(self, instance):
        self.position = 0
        Clock.unschedule(self.stop_watch_event)
        self.start_time = time.time()
        self.update_time_label(None)
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.reset_button.disabled = True

    def update_time_label(self, dt):
        elapsed_time = time.time() - self.start_time
        milliseconds = int(elapsed_time * 1000) % 1000
        seconds = int(elapsed_time) % 60
        minutes = int((elapsed_time // 60) % 60)
        hours = int(elapsed_time // 3600)
        time_text = '{:02}:{:02}:{:02}.{:03d}'.format(
            hours, minutes, seconds, milliseconds
        )
        self.time_label.text = time_text


if __name__ == '__main__':
    StopWatchApp().run()
