#!/usr/bin/env ruby

class Tablature

    attr_accessor :band;
    attr_accessor :song;
    attr_accessor :content;
    attr_accessor :multicol;

    # Create the object
    def initialize(band = "", song = "", content = "", multicol = "")
        @band = band
        @song = song
        @content = content
        @multicol = multicol
    end

    # returns tex code
    def toTex

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
    end

    # compares to another tablature
    def equalTo(otherTablature)
        if otherTablature.is_a?(Tablature)
            a = otherTablature.band.downcase + "" + otherTablature.song.downcase;
            b = @band.downcase + "" + @song.downcase;

            if a == b
                return true;
            end
        end
        return false;
    end

end

class Chord

    attr_accessor :name;
    attr_accessor :value;

    # Create the object
    def initialize(band = "", song = "")
        @name = name
        @value = value
    end

    # returns tex code
    def toTex

        tex = "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n";
        # TODO

        return tex;
    end

    # compares to another chord
    def equalTo(otherChord)
        if otherChord.is_a?(Chord)
            a = otherChord.name.downcase + "" + otherChord.value.downcase;
            b = @name.downcase + "" + @value.downcase;
            if a == b
                return true;
            end
        end
        return false;
    end

end

###
### ############################################################################
###


if __FILE__ == $0

    tb1 = Tablature.new("Oasis","Wonderwall","This is the content",false);
    tb2 = Tablature.new("Oasis","Wonderwall","This is a repetition",true);
    tb3 = Tablature.new("Daft Punk","Me","This is the content",true);

    puts tb1.toTex
    puts "------------------------------------------------"
    puts tb3.toTex
    puts "------------------------------------------------"
    puts tb1.equalTo(tb2)
    puts tb1.equalTo(tb3)

end
