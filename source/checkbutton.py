from button import Button

class CheckButton(Button):
    # Loads button and then set selected image and state
    def __init__(self, path, selectedImage, checkedImage, boxImage, x, y, checked=False):
        super().__init__(path, selectedImage, x, y)
        self.checkedImage = checkedImage
        self.boxImage = boxImage
        self.checked = checked

    def isChecked(self):
        return self.checked

    def toggleCheck(self):
        if self.checked:
            self.checked = False
        else:
            self.checked = True

    def render(self, bufferSurface):
        self.boxImage.render(bufferSurface, self.x, self.y)
        self.textImage.render(bufferSurface, self.x + 50, self.y)
        if self.selected:
            self.selectedImage.render(bufferSurface, self.x, self.y)
        if self.checked:
            self.checkedImage.render(bufferSurface, self.x, self.y)
