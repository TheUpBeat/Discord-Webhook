import requests
import json

print("Send Messages through a Webhook to the specific Channel \n")
url = str(input("Enter the Webhook URL of the channel "))
choice = str(input("Enter \n N/n for Normal Message \n E/e for Embeded Message \n "))

if (choice == "N" or choice == "n"):
    data = {}
    content = (input("Enter the Message:\n"))
    username = (input("Enter the Bot's Username (Press Enter to use the default settings): "))
    avatar_url = (input("Enter the Bot's Avatar (url) (Press Enter to use the default settings): "))
    tts = (input("Enter a TTS Message (Press Enter to use the default settings): "))
    allowed_mentions = (input("Enter the Members to be mentioned (Press Enter to use the default settings): "))

    if not username.isalpha():
        pass
    else:
        data["username"] = username

    if not avatar_url.isalpha():
        pass
    else:
        data["avatar_url"] = avatar_url

    if not tts.isalpha():
        pass
    else:
        data["tts"] = tts

    if not allowed_mentions.isalpha():
        pass
    else:
        data["allowed_mentions"] = allowed_mentions

    data["content"] = content


elif (choice == "E" or choice == "e"):
    data = {}
    data["embeds"] = []
    embed = {}
    embed["footer"] = []
    foot = {}

    advancedornot = str(input("Enter \n B/b for Basic options for Embed \n A/a for More options for Embed \n"))
    if (advancedornot == 'B' or advancedornot == 'b'):
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        color = input("Enter the color code (Press Enter to use the default settings): ")
        if not color.isalpha():
            pass
        else:
            embed["color"] = color

        embed["title"] = title
        embed["description"] = description

    elif (advancedornot == 'A' or advancedornot == 'a'):
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        color = input("Enter the color code (Press Enter to use the default settings): ")
        footer = input("Enter C to add info to the footer (Press Enter to use the default settings): ")

        if not footer.isalpha():
            pass
        else:
            text = input("Enter the Footer information: ")
            icon_url = input("Enter URL of the footer icon (Press Enter to use the default settings): ")
            proxy_icon_url = input("Enter proxy URL of the footer icon (Press Enter to use the default settings): ")
            if not icon_url.isalpha():
                pass
            else:
                foot["icon_url"] = icon_url

            if not proxy_icon_url.isalpha():
                pass
            else:
                foot["proxy_icon_url"] = proxy_icon_url

            foot["text"] = text

        image = input("Enter the URL of Image (Press Enter to use the default settings): ")
        thumbnail = input("Enter the URL of Thumbnail (Press Enter to use the default settings): ")
        video = input("Enter the URL of Video (Press Enter to use the default settings): ")
        author = input("Enter the Name of the Author (Press Enter to use the default settings): ")
        fields = input("Enter info in fields (Press Enter to use the default settings): ")

        if not color.isalpha():
            pass
        else:
            embed["color"] = color


        if not image.isalpha():
            pass
        else:
            embed["image"] = image
        if not thumbnail.isalpha():
            pass
        else:
            embed["thumbnail"] = thumbnail
        if not video.isalpha():
            pass
        else:
            embed["video"] = video
        if not author.isalpha():
            pass
        else:
            embed["author"] = author
        if not fields.isalpha():
            pass
        else:
            embed["fields"] = fields

        embed["title"] = title
        embed["description"] = description

    embed["footer"].append(foot)
    data["embeds"].append(embed)


result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
