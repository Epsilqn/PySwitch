def sample_default(): print("No default function was provided.")


class Switch:
    def __init__(self, default_function=sample_default): self.map = {"default": default_function}

    def add(self, sid: str, fnc) -> None: self.map[sid] = fnc

    def rm(self, sid: str) -> None: del self.map[sid]

    def exec_(self, sw) -> None:
        try: self.map[sw]()
        except KeyError: self.map["default"]()
