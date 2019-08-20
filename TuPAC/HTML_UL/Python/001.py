from lib001 import *

list = HTMLUl()
file = open("index.html", "w")
content = list.convert(
    [
        "Hola Mundo",
        list.convert(
            [
                1,
                [1,2,3]
            ]
        )
    ]
)

file.write(content)
file.close