# importar o App, Builder (GUI)
# criar o app
# criar função build

from kivy.app import App
from kivy.lang import Builder
import pyautogui
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
from KivyOnTop import register_topmost
from kivy.config import Config
from pynput import keyboard
import time
import pyautogui
from pynput.mouse import Listener

Window.size = (500,500)

class Panel(FloatLayout):

	btn = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Panel, self).__init__(**kwargs)
		# Panel.create_listener(self)
		self.on = False

	def activate_autoclicker(self):
		# self.slider.disabled = True
		# pyautogui.PAUSE = 1 / self.slider.value
		Clock.schedule_interval(self.click, 2)

	def stop_autoclicker(self):
		# self.slider.disabled = False
		Clock.unschedule(self.click)

	def change_button(self):
		if self.on:
			self.btn.background_color = (.157, .455, .753, 1)
			self.btn.text = "START"
			# self.stop_autoclicker()

			win10 = pyautogui.screenshot(region=(0, 1041, 50, 39))
			location = pyautogui.locateOnScreen(win10)
			pyautogui.click(location)

			time.sleep(1)

			powerOff = pyautogui.screenshot(region=(0, 1000, 50, 39))
			powerOfflocation = pyautogui.locateOnScreen(powerOff)
			pyautogui.click(powerOfflocation)
		else:
			self.btn.background_color = (1, .4, 0, 1)
			self.btn.text = "STOP"
			# self.activate_autoclicker()		
		self.on = not self.on

	# def click(self, *args):
	# 	pyautogui.click()

	# def on_release(self, key, *args):
	# 	if keyboard.Key.f4 in args:
	# 		self.change_button()

	# def create_listener(self):
	# 	listener = keyboard.Listener(on_release=lambda key, *args: self.on_release(self, key, *args))
	# 	listener.start()

GUI = Builder.load_file("kv.kv")

class MeuApp(App):
	def build(self):
		return GUI
	
	def on_start(self):
		print('chamou on_start')
		# win10 = pyautogui.screenshot(region=(0, 1041, 50, 39))
		# location = pyautogui.locateOnScreen(win10)
		# pyautogui.click(location)

		# time.sleep(1)

		# powerOff = pyautogui.screenshot(region=(0, 1000, 50, 39))
		# powerOfflocation = pyautogui.locateOnScreen(powerOff)
		# pyautogui.click(powerOfflocation)

		# location[0] is the top left x coord
		# location[1] is the top left y coord
		# location[2] is the distance from left x coord to right x coord
		# location[3] is the distance from top y coord to bottom y coord

		# x_boundary_left = location[0]
		# y_boundary_top = location[1]
		# x_boundary_right = location[0] + location[2]
		# y_boundary_bottom = location[1] + location[3]

		# def on_click(x, y, button, pressed):
		#     if x_boundary_left < x < x_boundary_right and y_boundary_bottom > y > y_boundary_top and str(button) == 'Button.left' and pressed:
		#         print('You clicked on Windows 10 Logo')
		#         return False    # get rid of return statement if you want a continuous loop
		
		# with Listener(on_click=on_click) as listener:
		#     listener.join()

if __name__ == "__main__":
	MeuApp().run()