def GetTextUser(message):
    text = ""
    typeMessage = message["type"]
    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactive = message["interactive"]
        typeInteractive = interactive["type"]
        if typeInteractive == "button_reply":
            text = (interactive["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactive["list_reply"])["title"]
        else:
            print("[!] Interactive type not supported")
    else:
        print("[!] Message type not supported")
    return text