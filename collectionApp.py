# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:42:02 2022

@author: belt1
"""
# imports
#citations for plyer and merkle tree
#https://github.com/Tierion/pymerkletools
#https://github.com/kivy/plyer


__version__ = '1.0'

import kivy
kivy.require('1.0.6')
import collections

import merkletools
from merkletools import MerkleTools
import hashlib
#merkle tree
mt = MerkleTools()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.properties import StringProperty



# Designate Our .kv design file 

#TO DO
#Create buttons of 3-5 locations of the submission uw 1 uw 2 arc etc.
#hook the code up to some sort of data storage, text file for now?
#Clean it up make the ui look nice


locationData = collections.namedtuple('locationData',['location','noiseLevel'])

#

   
class MyLayout(Screen):
    location_string = "test"
    def modifyString(self,string):
        MyLayout.location_string = string
    
    #pass


class ScreenTwo(Screen):
    location_string =  MyLayout.location_string
    noise_level = 0;
    def slide_it(self, *args):
        #print(args[1])
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = 20
        ScreenTwo.noise_level = str(int(args[1]))
        
    def testPrint(self):
        print("hello world")
        print(MyLayout.location_string)
        print(ScreenTwo.noise_level)
        
        
         
class merkleTree():
    def storeInfo(self):
        noise_level =ScreenTwo.noise_level
        location = MyLayout.location_string
    
        treeData = [noise_level,location]
        #second input in add_leaf method sets the value to be hashed in the tree
        print(treeData)
        mt.add_leaf(treeData,True)
        mt.make_tree()
        print( "root:", mt.get_merkle_root())
        print (mt.get_proof(0))
        print (mt.validate_proof(mt.get_proof(0), mt.get_leaf(0), mt.get_merkle_root()))  # True



class ScreenThree(Screen,merkleTree):
    
    def closeApp(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
        
class ScreenManagement(ScreenManager):
    #pass these variables in the merkle tree store method
    location_string = MyLayout.location_string
    location_number = 0
    #Could pass into method from kivy code if they don't update from here? probably have to do that
    
    
class infoCollector(App):
    #location_number = 0
    #location_string = "2"
    #sm = ScreenManager()
        


    def build(self):
        #Window.clearcolor = (1,1,1,1)
        #infoCollector.sm.add_widget(MyLayout(name="screen_1"))
        #infoCollector.sm.add_widget(ScreenTwo(name="screen_2"))
       # Window.bind(on_request_close=self.on_request_close)

        return Builder.load_file('menu.kv')
    
    #pass
 
    
#ensures that the program runs when the file is executed, comment out to toggle off
if __name__ == "__main__":
 infoCollector().run()
 #merkleTree()
