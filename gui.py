import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from commands import Commands

class RootWidget(BoxLayout):
    pass

class MenuWidget(GridLayout):
    commands = Commands()

    def __init__(self, **kwargs):
        super(MenuWidget, self).__init__(**kwargs)
        self.cols = 2
        button  = Button(text='Load')
        button.bind(on_press=self.callback)
        self.add_widget(button)

    def playSoundCallback(self, value):
        self.commands.playSound(value.Filename)

    def callback(self, value):
        self.clear_widgets()
        soundList = self.commands.soundList()

        for sound in soundList["sounds"]:
            soundButton = Button(text=sound['Filename'])
            soundButton.create_property('Filename', sound['Filename'])
            soundButton.bind(on_press=self.playSoundCallback)
            self.add_widget(soundButton)

class Mullesounds(App):

    def build(self):
        root = RootWidget()
        menu = MenuWidget()
        root.add_widget(menu)
        return root
