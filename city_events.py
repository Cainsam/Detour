# City Events
import copy
import random

import dictonaries

# Global Variables

# Tells main where the dialogue is placed
x_pos = 10
top_pos = 10
pos1 = 400
pos2 = 450
pos3 = 500
pos4 = 550

# Controls the RGB values of text when hovered over and when not hovered over
dia_r = 200
dia_g = 200
dia_b = 200
dia_hov_r = 200
dia_hov_g = 0
dia_hov_b = 0

# Controls the if/than statements and tracks dialogue
cur_city = "first"

# Tells main what cities are connected to our current city
city_conn = ["Meat Export", "Lion Industries"]

# List of people riding in our car with us
passengers = []

# List of events currently happening
events = []

# List of events that have ended
event_archive = []

# Basic variable that need to be lists because of how pygame reads these functions every frame
random_num = []
city = ["null"]
car = ["color", "type"]

# Returns a simple random number between 1 and 4
def random_roll():
    roll = random.random()
    if roll < .25:
        return 1
    elif roll <  .5:
        return 2
    elif roll < .75:
        return 3
    else:
        return 4

# Controls the if-then options for in-game choices. Changes event by changing the city-name.
def city_event(city_name, select):
    # Color change code for mouse hovering over text
    # r g and b are the red, green and blue values for each line of text.
    if select == 0:
        r1 = r2 = r3 = r4 = dia_r
        g1 = g2 = g3 = g4 = dia_g
        b1 = b2 = b3 = b4 = dia_b
    elif select == 1:
        r2 = r3 = r4 = dia_r
        g2 = g3 = g4 = dia_g
        b2 = b3 = b4 = dia_b
        r1 = dia_hov_r
        g1 = dia_hov_g
        b1 = dia_hov_b
    elif select == 2:
        r1 = r3 = r4 = dia_r
        g1 = g3 = g4 = dia_g
        b1 = b3 = b4 = dia_b
        r2 = dia_hov_r
        g2 = dia_hov_g
        b2 = dia_hov_b
    elif select == 3:
        r1 = r2 = r4 = dia_r
        g1 = g2 = g4 = dia_g
        b1 = b2 = b4 = dia_b
        r3 = dia_hov_r
        g3 = dia_hov_g
        b3 = dia_hov_b
    elif select == 4:
        r1 = r2 = r3 = dia_r
        g1 = g2 = g3 = dia_g
        b1 = b2 = b3 = dia_b
        r4 = dia_hov_r
        g4 = dia_hov_g
        b4 = dia_hov_b

    # ___Game Introduction (Raven Events)___
    if city_name == "first":
        top = ["Another morning in Raven. It's still strange to see the sun in Cornelius Consumption.", 10, 10, 200, 200, 200]
        opt1 = ["A true morning in Cornelius Consumption. Never thought I'd live to see it.", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "firstopt3"
        choice2 = "first"
        choice3 = "first"
        choice4 = "first"
        end_flag = 0
    if city_name == "firstopt3":
        top = ["For most it's been 200 years since the sun started rising again. For you it's only been a few days", 10, 10, 200, 200, 200]
        opt1 = ["Why would Mystra send me here and now?", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "firstopt4"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
    if city_name == "firstopt4":
        top = ["You do know that Cornelius is still alive somewhere", 10, 10, 200, 200, 200]
        opt1 = ["Perhaps she sent me to take care of that", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "firsto5"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
    if city_name == "firsto5":
        top = ["Whatever the reason, it's time to summon your spirit car", 10, 10, 200, 200, 200]
        opt1 = ["I wonder what God and magic still exists to allow me to summon...", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "firsto6"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
    if city_name == "firsto6":
        top = ["What color is your spirit?", 10, 10, 200, 200, 200]
        opt1 = ["Red", x_pos, pos1, r1, g1, b1]
        opt2 = ["Blue", x_pos, pos2, r2, g2, b2]
        opt3 = ["Green", x_pos, pos3, r3, g3, b3]
        opt4 = ["Black", x_pos, pos4, r4, g4, b4]
        choice1 = "firstred"
        choice2 = "firstblue"
        choice3 = "firstgreen"
        choice4 = "firstblack"
        end_flag = 0
    if city_name == "firstred":
        if car[0] == "color":
            car[0] = "red"
        return city_event("firsto7", select)
    if city_name == "firstblue":
        if car[0] == "color":
            car[0] = "dark blue"
        return city_event("firsto7", select)
    if city_name == "firstgreen":
        if car[0] == "color":
            car[0] = "green"
        return city_event("firsto7", select)
    if city_name == "firstblack":
        if car[0] == "color":
            car[0] = "black"
        return city_event("firsto7", select)
    if city_name == "firsto7":
        top = ["That's right. And what type of vehicle does your spirit produce?", 10, 10, 200, 200, 200]
        opt1 = ["A simple sedan, for the humble soul", x_pos, pos1, r1, g1, b1]
        opt2 = ["A large truck, for the adventurous soul", x_pos, pos2, r2, g2, b2]
        opt3 = ["A sports car, for the flashy soul", x_pos, pos3, r3, g3, b3]
        opt4 = ["An SUV, for the practical soul", x_pos, pos4, r4, g4, b4]
        choice1 = "firstcar"
        choice2 = "firsttruck"
        choice3 = "firstsport"
        choice4 = "firstsuv"
        end_flag = 0
    if city_name == "firstcar":
        if car[1] == "type":
            car[1] = "honda accord car"
        return city_event("firsto8", select)
    if city_name == "firsttruck":
        if car[1] == "type":
            car[1] = "ford truck"
        return city_event("firsto8", select)
    if city_name == "firstsport":
        if car[1] == "type":
            car[1] = "sports car"
        return city_event("firsto8", select)
    if city_name == "firstsuv":
        if car[1] == "type":
            car[1] = "suv"
        return city_event("firsto8", select)
    if city_name == "firsto8":
        top = ["Here is your car:", 10, 10, 200, 200, 200]
        opt1 = ["Seems about right", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "first00"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 2
    if city_name == "first00":
        top = ["You are in Raven, you are driving elsewhere. Do you want to take Christine or Henry with you?", 10, 10, 200, 200, 200]
        opt1 = ["1. Christine", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. Henry", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "firstopt1"
        choice2 = "firstopt2"
        choice3 = "first"
        choice4 = "first"
        end_flag = 0
    if city_name == "firstopt1":
        top = ["Christine joins your car!", 10, 10, 200, 200, 200]
        opt1 = ["1. Great!", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Raven"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Christine" not in passengers:
            passengers.append("Christine")
    if city_name == "firstopt2":
        top = ["Henry joins your car!", 10, 10, 200, 200, 200]
        opt1 = ["1. Great!", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Raven"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Henry" not in passengers:
            passengers.append("Henry")
    if city_name == "Raven":
        top = ["Choose your destination..."]
        opt1 = ["1. Continue"]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Raven"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 1

    # ___Meat Export Events___
    if city_name == "Meat Export Event":
        top = ["You are at Meat Export.", 10, 10, 200,
           200, 200]
        opt1 = ["1. Nice", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. Cool", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Eventopt1"
        choice2 = "Meat Export Eventopt1"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        while random_num != []:
            random_num.pop()

    if city_name == "Meat Export Eventopt1":
        top = ["I hope you enjoyed your drive!", 10, 10, 200,
           200, 200]
        opt1 = ["1. I did", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. This seems more like a mimimum viable project than a full game...", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export"
        choice2 = "Meat Export"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export":
        while city_conn != []:
            city_conn.pop()
        for x in dictonaries.city_arr:
            if x["Name"] == "Meat Export":
                for i in x["Connections"]:
                    city_conn.append(i)
        top = ["I hope you enjoyed your drive!", 10, 10, 200,
           200, 200]
        opt1 = ["1. I did", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. This seems more like a mimimum viable project than a full game...", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export"
        choice2 = "Meat Export"
        choice3 = city_name
        choice4 = city_name
        end_flag = 1

    if city_name == "Meat Export Start":
        if city[0] != "Meat Export Start":
            city[0] = "Meat Export Start"
        if len(events) > 0:
            return city_event("Meat Export Event", select)
        elif len(random_num) < 1:
            random_num.append(random_roll())
        if random_num[0] <= 2:
            return city_event("Meat Export Random 1", select)
        else:
            return city_event("Meat Export Random 2", select)

    if city_name == "Meat Export Random 1":
        if "Christine Event" not in events and "Christine Event" not in event_archive and "Christine" in passengers:
                return city_event("Christine Event", select)
        elif "Henry Event" not in events and "Henry Event" not in event_archive and "Henry" in passengers:
                return city_event("Henry Event", select)
        else:
            while random_num != []:
                random_num.pop()
            return city_event("Meat Export Start", select)

    if city_name == "Meat Export Random 2":
        if "Henry Meat Export Event" not in events and "Henry Meat Export Event" not in event_archive and "Henry" in passengers:
                return city_event("Henry Meat Export Event", select)
        elif "Christine Meat Export Event" not in events and "Christine Meat Export Event" not in event_archive and "Christine" in passengers:
                return city_event("Christine Meat Export Event", select)
        else:
            while random_num != []:
                random_num.pop()
            return city_event("Meat Export Start", select)

    if city_name == "Henry Meat Export Event":
        top = ["Henry tells you he doesn't like Meat Export", 10, 10, 200,
               200, 200]
        opt1 = ["1. I don't care Henry", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. I do care Henry", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Henry Meat Export Eventopt1"
        choice2 = "Henry Meat Export Eventopt2"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Meat Export Eventopt1":
        top = ["Henry is not pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Whatevs", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Henry Meat Export Event" not in events:
            events.append("Henry Meat Export Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Henry":
                    person["Attitude"] -= 5
        while random_num != []:
            random_num.pop()

    if city_name == "Henry Meat Export Eventopt2":
        top = ["Henry is pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Nice", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Henry Meat Export Event" not in events:
            events.append("Henry Meat Export Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Henry":
                    person["Attitude"] += 5
        while random_num != []:
            random_num.pop()

    if city_name == "Christine Meat Export Event":
        top = ["Christine tells you she likes Meat Export", 10, 10, 200,
               200, 200]
        opt1 = ["1. I also like Meat Export", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. I do not care for Meat Export", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Christine Meat Export Eventopt1"
        choice2 = "Christine Meat Export Eventopt2"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Christine Meat Export Eventopt1":
        top = ["Christine is pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Cool", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Christine Meat Export Event" not in events:
            events.append("Christine Meat Export Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Christine":
                    person["Attitude"] += 5
        while random_num != []:
            random_num.pop()

    if city_name == "Christine Meat Export Eventopt2":
        top = ["Christine is not pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Bummer", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Christine Meat Export Event" not in events:
            events.append("Christine  Export Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Christine":
                    person["Attitude"] -= 5
        while random_num != []:
            random_num.pop()

    # ____Lion Industries Events___

    if city_name == "Lion Industries Event":
        top = ["You are at Lion Industries.", 10, 10, 200,
           200, 200]
        opt1 = ["1. Nice", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. Cool", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Lion Industries Eventopt1"
        choice2 = "Lion Industries Eventopt1"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        while random_num != []:
            random_num.pop()

    if city_name == "Lion Industries Eventopt1":
        top = ["I hope you enjoyed your drive!", 10, 10, 200,
           200, 200]
        opt1 = ["1. I did", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. This seems more like a mimimum viable project than a full game...", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Lion Industries"
        choice2 = "Lion Industries"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Lion Industries":
        while city_conn != []:
            city_conn.pop()
        for x in dictonaries.city_arr:
            if x["Name"] == "Lion Industries":
                for i in x["Connections"]:
                    city_conn.append(i)
        top = ["I hope you enjoyed your drive!", 10, 10, 200,
           200, 200]
        opt1 = ["1. I did", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. This seems more like a mimimum viable project than a full game...", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Lion Industries"
        choice2 = "Lion Industries"
        choice3 = city_name
        choice4 = city_name
        end_flag = 1

    if city_name == "Lion Industries Start":
        if city[0] != "Lion Industries Start":
            city[0] = "Lion Industries Start"
        if len(events) > 0:
            return city_event("Lion Industries Event", select)
        elif len(random_num) < 1:
            random_num.append(random_roll())
        if random_num[0] <= 2:
            return city_event("Lion Industries Random 1", select)
        else:
            return city_event("Lion Industries Random 2", select)

    if city_name == "Lion Industries Random 1":
        if "Christine Event" not in events and "Christine Event" not in event_archive and "Christine" in passengers:
                return city_event("Christine Event", select)
        elif "Henry Event" not in events and "Henry Event" not in event_archive and "Henry" in passengers:
                return city_event("Henry Event", select)
        else:
            while random_num != []:
                random_num.pop()
            return city_event("Lion Industries Start", select)

    if city_name == "Lion Industries Random 2":
        if "Henry Lion Industries Event" not in events and "Henry Lion Industries Event" not in event_archive and "Henry" in passengers:
                return city_event("Henry Lion Industries Event", select)
        elif "Christine Lion Industries Event" not in events and "Christine Lion Industries Event" not in event_archive and "Christine" in passengers:
                return city_event("Christine Lion Industries Event", select)
        else:
            while random_num != []:
                random_num.pop()
            return city_event("Lion Industries Start", select)

    if city_name == "Henry Lion Industries Event":
        top = ["Henry tells you he does like Lion Industries", 10, 10, 200,
               200, 200]
        opt1 = ["1. I agree Henry", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. I think you are stinky Henry", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Henry Lion Industries Eventopt1"
        choice2 = "Henry Lion Industries Eventopt2"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Lion Industries Eventopt1":
        top = ["Henry is pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Heck Yea!", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Lion Industries Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Henry Lion Industries Event" not in events:
            events.append("Henry Lion Industries Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Henry":
                    person["Attitude"] += 5
        while random_num != []:
            random_num.pop()

    if city_name == "Henry Lion Industries Eventopt2":
        top = ["Henry is not pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Like I even care", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Lion Industries Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Henry Lion Industries Event" not in events:
            events.append("Henry Lion Industries Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Henry":
                    person["Attitude"] -= 5
        while random_num != []:
            random_num.pop()

    if city_name == "Christine Lion Industries Event":
        top = ["Christine tells you she HATES Lion Industries", 10, 10, 200,
               200, 200]
        opt1 = ["1. I HATES Christine", x_pos, pos1, r1, g1, b1]
        opt2 = ["2. I do not care for Lion Industries either", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Christine Lion Industries Eventopt1"
        choice2 = "Christine Lion Industries Eventopt2"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Christine Lion Industries Eventopt1":
        top = ["Christine is NOT pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Whatevs", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Lion Industries Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Christine Lion Industries Event" not in events:
            events.append("Christine Lion Industries Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Christine":
                    person["Attitude"] -= 5
        while random_num != []:
            random_num.pop()

    if city_name == "Christine Lion Industries Eventopt2":
        top = ["Christine is pleased with your actions", 10, 10, 200,
               200, 200]
        opt1 = ["1. Woo hoo!", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Lion Industries Start"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Christine Lion Industries Event" not in events:
            events.append("Christine Lion Industries Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Christine":
                    person["Attitude"] += 5
        while random_num != []:
            random_num.pop()
    # ____Passenger Events___
    # These events can randomly happen if the passenger is in your car and traveling to any city.
    if city_name == "Christine Event":
        top = ["Christine tells you about her wild backstory", 10, 10, 200,
               200, 200]
        opt1 = ["1. What a wild backstory!", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Christine Eventopt1"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Christine Eventopt1":
        top = ["Christine confidently agrees", 10, 10, 200,
               200, 200]
        opt1 = ["1. Nice", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = city[0]
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Christine Event" not in events:
            events.append("Christine Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Christine":
                    person["Attitude"] += 3
        while random_num != []:
            random_num.pop()

    if city_name == "Henry Event":
        top = ["Henry talks about his life", 10, 10, 200,
               200, 200]
        opt1 = ["1. Sounds like quite the life!", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Henry Eventopt1"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Eventopt1":
        top = ["Henry bashfully agrees", 10, 10, 200,
               200, 200]
        opt1 = ["1. Nice", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = city[0]
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Henry Event" not in events:
            events.append("Henry Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Henry":
                    person["Attitude"] += 3
        while random_num != []:
            random_num.pop()

    if len(passengers) > 3:
        pass

    return [top, opt1, opt2, opt3, opt4, choice1, choice2, choice3, choice4, end_flag]
