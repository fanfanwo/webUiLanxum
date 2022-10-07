
import json


def create_data(file_name):
    file_r = open(file_name, encoding="utf-8").read()
    data = json.loads(file_r)

    def wrapper(cls):
        for i in data:
            if i["type"] == "button":
                setattr(getattr(cls, "Button"), i["name"], (i["selector"], i["value"]))
            if i["type"] == "input":
                setattr(getattr(cls, "Input"), i["name"], (i["selector"], i["value"]))
            if i["type"] == "link":
                setattr(getattr(cls, "Link"), i["name"], (i["selector"], i["value"]))
            if i["type"] == "url":
                setattr(cls, "url", i["value"])
            if i["type"] == "frame":
                setattr(cls, "iframe", i["value"])
        return cls

    return wrapper
