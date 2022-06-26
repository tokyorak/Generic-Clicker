import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from enum import Enum
from math import floor
from Option import Mode, Option



class ClickMouse(threading.Thread):

    # _click_cost = click_cost

    def __init__(self, options, mouse_controller):
        super().__init__()
        self.options = options
        self.delay = self.options.delay
        self.button = self.options.left_button
        self.running = False    # Check if autoclick is ON2
        self.program_running = True # Check if the script is on
        self.start_time = time.time()
        self.waiting_delay = self.options.waiting_delay
        self.spamcoordinates = (0, 0)
        self.mode = self.options.click_mode
        self.last_time_clicked = self.start_time
        self.done_clicking_for_dating = False
        self.click_cost = self.options.click_cost
        self.mouse = mouse_controller


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
        print("Position: {}".format(self.mouse.position))
        self.spamcoordinates = self.mouse.position


    def clickAndWait(self, position, delay, message=''):
        print("click on : [", message, "]... and wait for ", delay ,"s")
        self.mouse.position = (position[0] + self.options.offset, position[1])
        time.sleep(0.5)
        self.mouse.click(self.button)
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
        self.clickAndWait(coordinates, 4, "Panel phase" + phase)


    def test(self):
        print("Test en cours...")
        self.clickAndWait(self.options.enter_position, 25,"Enter Pos")
        self.clickAndWait(self.options.close_position, 1,"Close Pos")
        self.clickAndWait(self.options.close_position, 5,"Close Pos")
        self.clickAndWait(self.options.close_position_1_2, 5,"Close Pos 1_2")
        self.clickAndWait(self.options.close_position_last_chance, 3,"Close Pos Last chance")
        self.clickAndWait(self.options.close_position_last_chance, 3,"Close Pos Last chance")

        print("Test en cours...Menu")
        self.options.menu_position = (1132,173)

        print("Test en cours...Volume")
        # self.options.volume_1_position = (868,350) #(868,333)
        # self.options.volume_2_position = (868,382) #(868,369)
        self.clickAndWait(self.options.menu_position,1,"Menu Pos")
        self.clickAndWait(self.options.volume_1_position,1,"Volume Pos 1")
        self.clickAndWait(self.options.volume_2_position,1,"Volume Pos 2")
        self.clickAndWait(self.options.back_position,1,"Back Pos")

        print("Test en cours...Event")
        #============Open event view======================
        self.clickAndWait(self.options.event_position, 3,"Event Pos")
        self.clickAndWait(self.options.close_position, 2,"Close Pos")

        print("Test en cours...Dating")
        self.clickAndWait(self.options.energy_position,1,"Energy Pos")
        self.clickAndWait(self.options.collect_energy_position,3,"Collect Energy Pos")
        self.clickAndWait(self.options.close_dating_1,1,"Close Dating 1 Pos")
        self.clickAndWait(self.options.close_dating_2,1,"Close Dating 2 Pos")
        print("Test terminé.")


    def test2(self):
        print("Test2 en cours...")
        self.enter_in_game()

        print("Test en cours...Menu + Volume")
        self.lower_volume()

        print("Test en cours...Event")
        self.open_event_view()

        print("Test en cours...Dating")
        self.collect_dating_energy()
        print("Test terminé.") 


    def raise_basic_gauge(self, position):
        self.mouse.position = position
        self.mouse.click(self.button)
        time.sleep(self.delay)


    def collect_dating_energy(self):
        self.clickAndWait(self.options.energy_position,1,"Energy Pos")
        self.clickAndWait(self.options.collect_energy_position,3,"Collect Energy Pos")
        self.clickAndWait(self.options.close_dating_1,1,"Close Dating 1 Pos")
        self.clickAndWait(self.options.close_dating_2,1,"Close Dating 2 Pos")


    def open_event_view(self):
        self.clickAndWait(self.options.event_position, 3,"Event Pos")
        self.clickAndWait(self.options.close_position, 2,"Close Pos")


    def lower_volume(self):
        # self.options.menu_position = (1132,173)
        # self.options.volume_1_position = (868,350) #(868,333)
        # self.options.volume_2_position = (868,382) #(868,369)
        self.clickAndWait(self.options.menu_position,1,"Menu Pos")
        self.clickAndWait(self.options.volume_1_position,1,"Volume Pos 1")
        self.clickAndWait(self.options.volume_2_position,1,"Volume Pos 2")
        self.clickAndWait(self.options.back_position,1,"Back Pos")


    def enter_in_game(self):
        print("Enters in the game..")
        self.clickAndWait(self.options.enter_position, 25,"Enter Pos")
        self.clickAndWait(self.options.close_position, 1,"Close Pos")
        self.clickAndWait(self.options.close_position, 5,"Close Pos")
        self.clickAndWait(self.options.close_position_1_2, 5,"Close Pos 1_2")
        self.clickAndWait(self.options.close_position_last_chance, 3,"Close Pos Last chance")
        self.clickAndWait(self.options.close_position_last_chance, 3,"Close Pos Last chance")   


    def reloadAndLocate(self):
        print("Reload time at {}".format(time.ctime()))
        #============Go back to home screen==================
        self.clickAndWait(self.options.back_position, 3,"Back Pos")
        self.clickAndWait(self.options.back_position, 1,"Back Pos")

        #============Reload the tab and close ads============
        self.clickAndWait(self.options.reload_position, 1,"Reload Pos")
        
        self.clickAndWait(self.options.confirm_reload_position, 125,"Confirm Reload Pos")

        self.enter_in_game()

        #============Lower the volume=====================
        # self.lower_volume()

        #============Open event view======================
        self.open_event_view()

        # self.choosePanel(4)

        #=======Set mouse to its final position===========
        self.mouse.position = self.options.final_position
        # self.mouse.position = (944, 829)
        # self.mouse.position = (1036, 829)


    def useMode(self, position, mode = Mode.BASIC):
        if(mode == Mode.BASIC):
            self.raise_basic_gauge(position)
        elif(mode == Mode.DATING_EVENT):
            self.collect_dating_energy()
        else:
            raise ValueError("Error in click mode")


    def runDatingMode(self, cpt, delta_time):
        try:
            if self.running and not self.done_clicking_for_dating:
                print("time {}".format(delta_time))

                self.useMode(self.options.final_position, Mode.DATING_EVENT)
                self.done_clicking_for_dating = True
                cpt -= 1
                print("Click #{}".format(cpt))
        except Exception as e:
            print(e)

        if(self.waiting_delay > self.options.sleep_mode and floor(delta_time)%(self.options.sleep_mode*60) == 0):
            self.mouse.move(3,3)

        if (self.running and delta_time >= self.waiting_delay):
            self.last_time_clicked = time.time()
            print(time.ctime())
            self.done_clicking_for_dating = False
            self.reloadAndLocate()


    def runBasicMode(self, cpt, delta_time):
        while self.running and cpt > 0 and delta_time >= self.waiting_delay:
            print("Click #{}".format(cpt))
            self.mouse.position = self.options.final_position
            try:
                self.useMode(self.options.final_position, Mode.BASIC)
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

            cpt = self.options.times_clicking
            if(self.mode == Mode.BASIC):
                self.runBasicMode(cpt=cpt, delta_time=delta_time_2)
            elif(self.mode == Mode.DATING_EVENT):
                self.runDatingMode(cpt=cpt, delta_time=delta_time_2)

