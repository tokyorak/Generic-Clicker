from ssl import Options
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from enum import Enum
from math import floor
import Option
import ClickMouse



mouse = Controller() # Gets the mouse controller

options = Option()
options.mouse = mouse
options.click_mode = Mode.DATING_EVENT
options.sleep_mode = 30 #minutes
options.click_cost = 2 #1 minute
options.times_clicking = 1 #5
options.charging_time = 60 # 150 seconds
options.waiting_delay = options.click_cost * options.times_clicking * options.charging_time

options.delay = 1
options.left_button = Button.left

options.start_stop_key = KeyCode(char = '1')
options.exit_key = KeyCode(char = '2')
options.position_key = KeyCode(char = '3')

options.test_key = KeyCode(char = '4')
options.cost_key = KeyCode(char = '5')

# back_position = (769, 919)
options.back_position = (753,844)#(757, 860)
options.reload_position = (89, 52)
options.confirm_reload_position = (1018, 226)
options.enter_position = (939,876)#(919, 893)
options.close_position = (939,876) #(932, 893)
options.close_position_1_2 = (807, 754)
options.close_position_last_chance = (1056,783) #(1060 ,770)
options.event_position = (950, 613)
options.close_position_2 = (762, 746)
options.final_position = (911, 836) # (962, 822) # (868, 829)
options.reload_delay = 2700 # 45 min

# volume position
options.menu_position = (1147,166)
options.volume_1_position = (868,334) #(868,333)
options.volume_2_position = (868,370) #(868,369)

# dating event Extended positions
options.energy_position = (789, 780)
options.collect_energy_position = (1084, 773)
options.close_dating_1 = (962, 697)
options.close_dating_2 = (943, 873)



# Since Clickmouse inherits from thread class it can be launched as one
click_thread = ClickMouse(options)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("Clicker paused")
        else:
            click_thread.start_clicking()
            print("Clicker resumed")
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        print("Clicker stopped")
    elif key == position_key:
        click_thread.printPosition()
    elif key == test_key:
        click_thread.test()

with Listener(on_press = on_press) as listener:
    listener.join()
