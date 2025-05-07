init python:
    def reset_hanako_death_flag():
        persistent.hanako_dead = False
        
define h = Character("Hanako", color="#e5762c")

# 初始化状态
default affection = 0.0
default health = 0.0
default mystery = 0.0

default day = 1

default has_fed_cockroach = False
default fed_unknown = False

default first_day_food = ""
default second_day_food = ""
default final_cockroach = False
default day2_mystery_hint_shown = False

# Hanako 表情图像定义
image hanako idle = Transform("images/hanako_idle.png", zoom=0.5, xalign=0.5, yalign=0.5)
image hanako chill = Transform("images/hanako_chill.png", zoom=0.5, xalign=0.5, yalign=0.5)
image hanako happy = Transform("images/hanako_happy.png", zoom=0.5, xalign=0.5, yalign=0.26)
image hanako confused = Transform("images/hanako_confused.png", zoom=0.5, xalign=0.5, yalign=0.64)
image hanako scared = Transform("images/hanako_scared.png", zoom=0.5, xalign=0.9, yalign=0.9)
image hanako active = Transform("images/hanako_active.png", zoom=0.5, xalign=0.5, yalign=0.3)
image hanako sick = Transform("images/hanako_sick.png", zoom=0.5, xalign=0.5, yalign=0.75)
image big hanako chill = Transform("images/hanako_chill.png", zoom=0.8, xalign=0.5, yalign=0.4)
image big hanako happy = Transform("images/hanako_happy.png", zoom=0.8, xalign=0.5, yalign=0.3)
image gigantic hanako sick = Transform("images/hanako_sick.png", zoom=4.75, xalign=0.36, yalign=0.53)
image bg_pixel_aquarium = Transform("images/bg.png", fit="cover")

label before_main_menu:
    scene bg_pixel_aquarium

    if persistent.hanako_dead:
        play music "audio/love_question.ogg" fadein 0.5  # 如果Hanako曾死亡，播放死亡BGM
    else:
        play music "audio/i_love_you.ogg" fadein 0.5  # 正常BGM

    return

label start:
    stop music fadeout 1.0

    scene bg_pixel_aquarium
    show hanako idle

    play music "audio/im_hungy.ogg" 

    "You have adopted a small goldfish named Hanako."
    jump day1

label day1:
    scene bg_pixel_aquarium
    show hanako idle
    "Day 1"
    h "I'm hungy... ><"

    menu:
        "Fish Food":
            $ affection += 1.5
            $ health += 2
            $ first_day_food = "fish"
            h "Fish food! It'll help Hanako grow strong and healthy. ^^"
            show hanako chill
            "Hanako floats calmly in the water."
            jump after_day1

        "Peach":
            $ affection += 3
            $ first_day_food = "peach"
            h "Peach!! How did you know that's Hanako's favorite? You're the best! ><"
            show hanako happy
            "Hanako swims joyfully around the tank."
            jump after_day1

        "Unknown Object":
            $ health -= 1
            $ mystery += 2
            $ fed_unknown = True
            $ first_day_food = "unknown"
            h "...?"
            show hanako confused
            "Hanako looks puzzled."
            jump after_day1

label after_day1:
    h "Goodnight... See you tomorrow."
    $ day = 2
    jump day2

label day2:
    scene bg_pixel_aquarium
    show hanako idle
    "Day 2"


    
    h "I'm hungy again... What's on the menu today? ><"

    if first_day_food == "unknown" and not day2_mystery_hint_shown:
        "She tilts her head... as if waiting for your reaction."
        $ day2_mystery_hint_shown = True

    menu:
        "Fish Food":
            $ affection += 1.5
            $ health += 2
            $ second_day_food = "fish"
            h "Fish food! It'll help Hanako grow strong and healthy. ^^"
            show hanako chill
            if first_day_food == "fish":
                "Hanako floats calmly in the water. She seems... chubbier?"
            else:
                "Hanako floats calmly in the water."
            jump after_day2

        "Peach":
            $ affection += 3
            $ second_day_food = "peach"
            h "Peach!! How did you know that's Hanako's favorite? You're the best! ><"
            show hanako happy
            "Hanako swims joyfully around the tank."
            jump after_day2

        "Unknown Object" if not fed_unknown:
            $ health -= 1
            $ mystery += 2
            $ fed_unknown = True
            $ second_day_food = "unknown"
            h "...?"
            show hanako confused
            "Hanako seems more confused."
            jump after_day2

        "Cockroach" if fed_unknown:
            $ mystery += 3
            $ affection -= 5
            $ health -= 5
            $ second_day_food = "cockroach"
            if has_fed_cockroach:
                $ final_cockroach = True
                h "..................."
                "You filled the tank with cockroaches."
            else:
                $ has_fed_cockroach = True
                h "!!!!???"
                show hanako scared
                "The cockroach flails in the water. Hanako hides in the corner, terrified."
            jump after_day2

