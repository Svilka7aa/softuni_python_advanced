# def add_songs(*args):
#     result = ""
#     songs = {}
#     for i in args:
#         song = i[0]
#         lyrics = i[1]
#         result += f"- {song}" + "\n"
#         if lyrics:
#             final_lyrics = "\n".join(lyrics)
#             result += f"{final_lyrics}"
#
#     return result



def add_songs(*args):
    result = ""
    songs = {}
    for i in args:
        song = i[0]
        lyrics = i[1]
        if song in songs:
            songs[song] += lyrics
        else:
            songs[song] = lyrics

    for key, value in songs.items():
        result += f"- {key}" + "\n"
        if len(value):
            result += "\n".join(value) + "\n"

    return result.strip()


# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))
#
#
# print("-" * 50)
#
#
# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))
# print("-" * 50)

print(add_songs(
            ("Love of my life",
             ["Love of my life, you've hurt me",
              "You've broken my heart, and now you leave me",
              "Love of my life, can't you see?",
              "Bring it back, bring it back"]),
            ("Beat It", []),
            ("Love of my life",
             ["Don't take it away from me",
              "Because you don't know",
              "What it means to me"]),
            ("Dream On",
             ["Every time that I look in the mirror"]),
        ))