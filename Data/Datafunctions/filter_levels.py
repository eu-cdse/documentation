def createcheckboxes(categories):
    checktext=''

    for levelid in categories:
        if levelid == "Level-0":
            checktext+=f"""<input type="checkbox" onchange=togglecheck("{levelid}") style="margin: 15px;"> {levelid}"""
        else:
            checktext+=f"""<input type="checkbox" onchange=togglecheck("{levelid}") style="margin: 15px;"checked> {levelid}"""
    return checktext



