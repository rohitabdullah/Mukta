import datetime
from termcolor import colored, cprint

person_name = "Mukta"
birthday_date = datetime.date(2025, 1, 3)

today = datetime.date.today()
if today == birthday_date:
else print ("Hop beda, Ajke birthday na")
    # Create a colorful and animated message
    message = f"✨ Happy birthday, dear {person_name}! ✨"
    cprint(message, "magenta", "on_yellow", attrs=["bold"])

    # Add a scrolling rainbow effect
    for color in ["red", "green", "yellow", "blue", "magenta"]:
        cprint("Wishing you a day filled with joy, laughter, and all the things you love!", color, attrs=["blink"])

    # Print a colorful cake (ASCII art)
    cake = colored("""
                0   0

                |   |

            ____|___|____

         0  |~ ~ ~ ~ ~ ~|   0

         |  |           |   |

      ___|__|___________|___|__

      |/\/\/\/\/\/\/\/\/\/\/\/|

  0   |       H a p p y       |   0

  |   |/\/\/\/\/\/\/\/\/\/\/\/|   |

 _|___|_______________________|___|__

|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|

|                                   |

|         B i r t h d a y! ! !      |

| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |

|___________________________________|



------------------------------------------------


""", "yellow")
    print(cake)

