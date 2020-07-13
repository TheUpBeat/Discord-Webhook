import requests
import json

print("Send Messages through a Webhook to the specific Channel \n")
url = str(input("Enter the Webhook URL of the channel "))
choice = str(input("Enter \n N/n for Normal Message \n E/e for Embeded Message \n "))

if (choice == "N" or choice == "n"):
    data = {}
    content = (input("Enter the Message:\n"))
    data["content"] = content

    username = (input("Enter the Bot's Username (Press Enter to use the default settings): "))
    if not username == "":
        data["username"] = username

    avatar_url = (input("Enter the Bot's Avatar (url) (Press Enter to use the default settings): "))
    if not avatar_url == "":
        data["avatar_url"] = avatar_url

elif (choice == "E" or choice == "e"):
    data = {}
    data["embeds"] = []
    embed = {}

    advancedornot = str(input("Enter \n B/b for Basic options for Embed \n A/a for More options for Embed \n"))
    if (advancedornot == 'B' or advancedornot == 'b'):
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        color = (input("Enter the color code (Press Enter to use the default settings): "))

        embed["title"] = title
        embed["description"] = description
        if not color == "":
            embed["color"] = color


    elif (advancedornot == 'A' or advancedornot == 'a'):

        username = (input("Enter the Bot's Username (Press Enter to use the default settings): "))
        if not username == "":
            data["username"] = username

        avatar_url = (input("Enter the Bot's Avatar (url) (Press Enter to use the default settings): "))
        if not avatar_url == "":
            data["avatar_url"] = avatar_url

        author_name = input("Enter C of the Author (Press Enter to use the default settings): ")
        if not author_name == "":
            name = input("Author's Name: ")
            URL = input("Author's URL: ")
            iconurl = input("Icon URL: ")

            author = {}

            if not name == "":
                author["name"] = name

            if not URL == "":
                author["url"] = URL

            if not iconurl == "":
                author["icon_url"] = iconurl

            embed["author"] = author

        title = input("Enter the title: ")
        embed["title"] = title

        description = input("Enter the description: ")
        embed["description"] = description

        color = input("Enter the color code (Press Enter to use the default settings): ")
        if not color == "":
            embed["color"] = color

        field = input("Enter number of fields (Press Enter to use the default settings): ")

        if not field == "":
            number = int(field)
            embed ["fields"] = []
            fields = {}

            for i in range(number):
                name = input("Name of the field: ")
                fields["name"] = name
                value = input("Value of the field: ")
                fields["value"] = value
                trueornot = input("Inline: \n T/t for True \n F/f for False \n")
                if (trueornot == 'T' or trueornot == 't'):
                    fields["inline"] = True
                elif (trueornot == 'F' or trueornot == 'f'):
                    fields["inline"] = False

                embed["fields"].append(fields)

        footer = input("Enter C to add info to the footer (Press Enter to use the default settings): ")

        if not footer == "":
            footer = {}
            text = input("Footer Text: ")
            icon_url = input("Footer Icon URL: ")

            if not text == "":
                footer["text"] = text

            if not icon_url == "":
                footer["icon_url"] = icon_url

            embed["footer"] = footer

        image_url = input("Enter the URL of Image (Press Enter to use the default settings): ")
        if not image_url == "":
            image = {}

            image["url"] = image_url
            embed["image"] = image

        thumbnail_url = input("Enter the URL of Thumbnail (Press Enter to use the default settings): ")
        if not thumbnail_url == "":
            thumbnail = {}

            thumbnail["url"] = thumbnail_url
            embed["thumbnail"] = thumbnail

    data["embeds"].append(embed)


result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
