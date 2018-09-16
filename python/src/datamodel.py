

class Tablature:

    # Create the object
    def __init__(self, band = "", song = "", content = "", multicol = False):
        self.band = band
        self.song = song
        self.content = content
        self.multicol = multicol

    # returns html code (body)
    def toHtml(self):
        aux = ""
        aux += "<h2 id='" +  self.id() + "'>" + self.band + " - " + self.song + "</h2>"
        aux += "<pre>" + self.content + "</pre>"
        return aux

    # returns html code (contents)
    def toHtml_content_line(self):
        aux = ""
        aux += "<li><a href=#" + self.id() + ">" + self.band + " - " + self.song + "</a></li>"
        return aux

    # returns unique ID
    def id(self):
        return self.band.replace(" ","") + self.song.replace(" ","")


    # compares to another tablature
    def equalTo(self,otherTablature):

        if isinstance(otherTablature, Tablature):
            a = otherTablature.band.lower() + "" + otherTablature.song.lower()
            b = self.band.lower() + "" + self.song.lower()
            if a == b:
                return True

        return False


class Chord:

    # Create the object
    def __init__(self, band = "", song = ""):
        self._name = name
        self._value = value

    # returns tex code
    def toTex(self):

        return "toTex method"
        '''
        tex = "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n";
        # TODO

        return tex;
        '''

    # compares to another chord
    def equalTo(self,otherChord):

        if isinstance(otherChord, Chord):
            a = otherChord._name.lower() + "" + otherChord._value.lower()
            b = self._name.lower() + "" + self._value.lower()
            if a == b:
                return True

        return False


###
### ############################################################################
###

# test statements

tb1 = Tablature("Oasis","Wonderwall","This is the content",False)
tb2 = Tablature("Oasis","Wonderwall","This is a repetition",True)
tb3 = Tablature("Daft Punk","Me","This is the content",True)


print tb1.toHtml()
print "------------------------------------------------"
print tb3.toHtml()
print "------------------------------------------------"
print tb1.equalTo(tb2)
print tb1.equalTo(tb3)