label after_day2:
    if affection < 3:
        "Hanako ignores your goodbye."
    elif abs(affection - 3.0) < 0.1:
        "Hanako blows bubbles at you slowly."
    else:
        "Hanako swims to the glass and gazes at you as you leave."

    $ day = 3
    jump day3

label day3:
    scene bg_pixel_aquarium

    if first_day_food == "unknown" and second_day_food == "cockroach":
        play music "audio/Pain.ogg"
        "Day 3"
        show hanako sick
        "Hanako looks ill and weak."
        "What will you feed Hanako today?"

        menu:
            "Cockroach":
                stop music
                $ final_cockroach = True
                $ affection -= 5
                $ health -= 5
                h "..................."
                "You filled the tank with cockroaches."
                play music "audio/so_much_pain.ogg"
                jump ending

    else:
        "Day 3"

        if health < 0:
            show hanako sick
            "Hanako looks ill and weak."
        elif health == 0:
            show hanako chill
            "Hanako floats calmly in the tank."
        else:
            show hanako active
            "Hanako is energetic and full of life."

        "What will you feed Hanako today?"

        if final_cockroach:
            menu:
                "Cockroach":
                    $ final_cockroach = True
                    $ affection -= 5
                    $ health -= 5
                    h "..................."
                    "You filled the tank with cockroaches."
                    jump ending

        elif fed_unknown:
            menu:
                "Medicine":
                    $ health = 0
                    h "Thank you... I feel much better now."
                    jump ending

                "Cockroach":
                    $ mystery += 3
                    $ affection -= 5
                    $ health -= 5
                    if has_fed_cockroach:
                        $ final_cockroach = True
                        h "..................."
                        "You filled the tank with cockroaches."
                    else:
                        h "!!!!???"
                        show hanako scared
                        "The cockroach flails in the water. Hanako hides in the corner, terrified."
                    jump ending

        else:
            menu:
                "Deluxe Feast":
                    stop music
                    $ affection += 2
                    $ health += 6
                    h "...Wow!"
                    "Hanako's tummy becomes adorably round."
                    jump ending

                "Heart Meal":
                    $ affection += 6
                    h "All of Hanako's favorite things!! Yippeee!!!! ><"
                    jump ending


label ending:
    if final_cockroach:
        hide hanako
        show gigantic hanako sick
        $ persistent.hanako_dead = True   # ✅ 记录死亡状态
        "ENDING: ??? Death - You filled the tank with cockroaches. Hanako died."
    elif affection < 0 and health < 0 and mystery >= 5:
        stop music
        play music "audio/why_depression.ogg" fadein 0.5
        hide hanako
        show hanako confused
        "ENDING: Depression - Hanako whispers: 'You weren't like this at first... why?'"
    elif affection < 5 and health == 0:
        hide hanako
        show hanako idle
        "ENDING: Peaceful Life - You and Hanako continue your days as usual."
        "She gently blows bubbles at you through the glass."
    elif abs(affection - 5.0) < 0.1 and health > 5:
        hide hanako
        show big hanako chill
        play music "audio/hehe.ogg"
        "ENDING: So Fat! - You overfed Hanako into a round fish."
        "She happily floats with a full belly, not a care in the world."
    elif affection > 5 and health > 5:
        hide hanako
        show big hanako happy
        play music "audio/yippee_love_me_forever.ogg"
        "ENDING: Love Me Forever!? - You spoiled Hanako so much she became a chubby tyrant."
        "She bumps against the glass with pride, demanding attention."
        "But she's just too cute."
    elif affection > 5 and health < 5:
        stop music
        play music "audio/goldfish_love_dance.ogg"
        hide hanako
        show hanako active
        "ENDING: I Like You--!! - Hanako has grown very attached to you."
        "She often plays dead just to see if you'll worry."
        
    else:
        hide hanako
        "ENDING: The Glitch Fish - You've uncovered a combination that shouldn't exist."
        "Hanako looks at you... and winks."

    return
