import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from enum import Enum
from math import floor



class ClickMouse(threading.Thread):

    _click_cost = click_cost

    def __init__(self, options, button):
        super().__init__()
        self.options = options
        self.delay = self.options.delay
        self.button = button
        self.running = False    # Check if autoclick is ON2
        self.program_running = True # Check if the script is on
        self.start_time = time.time()
        self.waiting_delay = self.options.waiting_delay
        self.spamcoordinates = (0, 0)
        self.mode = self.options.click_mode
        self.last_time_clicked = self.start_time
        self.done_clicking_for_dating = False

    def start_clicking(self):
        self.running = True
        print("Autoclicker: ON")

    def stop_clicking(self):
        self.running = False
        print("Autoclicker: OFF")

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def printPosition(self):
        print("Position: {}".format(mouse.position))
        self.spamcoordinates = mouse.position

    def clickAndWait(self, position, delay):
        mouse.position = position
        time.sleep(0.5)
        mouse.click(self.button)
        time.sleep(delay)

    def choosePanel(self, phase):
        coordinates = (0 , 0)
        if phase == 1:
            coordinates = (1075, 456)
        elif phase == 2:
            coordinates = (1075, 545)
        elif phase == 3:
            coordinates = (1075, 615)
        elif phase == 4:
            coordinates = (1075, 710)
        self.clickAndWait(coordinates, 4)

    def test(self):
        print("Test en cours...")
        self.clickAndWait(enter_position, 25)
        self.clickAndWait(close_position, 1)
        self.clickAndWait(close_position, 5)
        self.clickAndWait(close_position_1_2, 5)
        self.clickAndWait(close_position_last_chance, 3)
        self.clickAndWait(close_position_last_chance, 3)

        print("Test en cours...Menu")
        menu_position = (1132,173)

        print("Test en cours...Volume")
        # volume_1_position = (868,350) #(868,333)
        # volume_2_position = (868,382) #(868,369)
        self.clickAndWait(menu_position,1)
        self.clickAndWait(volume_1_position,1)
        self.clickAndWait(volume_2_position,1)
        self.clickAndWait(back_position,1)

        print("Test en cours...Event")
        #============Open event view======================
        self.clickAndWait(event_position, 3)
        self.clickAndWait(close_position, 2)

        print("Test en cours...Dating")
        self.clickAndWait(energy_position,1)
        self.clickAndWait(collect_energy_position,3)
        self.clickAndWait(close_dating_1,1)
        self.clickAndWait(close_dating_2,1)
        print("Test terminé.")

    def reloadAndLocate(self):
        print("Reload time at {}".format(time.ctime()))
        #============Go back to home screen==================
        self.clickAndWait(back_position, 3)
        self.clickAndWait(back_position, 1)

        #============Reload the tab and close ads============
        self.clickAndWait(reload_position, 1)
        # self.clickAndWait(confirm_reload_position, 160)
        self.clickAndWait(confirm_reload_position, 125)
        self.clickAndWait(enter_position, 40)
        # self.clickAndWait(confirm_reload_position, 35)
        # self.clickAndWait(enter_position, 25)
        self.clickAndWait(close_position, 1)
        self.clickAndWait(close_position, 5)
        self.clickAndWait(close_position_1_2, 5)
        self.clickAndWait(close_position_last_chance, 3)
        self.clickAndWait(close_position_last_chance, 3)
        self.clickAndWait(close_position_last_chance, 3)
        # self.clickAndWait(close_position_last_chance, 10)

        #============Lower the volume=====================
        # menu_position = (1132,173)
        # volume_1_position = (868,350) #(868,333)
        # volume_2_position = (868,382) #(868,369)
        # self.clickAndWait(menu_position,1)
        # self.clickAndWait(volume_1_position,1)
        # self.clickAndWait(volume_2_position,1)
        # self.clickAndWait(back_position,1)

        #============Open event view======================
        self.clickAndWait(event_position, 3)
        self.clickAndWait(close_position, 2)

        # self.choosePanel(4)

        #=======Set mouse to its final position===========
        # mouse.position = final_position
        mouse.position = final_position
        # mouse.position = (944, 829)
        # mouse.position = (1036, 829)

    def useMode(self, position, mode = Mode.BASIC):
        if(mode == Mode.BASIC):
            mouse.position = position
            mouse.click(self.button)
            time.sleep(self.delay)
        elif(mode == Mode.DATING_EVENT):
            self.clickAndWait(energy_position,1)
            self.clickAndWait(collect_energy_position,3)
            self.clickAndWait(close_dating_1,1)
            self.clickAndWait(close_dating_2,1)
        else:
            raise ValueError("Error in click mode")

    def runDatingMode(self, cpt, delta_time):
        try:
            if self.running and not self.done_clicking_for_dating:
                print("time {}".format(delta_time))

                self.useMode(final_position, Mode.DATING_EVENT)
                self.done_clicking_for_dating = True
                cpt -= 1
                print("Click #{}".format(cpt))
        except Exception as e:
            print(e)

        if(self.waiting_delay > sleep_mode and floor(delta_time)%(sleep_mode*60) == 0):
            mouse.move(3,3)

        if (self.running and delta_time >= self.waiting_delay):
            self.last_time_clicked = time.time()
            print(time.ctime())
            self.done_clicking_for_dating = False
            self.reloadAndLocate()

    def runBasicMode(self, cpt, delta_time):
        while self.running and cpt > 0 and delta_time >= self.waiting_delay:
            print("Click #{}".format(cpt))
            mouse.position = final_position
            try:
                self.useMode(final_position, Mode.BASIC)
            except Exception as e:
                print(e)

            cpt -= 1
            if cpt == 0:
                self.last_time_clicked = time.time()
                print(time.ctime())
                self.reloadAndLocate()

    def run(self):
        self.last_time_clicked = time.time()
        while self.program_running:
            time.sleep(0.1)
            #delta_time = time.time() - self.start_time
            delta_time_2 = time.time() - self.last_time_clicked

            cpt = times_clicking
            if(self.mode == Mode.BASIC):
                self.runBasicMode(cpt=cpt, delta_time=delta_time_2)
            elif(self.mode == Mode.DATING_EVENT):
                self.runDatingMode(cpt=cpt, delta_time=delta_time_2)

