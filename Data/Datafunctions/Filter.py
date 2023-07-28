def createcheckboxes(categories):
    checktext=''

    for levelid in categories:
        checktext+=f"""<input type="checkbox" onchange=togglecheck("{levelid}","none") style="margin: 15px;" checked> {levelid}"""
    return checktext