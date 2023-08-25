import json 
data = {
    "bottles":[
        ["EMPTY", "EMPTY", "EMPTY", "EMPTY"],
        ["EMPTY", "EMPTY", "EMPTY", "EMPTY"],
        ["GREEN", "BROWN", "DARK_GREEN", "PINK"],
        ["RED", "RED", "DARK_GREEN", "PURPLE"],
        ["BLUE", "LIGHT_BLUE", "ORANGE", "DARK_GREEN"],
        ["BLUE", "PINK", "DARK_GREEN", "YELLOW"],
        ["PURPLE", "BROWN", "GREEN", "DARK_BROWN"],
        ["ORANGE", "RED", "GREY", "LIGHT_BLUE"],
        ["ORANGE", "BROWN", "LIGHT_BLUE", "DARK_BROWN"],
        ["ORANGE", "YELLOW", "PURPLE", "LIGHT_BLUE"],
        ["DARK_BROWN", "YELLOW", "BLUE", "GREY"],
        ["BROWN", "PURPLE", "DARK_BROWN", "GREEN"],
        ["BLUE", "GREY", "PINK", "RED"],
        ["PINK", "GREY", "YELLOW", "GREEN"],
     ]
}

data = [b[::-1] for b in data["bottles"]]

print(data)