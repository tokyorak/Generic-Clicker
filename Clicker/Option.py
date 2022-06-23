from pynput.mouse import Button
from pynput.keyboard import KeyCode
from enum import Enum


class Option:
    def __init__(self) -> None:
        self.click_mode = Mode.DATING_EVENT
        self.sleep_mode = 30 #minutes
        self.click_cost = 2 #1 minute
        self.times_clicking = 1 #5
        self.charging_time = 60 # 150 seconds
        self.waiting_delay = self.click_cost * self.times_clicking * self.charging_time

        self.delay = 1
        self.left_button = Button.left

        self.start_stop_key = KeyCode(char = '1')
        self.exit_key = KeyCode(char = '2')
        self.position_key = KeyCode(char = '3')

        self.test_key = KeyCode(char = '4')
        self.cost_key = KeyCode(char = '5')

        # back_position = (769, 919)
        self.back_position = (753,844)#(757, 860)
        self.reload_position = (89, 52)
        self.confirm_reload_position = (1018, 226)
        self.enter_position = (939,876)#(919, 893)
        self.close_position = (939,876) #(932, 893)
        self.close_position_1_2 = (807, 754)
        self.close_position_last_chance = (1056,783) #(1060 ,770)
        self.event_position = (950, 613)
        self.close_position_2 = (762, 746)
        self.final_position = (911, 836) # (962, 822) # (868, 829)
        self.reload_delay = 2700 # 45 min

        # volume position
        self.menu_position = (1147,166)
        self.volume_1_position = (868,334) #(868,333)
        self.volume_2_position = (868,370) #(868,369)

        # dating event Extended positions
        self.energy_position = (789, 780)
        self.collect_energy_position = (1084, 773)
        self.close_dating_1 = (962, 697)
        self.close_dating_2 = (943, 873)


class Mode(Enum):
    BASIC = 1
    DATING_EVENT = 2

# Set for a click event
# Basic mode = 1
# Dating event = 2
# click only = 3

