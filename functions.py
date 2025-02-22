def emojiConverter(message):
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    emoji = emojis[message.split(" ")[-1]]
    return message.replace(message.split(" ")[-1], emoji)


message = emojiConverter("Good morning :)")
print(message)
