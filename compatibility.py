from platform import system as sy


def slash_type():
    if sy() in ("Windows",): return "\\"
    else: return "/"
