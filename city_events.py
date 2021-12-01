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
            car[0] = "blue"
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
        top = ["Before you step in, you see a couple staring at your newly summoned car. The woman is holding a child.", 10, 10, 200, 200, 200]
        opt1 = ["I should probably stop summoning this thing in public places", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "first01"
        choice2 = "first"
        choice3 = "first"
        choice4 = "first"
        end_flag = 0
    if city_name == "first01":
        top = ["'I'm sorry...' says the husband, tall and slender, as elves tend to be.", 10, 10, 200, 200, 200]
        opt1 = ["continue", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "first02"
        choice2 = "first"
        choice3 = "first"
        choice4 = "first"
        end_flag = 0
    if city_name == "first02":
        top = ["Are you by chance heading in towards Tatst-E Cusine?", 10, 10, 200, 200, 200]
        opt1 = ["I will be passing through it yes", x_pos, pos1, r1, g1, b1]
        opt2 = ["You looking for a ride?", x_pos, pos2, r2, g2, b2]
        opt3 = ["I'm sorry, who are you?", x_pos, pos3, r3, g3, b3]
        opt4 = []
        choice1 = "first03"
        choice2 = "first03"
        choice3 = "first03"
        choice4 = "first"
        end_flag = 0
    if city_name == "first03":
        top = ["'I'm Henry, this is my wife Christine. We were... well one of us needs to...'", 10, 10, 200, 200, 200]
        opt1 = ["...", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "first04"
        choice2 = "first"
        choice3 = "first"
        choice4 = "first"
        end_flag = 0
    if city_name == "first04":
        top = ["'Our friend is sick' Christine finally broke off Henry's stammering. 'and he's all alone right now'", 10, 10, 200, 200, 200]
        opt1 = ["It's not the safest trip for a small child. And I won't be returning for a while", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "first05"
        choice2 = "first"
        choice3 = "first"
        choice4 = "first"
        end_flag = 0
    if city_name == "first05":
        top = ["'That's alright, one of us will stay with the child.' Christine explained ", 10, 10, 200, 200, 200]
        opt1 = ["Okay, well you sound pretty adamant Christine. Come on in", x_pos, pos1, r1, g1, b1]
        opt2 = ["Well Henry, you ready to go?", x_pos, pos2, r2, g2, b2]
        opt3 = ["Sure, which of you would rather go?", x_pos, pos3, r3, g3, b3]
        opt4 = []
        choice1 = "firstopt1"
        choice2 = "firstopt2"
        choice3 = "first06"
        choice4 = "first"
        end_flag = 0
    if city_name == "first06":
        top = ["'Doesn't matter' Henry said. Christine's a mechanic which might be helpful... I'm more of a book guy myself ", 10, 10, 200, 200, 200]
        opt1 = ["Could always use a mechanic. Hop in Christine", x_pos, pos1, r1, g1, b1]
        opt2 = ["A scholar sounds like decent company on the road. Come on in Henry", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "firstopt1"
        choice2 = "firstopt2"
        choice3 = "first"
        choice4 = "first"
        end_flag = 0
    if city_name == "firstopt1":
        top = ["Christine hands the baby over to Henry and goes to grab her things. Henry thanks you too many times.", 10, 10, 200, 200, 200]
        opt1 = ["Christine has joined your car!", x_pos, pos1, r1, g1, b1]
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
        top = ["'Okay!' Henry exclames 'Thank you so much! I'll just grab my things...'", 10, 10, 200, 200, 200]
        opt1 = ["Henry joins your car!", x_pos, pos1, r1, g1, b1]
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
        top = ["You finally pull into Meat Export, the massive array of defunct cube-shaped factories stretch across the horizon", 10, 10, 200,
           200, 200]
        opt1 = ["A reminder of what we accomplished when we overthrew the corrupt leaders of this land", x_pos, pos1, r1, g1, b1]
        opt2 = ["A reminder of the dead space that is left behind when a great power is dethroned", x_pos, pos2, r2, g2, b2]
        opt3 = ["A reminder of the couldn't support their families after the factories were shut down", x_pos, pos3, r3, g3, b3]
        opt4 = ["Trying to create symbolism from this is meaningless. We did what we had to, this is just the result.", x_pos, pos4, r4, g4, b4]
        choice1 = "Meat Export Event01"
        choice2 = "Meat Export Event01"
        choice3 = "Meat Export Event01"
        choice4 = "Meat Export Event01"
        end_flag = 0
        while random_num != []:
            random_num.pop()

    if city_name == "Meat Export Event01":
        top = ["You ask " + passengers[0] + " if they want to stop for a drink, they shrug and say 'either way'", 10, 10, 200,
           200, 200]
        opt1 = ["Stop for a drink", x_pos, pos1, r1, g1, b1]
        opt2 = ["Keep driving", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event02"
        choice2 = "Meat Export"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export Event01":
        top = ["You ask " + passengers[0] + " if they want to stop for a drink, they shrug and say 'either way'", 10, 10, 200,
           200, 200]
        opt1 = ["Stop for a drink", x_pos, pos1, r1, g1, b1]
        opt2 = ["Keep driving", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event02"
        choice2 = "Meat Export"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export Event02":
        top = ["You ask " + passengers[0] + " if they want to stop for a drink, they shrug and say 'either way'", 10, 10, 200,
           200, 200]
        opt1 = ["Stop for a drink", x_pos, pos1, r1, g1, b1]
        opt2 = ["Keep driving", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event04"
        choice2 = "Meat Export Event03"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export Event03":
        top = ["You've spent enough time here. It's time to move on", 10, 10, 200,
               200, 200]
        opt1 = ["Dark history here. Hopefully it gets better with time.", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export Event04":
        top = ["The first bar you see open is called 'The Meat Grinder'. Dim candle light becons you inside", 10, 10, 200,
               200, 200]
        opt1 = ["Probably best not to mention that the lack of electricity is my fault...", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event05"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export Event05":
        top = ["You and " + passengers[0] + " order a drink. You can't help but notice everyone staring at you.", 10, 10, 200,
               200, 200]
        opt1 = ["You're the only person left with a car. Probably all wondering how you got here.", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event06"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export Event06":
        top = ["An orc sitting at a nearby stool finally speaks up, 'why the hell are an elf and a human in Meet Export?'", 10, 10, 200,
               200, 200]
        opt1 = ["'Just passing through'", x_pos, pos1, r1, g1, b1]
        opt2 = ["(Stay silent)", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event07"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export Event07":
        top = ["'Last time strangers came to town, they went through our houses, took everything we had...' The orc stands up", 10, 10, 200,
               200, 200]
        opt1 = ["Prepare to defend yourself...", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        if passengers[0] == "Henry":
            for person in dictonaries.pass_arr:
                if person["Name"] == "Henry":
                    if person["Attitude"] >= 0:
                        choice1 = "Meat Export EventHenry+"
                    else:
                        choice1 = "Meat Export EventHenry-"
        else:
            choice1 = "Meat Export EventChristine1"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export EventHenry+":
        top = ["Henry speaks up, 'My friend and I aren't those strangers. I was here for the union wars. On your side.'", 10, 10, 200,
               200, 200]
        opt1 = ["Henry seems more confident than usual", x_pos, pos1, r1, g1, b1]
        opt2 = ["It's nice that he called me friend", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export EventHenry+1"
        choice2 = "Meat Export EventHenry+1"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export EventHenry+1":
        top = ["The Orc nods and backs down. 'Sorry, we have to be slow to trust now. You understand...'", 10, 10, 200,
               200, 200]
        opt1 = ["50 years ago you and your family took Cornelius' crystal, taking his power away", x_pos, pos1, r1, g1, b1]
        opt2 = ["At the time it seemed like the only right thing to do. It was the heist of the century", x_pos, pos2, r2, g2, b2]
        opt3 = ["One of many heists of the century for your family. You hope they got sent back as well...", x_pos, pos3, r3, g3, b3]
        opt4 = ["Taking his power freed the workers... but also left them with nothing. You stay silent about it all.", x_pos, pos4, r4, g4, b4]
        choice1 = "Meat Export EventHenry+2"
        choice2 = "Meat Export EventHenry+2"
        choice3 = "Meat Export EventHenry+2"
        choice4 = "Meat Export EventHenry+2"
        end_flag = 0

    if city_name == "Meat Export EventHenry+2":
        top = ["You drink in silence and leave. Henry seems sorrowful, but strangely at peace", 10, 10, 200,
               200, 200]
        opt1 = ["Glad to have him along for the ride", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event03"
        choice2 = "Meat Export EventHenry+2"
        choice3 = "Meat Export EventHenry+2"
        choice4 = "Meat Export EventHenry+2"
        end_flag = 0

    if city_name == "Meat Export EventHenry-":
        top = ["Henry speaks up, 'I was here for the union wars, I fought for the workers here.'", 10, 10, 200,
               200, 200]
        opt1 = ["Henry seems more confident than usual", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export EventHenry-1"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export EventHenry-1":
        top = ["'And your friend?' asks the Orc. 'Not my friend... but not your enemy' Henry replies", 10, 10, 200,
               200, 200]
        opt1 = ["Kind of cold...", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export EventHenry-2"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export EventHenry-2":
        top = ["The Orc nods and backs down. 'Sorry, we have to be slow to trust now. You understand...'", 10, 10, 200,
               200, 200]
        opt1 = ["50 years ago you and your family took Cornelius' crystal, taking his power away", x_pos, pos1, r1, g1, b1]
        opt2 = ["At the time it seemed like the only right thing to do. It was the heist of the century", x_pos, pos2, r2, g2, b2]
        opt3 = ["One of many heists of the century for your family. You hope they got sent back as well...", x_pos, pos3, r3, g3, b3]
        opt4 = ["Taking his power freed the workers... but also left them with nothing. You stay silent about it all.", x_pos, pos4, r4, g4, b4]
        choice1 = "Meat Export EventHenry-3"
        choice2 = "Meat Export EventHenry-3"
        choice3 = "Meat Export EventHenry-3"
        choice4 = "Meat Export EventHenry-3"
        end_flag = 0

    if city_name == "Meat Export EventHenry-3":
        top = ["You drink in silence and leave. Henry avoids eye contact.", 10, 10, 200,
               200, 200]
        opt1 = ["You do the same", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Event03"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export EventChristine1":
        top = ["'Fuck off.' Snaps Christine 'We aren't thieves, and we don't want your shit'", 10, 10, 200,
               200, 200]
        opt1 = ["You were quite a good thief actually, but best not to mention that now", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export EventChristine2"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export EventChristine2":
        top = ["The Orc stands up. So does Christine. So do the rest of the patrons", 10, 10, 200,
               200, 200]
        opt1 = ["'By the connected powers and the soul of the city...'", x_pos, pos1, r1, g1, b1]
        opt2 = []
        opt3 = []
        opt4 = []
        choice1 = "Meat Export EventChristine3"
        choice2 = city_name
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export EventChristine3":
        top = ["You finish casting your spell right as its about to come to blows. The patrons stand, frozen in time.", 10, 10, 200,
               200, 200]
        opt1 = ["50 years ago you and your family took Cornelius' crystal, taking his power away", x_pos, pos1, r1, g1, b1]
        opt2 = ["At the time it seemed like the only right thing to do. It was the heist of the century", x_pos, pos2, r2, g2, b2]
        opt3 = ["One of many heists of the century for your family. You hope they got sent back as well...", x_pos, pos3, r3, g3, b3]
        opt4 = ["Taking his power freed the workers... but also left them with nothing. Frozen in time.", x_pos, pos4, r4, g4, b4]
        choice1 = "Meat Export EventChristine4"
        choice2 = "Meat Export EventChristine4"
        choice3 = "Meat Export EventChristine4"
        choice4 = "Meat Export EventChristine4"
        end_flag = 0

    if city_name == "Meat Export EventChristine4":
        top = ["'Sorry...' says Christine. 'It's been a stressful few days'", 10, 10, 200,
               200, 200]
        opt1 = ["'It's alright, let's just leave before the spell wears off'", x_pos, pos1, r1, g1, b1]
        opt2 = ["'These people have been beaten enough. Let's not add to it now'", x_pos, pos2, r2, g2, b2]
        opt3 = ["'Lets just go'", x_pos, pos3, r3, g3, b3]
        opt4 = []
        choice1 = "Meat Export Event03"
        choice2 = "Meat Export Event03"
        choice3 = "Meat Export Event03"
        choice4 = city_name
        end_flag = 0

    if city_name == "Meat Export":
        while city_conn != []:
            city_conn.pop()
        for x in dictonaries.city_arr:
            if x["Name"] == "Meat Export":
                for i in x["Connections"]:
                    city_conn.append(i)
        top = ["You've spent enough time here. It's time to move on", 10, 10, 200,
           200, 200]
        opt1 = ["Dark history here. Hopefully it gets better with time.", x_pos, pos1, r1, g1, b1]
        opt2 = []
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
        top = ["After driving in silence for a while, Henry breaks the silence. 'Why go through Meat Export?'", 10, 10, 200,
               200, 200]
        opt1 = ["I want to see how the factories look since they've stopped running", x_pos, pos1, r1, g1, b1]
        opt2 = ["Honestly, I think the name is funny", x_pos, pos2, r2, g2, b2]
        opt3 = ["Had to choose somewhere I guess", x_pos, pos3, r3, g3, b3]
        opt4 = []
        choice1 = "Henry Meat Export Event01"
        choice2 = "Henry Meat Export Event01"
        choice3 = "Henry Meat Export Event01"
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Meat Export Event01":
        top = ["'Ugly place' Henry says. 'Glad it's gone now'", 10, 10, 200,
               200, 200]
        opt1 = ["Me and my family were actually the ones who shut the place down", x_pos, pos1, r1, g1, b1]
        opt2 = ["I wouldn't call myself a fan either, but now we have no industry... was it worth it?", x_pos, pos2, r2, g2, b2]
        opt3 = ["There were good people here, but they worked under a monster.", x_pos, pos3, r3, g3, b3]
        opt4 = ["Hard to believe we were all eating ground up Goblins for years and somehow no one noticed", x_pos, pos4, r4, g4, b4]
        choice1 = "Henry Meat Export Event02"
        choice2 = "Henry Meat Export Event03"
        choice3 = "Henry Meat Export Event04"
        choice4 = "Henry Meat Export Event04"
        end_flag = 0

    if city_name == "Henry Meat Export Event02":
        top = ["Henry smiles 'I had a hunch it was you. Not many people know how summon a " + car[0] + " spirit car'", 10, 10, 200,
               200, 200]
        opt1 = ["I think I may have been sent back here to finish off Cornelius", x_pos, pos1, r1, g1, b1]
        opt2 = ["Keep this a secret okay? I don't want people knowing who I am", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Henry Meat Export Event05"
        choice2 = "Henry Meat Export Event05"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Meat Export Event03":
        top = ["Henry doesn't even look at you. 'yes. It is.'", 10, 10, 200,
               200, 200]
        opt1 = ["You sit in silence for a long while", x_pos, pos1, r1, g1, b1]
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

    if city_name == "Henry Meat Export Event04":
        top = ["I used to live out here. Lots of friends died in those factories. Glad it's over now'", 10, 10, 200,
               200, 200]
        opt1 = ["Me too", x_pos, pos1, r1, g1, b1]
        opt2 = ["you know... it was actually me an my family who took down Cornelius", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Start"
        choice2 = "Henry Meat Export Event02"
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

    if city_name == "Henry Meat Export Event05":
        top = ["I didn't realize I was riding with a legend' Henry smiles 'your secret is safe with me'", 10, 10, 200,
               200, 200]
        opt1 = ["Thanks Henry", x_pos, pos1, r1, g1, b1]
        opt2 = ["(silently keep driving)", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Meat Export Start"
        choice2 = "Meat Export Start"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0
        if "Henry Meat Export Event" not in events:
            events.append("Henry Meat Export Event")
            for person in dictonaries.pass_arr:
                if person["Name"] == "Henry":
                    person["Attitude"] += 10
        while random_num != []:
            random_num.pop()

    if city_name == "Christine Meat Export Event":
        top = ["On your way to Meet Export, Christine asks if your radio works", 10, 10, 200,
               200, 200]
        opt1 = ["Sorry, I can't focus with music on", x_pos, pos1, r1, g1, b1]
        opt2 = ["Yeah, but since it's soul car, it only plays music that gels with my current mood", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Christine Meat Export Eventopt1"
        choice2 = "Christine Meat Export Eventopt2"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Christine Meat Export Eventopt1":
        top = ["'Hmm. Lame' Is the last thing Christine says for the rest of the drive", 10, 10, 200,
               200, 200]
        opt1 = ["Awkward...", x_pos, pos1, r1, g1, b1]
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
                    person["Attitude"] -= 5
        while random_num != []:
            random_num.pop()

    if city_name == "Christine Meat Export Eventopt2":
        top = ["Ohh, mind if we give it a go?", 10, 10, 200,
               200, 200]
        opt1 = ["Sure", x_pos, pos1, r1, g1, b1]
        opt2 = ["Absolutly not", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Christine Meat Export Eventopt1"
        choice2 = "Christine Meat Export Eventopt3"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Christine Meat Export Eventopt3":
        top = ["Sorry, I fogot... what's your soul music again?", 10, 10, 200,
                200, 200]
        opt1 = ["Rock", x_pos, pos1, r1, g1, b1]
        opt2 = ["Country", x_pos, pos2, r2, g2, b2]
        opt3 = ["Techno", x_pos, pos3, r3, g3, b3]
        opt4 = ["Soft men mumbling about their problems", x_pos, pos4, r4, g4, b4]
        choice1 = "Christine Meat Export Eventopt4"
        choice2 = "Christine Meat Export Eventopt4"
        choice3 = "Christine Meat Export Eventopt4"
        choice4 = "Christine Meat Export Eventopt4"
        end_flag = 0

    if city_name == "Christine Meat Export Eventopt4":
        top = ["'Huh... not usually my thing, but kinda fitting for a dark lonely place like Meet Export'", 10, 10, 200,
                200, 200]
        opt1 = ["You and Christine Jam the rest of the ride", x_pos, pos1, r1, g1, b1]
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
                    person["Attitude"] += 5
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
        top = ["Part way though the trip, your car starts to sputter a bit. Christine suggest she could take a look at it", 10, 10, 200,
               200, 200]
        opt1 = ["'I appreciate it, but this is a spirit car... I'm just a bit stressed'", x_pos, pos1, r1, g1, b1]
        opt2 = ["'This thing runs on magic and feelings unfortunately, not much a wrench could do.'", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Christine Event01"
        choice2 = "Christine Event01"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Christine Event01":
        top = ["'That would explain why your the only one left with a functioning car. Why'd you bring the mechanic along then?'", 10, 10, 200,
               200, 200]
        opt1 = ["'No offense to your husband, but I wanted someone who could handle any disagreements we have on the road'", x_pos, pos1, r1, g1, b1]
        opt2 = ["'Just kind of chose randomly to be honest'", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Christine Eventopt1"
        choice2 = "Christine Eventopt2"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Christine Eventopt1":
        top = ["Christine laughs 'Love the guy... but good choice'", 10, 10, 200,
               200, 200]
        opt1 = ["You exchange witty banter for the rest of the drive", x_pos, pos1, r1, g1, b1]
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
                    person["Attitude"] += 5
        while random_num != []:
            random_num.pop()

    if city_name == "Christine Eventopt2":
        top = ["'Hmm. Guess that makes sense.'", 10, 10, 200,
               200, 200]
        opt1 = ["The conversation drops and you ride in silence", x_pos, pos1, r1, g1, b1]
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
                    person["Attitude"] -= 5
        while random_num != []:
            random_num.pop()

    if city_name == "Henry Event":
        top = ["After a bit of driving, Henry asks, 'You won't be coming back to Raven soon by chance will you?'", 10, 10, 200,
               200, 200]
        opt1 = ["'Maybe in a while, need a ride back?'", x_pos, pos1, r1, g1, b1]
        opt2 = ["Gotta take care of some things in the capital, but maybe after", x_pos, pos2, r2, g2, b2]
        opt3 = ["Wasn't really planning on it, no", x_pos, pos3, r3, g3, b3]
        opt4 = []
        choice1 = "Henry Eventopt1"
        choice2 = "Henry Eventopt1"
        choice3 = "Henry Eventopt2"
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Eventopt1":
        top = ["I mean go where you need to go first, but it was a desperate situation... never really planed the return trip", 10, 10, 200,
               200, 200]
        opt1 = ["I can pick you up on the way back", x_pos, pos1, r1, g1, b1]
        opt2 = ["I'm not sure where I'll be... no promises", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Henry Eventopt3"
        choice2 = "Henry Eventopt4"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Eventopt2":
        top = ["'Look I hate to ask but... I don't really have a plan for getting back... could you... maybe...'",10, 10, 200, 200, 200]
        opt1 = ["I should have time after I make it to the capital", x_pos, pos1, r1, g1, b1]
        opt2 = ["Sorry... I wish I could help but I don't want to make promises I can't keep", x_pos, pos2, r2, g2, b2]
        opt3 = []
        opt4 = []
        choice1 = "Henry Eventopt3"
        choice2 = "Henry Eventopt4"
        choice3 = city_name
        choice4 = city_name
        end_flag = 0

    if city_name == "Henry Eventopt3":
        top = ["'I'll hold you to that.' Henry smiles.",10, 10, 200, 200, 200]
        opt1 = ["Gotta remember to come back after our trip...", x_pos, pos1, r1, g1, b1]
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
                    person["Attitude"] += 5
        while random_num != []:
            random_num.pop()

    if city_name == "Henry Eventopt4":
        top = ["'Oh. It's okay... we'll... we'll figure something out...'",10, 10, 200, 200, 200]
        opt1 = ["You want to help... but there are bigger fish to fry", x_pos, pos1, r1, g1, b1]
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
                    person["Attitude"] -= 5
        while random_num != []:
            random_num.pop()


    return [top, opt1, opt2, opt3, opt4, choice1, choice2, choice3, choice4, end_flag]
