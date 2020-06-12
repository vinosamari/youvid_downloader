import pytube
import kivy
import datetime
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
from datetime import date, time


LabelBase.register(name='Concept', fn_regular='Concept.ttf')
LabelBase.register(name='Bertina', fn_regular='Bertina.otf')



class MainLayout(GridLayout):
    
    
    
    def download_button(self):
        with open("Youvid_Download_History.txt", 'a+') as htf:
            # vid_title = YouTube(self.ids.link.text).title()
            if self.ids.link.text != "":
                self.video_link = YouTube(self.ids.link.text)
                htf.write("Video Link :" + self.ids.link.text + 
                          
                          "  Date : " + str(date.today()) + '\n')
            else:
                htf.seek(2)
                
        
        
        try:
            self.video_link = YouTube(self.ids.link.text)
            self.ids.butt1.text = "Downloading"
            self.video_link.streams.get_highest_resolution().download()
            
            self.ids.butt1.background_color = 0,0,1,0.85
            # self.download_popup()
            # self.ids.link.text = ""
        except (
            ValueError, TypeError, pytube.exceptions.RegexMatchError,
        ):
            self.ids.butt1.font_size = 25
            self.ids.butt1.text = "Download Error. Refresh & Try Again."
            self.ids.butt1.background_color = 1,0,0,0.6
            
            
            
        
            
            
            
        
        
    def refresh_button(self):
        self.ids.link.text = ""
        self.ids.butt1.text = "Download"
        self.ids.butt1.background_color = 0.75,0.5,0,0.6
        
        
    def help_popup(self):
        popupText = """ 
        * Check Your Downloads Folder To See All Your Youvid Downloads
        * The "Youvid_Download_History.txt" Text File Contains Your Download History.
        * For More Help Contact support@youniversal.com"""
        popup = Popup(title='YouVid Downloader Help', content=Label(text=popupText, font_name='Bertina'),
                       auto_dismiss=True, size_hint=(0.75,0.5))
        popup.open()
        self.refresh_button()
        
    def download_popup(self):
        popupText = """ * Check Your Downloads Folder To See All Your Youvid Downloads"""
        popup = Popup(title='Your File Is Downloading', content=Label(text=popupText, font_name='Bertina'),
                   auto_dismiss=True, size_hint=(0.75,0.3))
        popup.open()
        # self.refresh_button()
        
    pass

class Youvid_Downloader(App):
    def build(self):
        Config.set('graphics', 'width', 700)
        Config.set('graphics', 'height', 300)
        # Config.set('graphics', 'resizable', 0)
        # Config.set('graphics', 'borderless', 0)
        self.title = "Youvid Video Downloader"
        return MainLayout()


Youvid_Downloader().run()
