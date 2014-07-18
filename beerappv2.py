#Beer App


print "Seems like you arrived at the right spot. What's your favorite beer?"
beer_type = raw_input("Write Beer Here:")
beer_color = raw_input("Write Beer Color:")

print "Cool, you're drinking a %r with a %r color." %(beer_type, beer_color)


from sys import exit

def start():
    print """Too tired to go out on the town,
    and want to just sit in front of your computer, 
    but still live up those great downtown moments?
    Well, let's get this party started!

    Print 'YOLO!' to let me know you have a pulse. """

    next = raw_input("> ")

    if next == "YOLO!":
        bar()
    else:
        encourage()

def encourage():
    print """I'm still waiting to see you type those 4 magic letters,
    with an exclamation mark! :D"""

    next = raw_input("> ")

    if next == "YOLO!":
        bar()
    else:
        encourage()

def bar():
    print """Karamba! Let's do this!! 
    Now, we've walked for a while,
    and we finally arrived at a sweet bar! 
    This bar has a good selection of 4 types of beers.
    Choose one of the following: 
    'ale', 'ipa', 'hef', and 'jb' """

    next = raw_input("> ")
    
    if next == "ale":
        ale()
    elif next == "ipa":
        ipa()
    elif next == "hef":
        hef()
    elif next == "jb":
        jon()
    else:
        boring()

#bar()   <- doesn't work here. Must be at bottom.

def ale():
    print "Good choice mate! Which beer did you choose?"

    next = raw_input("> ")

    if next == "brown ale":
        rating()
    elif next == "golden ale":
        rating()
    else: 
        boring()

def hef():
    print "Guten TAAAAG!!! Which type of hef did you choose?"
    next = raw_input("> ")

    if "hef 1" in next:
        rating()
    elif "hef 2" in next:
        rating()
    else: 
        hef()

def ipa():
    print "Excellent! Which refresher did you choose?"
    next = raw_input("> ")

    if "ipa 1" in next:
        rating()
    elif "ipa 2" in next:
        rating()
    else: 
        ipa()

def jon():
    print "RIGHTEOUS!!! Which one did you choose?"
    next = raw_input("> ")

    if "jon 1" in next:
        rating()
    elif "jon 2" in next:
        rating()
    else: 
        jon()

#based on def dead(why):
def boring():
    print "You're no fun at all. Go home."

def rating():
    print "On a scale of 1 to 5 (5 being the best), what did you think of this beer?"

    next = raw_input("> ")

    if "5" in next:
        ask = raw_input("Which one did you get? ")
        print """Lemme taste the %r....Whhaaa?! This one rules!
        Drinks all around of the %r!""" % (ask, ask)
        win()
    elif "4" in next:
        ask = raw_input("What would you prefer? ")
        print "Yum. That %r looks, smells, and has to be delicious and good enough for me! I'll take one too." % (ask)
        win()
    elif "3" in next:
        ask = raw_input("What would you prefer? ")
        print "Alright! Can someone give this hero a %r?. I'll take one too." % (ask)
        win()
    elif "2" in next:
        print "Oh no, now we know not to get these anymore. Let's choose another."
        bar()
    elif "1" in next:
        print "Damn! Return it and get another."
        bar()
    else:
        print boring("Do you want to leave?")

def win():
    print "We did it! We're having a good time! We all win!"

#bar()
start()