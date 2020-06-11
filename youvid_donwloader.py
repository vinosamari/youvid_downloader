import pytube
import kivy
from pytube import YouTube
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.popup import Popup


LabelBase.register(name='Concept', fn_regular='Concept.ttf')
LabelBase.register(name='Bertina', fn_regular='Bertina.otf')



# video_link = YouTube('https://www.youtube.com/watch?v=F4tpoFcnmRM')
# print('=====#####=====')
# print(f'Downloading {video_link.title}')
# print('=====#####=====')
# # video_link.download()
# print('=====#####=====')
# print('Done!')
# print('=====#####=====')

class MainLayout(GridLayout):
    
    def download_button(self):
        try:
            self.video_link = YouTube(self.ids.link.text)
            print(f'This is what was pasted===={self.video_link}')
            self.ids.butt1.text = "Downloading"
            self.ids.butt1.background_color = 0,0,1,0.85
            self.ids.link.text = ""
        except (
            ValueError, TypeError, pytube.exceptions.RegexMatchError,
        ):
            self.ids.butt1.font_size = 25
            self.ids.butt1.text = "Download Error. Refresh & Try Again."
            self.ids.butt1.background_color = 1,0,0,0.6
            
            
        
        
    def refresh_button(self):
        self.ids.link.text = ""
        self.ids.butt1.text = "Download"
        self.ids.butt1.background_color = 0.43,0.123,0.5,0.6
        
        
    def help_popup(self):
        popupText = """ 
        * Check Your Downloads Folder To See All Your Youvid Downloads
        * The 'linkslog' Text File Contains Your Download History.
        * For More Help Contact support@Huetopia.com"""
        popup = Popup(title='YouVid Downloader Help', content=Label(text=popupText, font_name='Bertina'),
                       auto_dismiss=True, size_hint=(0.75,0.5))
        popup.open()
        
        
    pass

class Youvid_Downloader(App):
    def build(self):
        Config.set('graphics', 'width', 700)
        Config.set('graphics', 'height', 300)
        Config.set('graphics', 'resizable', 0)
        # Config.set('graphics', 'borderless', 0)
        self.title = "Youvid Video Downloader"
        return MainLayout()


Youvid_Downloader().run()
