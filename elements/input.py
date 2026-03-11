from elements.base_element import BaseElement


class Input(BaseElement):
    def fill(self, text):
        elem = self.find()
        elem.clear()
        elem.send_keys(text)
