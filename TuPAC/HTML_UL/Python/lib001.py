class HTMLUl:
    def __init__(self):
        pass

    def convert(self, array):
        html = []

        for item in array:

            if(not isinstance(item, list)):
                html.append("<li>%s</li>"%(item))
            
            else:
                html.append("<li>%s</li>" %(self.convert(item)))

        return "<ul>%s</ul>"%("".join(html))

    def ul2array(self, content):
        pass