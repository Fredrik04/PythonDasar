import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        
        button = Button(text="Klik Saya")
        button.bind(on_press=self.on_button_click)
        
        layout.add_widget(button)
        
        return layout
    
    def on_button_click(self, instance):
        print("Tombol diklik")

if __name__ == '__main__':
    MyApp().run()
