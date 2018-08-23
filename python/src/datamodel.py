

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

        return "equalTo method"
        '''
        if otherTablature.is_a?(Tablature)
            a = otherTablature.band.downcase + "" + otherTablature.song.downcase;
            b = @band.downcase + "" + @song.downcase;

            if a == b
                return true;
            end
        end
        return false;
        '''


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

        return "equalTo method"

        '''
        if otherChord.is_a?(Chord)
            a = otherChord.name.downcase + "" + otherChord.value.downcase;
            b = @name.downcase + "" + @value.downcase;
            if a == b
                return true;
            end
        end
        return false;
        '''


###
### ############################################################################
###

# test statements

tb1 = Tablature("Oasis","Wonderwall","This is the content",False)
tb2 = Tablature("Oasis","Wonderwall","This is a repetition",True)
tb3 = Tablature("Daft Punk","Me","This is the content",True)


tb1.toTex()
"------------------------------------------------"
tb3.toTex()
"------------------------------------------------"
tb1.equalTo(tb2)
tb1.equalTo(tb3)

