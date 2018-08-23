

class Tablature:

    # Create the object
    def __init__(self, band = "", song = "", content = "", multicol = False):
        self._band = band
        self._song = song
        self._content = content
        self._multicol = multicol

    # returns tex code
    def toTex(self):

        return "toTex method"
        '''
        # header
        tex = "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n";
        tex += "\\newpage\n";
        tex += "\\section{ #{band} - #{song} }\n";

        if multicol == true
            tex += "\\begin{multicols}{2}\n";
        end

        tex += "\\begin{verbatim}\n";
        # content
        tex += content;
        tex += "\n\\end{verbatim}\n";

        if multicol == true
            tex += "\\end{multicols}\n";
        end

        return tex;
        '''

    # compares to another tablature
    def equalTo(self,otherTablature):

        if isinstance(otherTablature, Tablature):
            a = otherTablature._band.lower() + "" + otherTablature._song.lower()
            b = self._band.lower() + "" + self._song.lower()
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


print tb1.toTex()
print "------------------------------------------------"
print tb3.toTex()
print "------------------------------------------------"
print tb1.equalTo(tb2)
print tb1.equalTo(tb3)

