
import sys
from xhtml2pdf import pisa
from cStringIO import StringIO
from datamodel import *


if __name__ == '__main__':


    # args must be at least 2: sources and output file name
    # e.g.: ruby guitar2tex2pdf.rb sample1.g2tr mybook.pdf
    # e.g.: ruby guitar2tex2pdf.rb sample1.g2tr sample2.g2tr mybook.pdf
    # e.g.: ruby guitar2tex2pdf.rb *.g2tr mybook

    if len(sys.argv) < 2:
        print "Usage: guitar2tex2pdf.py inputFile(s) outputFile"
        print "-----------------------------------------------------------------"
        print "Usage example: python guitar2tex2pdf.py sample1.g2tr mybook.pdf"
        print "Usage example: python guitar2tex2pdf.py sample1.g2tr sample2.g2tr mybook.pdf"
        print "Usage example: python guitar2tex2pdf.py *.g2tr mybook"


    '''for idx, arg in enumerate(sys.argv):
       print("arg #{} is {}".format(idx, arg))
    print'''

    ###
    ### process variables
    ###

    # constants
    BAND = "$BB"
    SONG = "$SS"
    CHORD = "$CH"
    MULTICOL = "$MC";

    # generation constants
    GENDIR = "./output"

    # control variables
    in_song = False
    current_tab = -1


    chords = []
    tabs = []

    argc = len(sys.argv)
    OUTPUT_FILE = sys.argv[argc - 1]
    print "Generating output in: " + OUTPUT_FILE


    ### #######################################################################
    print "## File processing ################################################"
    ###

    #for idx, arg in enumerate(sys.argv):
    for i in range(1,argc-1):
        #print("arg #{} is {}".format(idx, arg))
        current_infilepath = sys.argv[i]
        print "Processing file: " + current_infilepath

        with open(current_infilepath) as f:
            content = f.readlines()

        for line in content:
            line = line.replace("\r\n","\n")
            #print line

            #################
            # avoid comments
            if line.startswith("#"):
                pass


            #######
            # band
            elif line.startswith(BAND):

                # create new tablature object and add it to the array
                tabs.append(Tablature())
                current_tab += 1

                # get band name
                tabs[current_tab].band = line.replace(BAND,'').replace('\n','').strip()
                #print tabs[current_tab].band


            #######
            # song
            elif line.startswith(SONG):

                # get song name
                tabs[current_tab].song = line.replace(SONG,'').replace('\n','').strip()
                print "Adding song: " + tabs[current_tab].band + " - " + tabs[current_tab].song


            ###########
            # multicol
            elif line.startswith(MULTICOL):
                tabs[current_tab].multicol = True


            ############
            # song line
            else:
                if current_tab >= 0:
                    tabs[current_tab].content += line + "-\r\n-"


    ### #######################################################################
    print "## Tabs optimization ##############################################"
    ###

    # sort tabs
    tabs = sorted(tabs, key=lambda x: x.band, reverse = False)

    for x in tabs:
        #t = (Tablature)x
        #print "XX " + t.band + " :: " + t.song
        print "XX " + x.band + " :: " + x.song


    ### #######################################################################
    print "## PDF generation #################################################"
    ###

    # Define your data
    sourceHtml = "<html><body>"

    for t in tabs:

        sourceHtml += t.toHtml()

    sourceHtml += "</body></html>"


    outputFilename = "test.pdf"


    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
        sourceHtml,  # the HTML to convert
        dest=resultFile)  # file handle to recieve result

    # close output file
    resultFile.close()  # close output file

    # return True on success and False on errors
    print pisaStatus.err



    ###
    ### script end
    print "done."



'''

    theFirst = true;

    ###
    ### read each file line by line
    ###


            
    

            ####################################################################
            # chord
            elsif  line.start_with?(CHORD)
                #puts "chord";

                #clean line
                line.slice! CHORD;
                line.strip!;
                line.gsub!("\n","");

                #if line.eql? ""
                if line.empty?
                    continue;
                end

                puts "adding chord: " + line;

                # get chord info and create a new chord
                values = line.split(" ");

                c = Chord.new;
                c.name = values[0];
                c.value = values[1];

                chords << c;

            ####################################################################
            # multicol
            elsif  line.start_with?(MULTICOL)
                puts "multicol";

                currentTab.multicol = true;

            ####################################################################
            # song line
            else
                #puts "normal line";
                currentTab.content += line;

            end

            #print "#{line_num += 1} #{line}"
        end

    end


    ###
    ### sort arrays
    ###

    chords.sort! { |a,b| a.name.downcase <=> b.name.downcase };
    tabs.sort! { |a,b| a.band.downcase + a.song.downcase <=>
        b.band.downcase + b.song.downcase };

    puts "\n\n==================== tabs ====================";

    counter = 0;
    chords.each do |c|
        puts "Chord " + counter.to_s + ": " + c.name
    end

    puts "\n\n=================== chords ===================";

    counter = 0;
    tabs.each do |t|
        puts "Tab " + (counter+=1).to_s + ": " + t.band + " -> " + t.song
    end


    ###
    ### check duplicates TODO
    ###


    ###
    ### pre-generation actions
    ###

    # BASEDIR
    # GENDIR
    # GENBASEFILE

    # delete existing? GENDIR
    FileUtils.rm_rf(GENDIR)
    FileUtils.cp_r(BASEDIR,GENDIR)

    ###
    ### generation - add songs and chords to file
    ###

    out_file = File.new(GENBASEFILE, "w");

    # add tabs
    tabs.each do |t|
        out_file.puts(t.toTex);
    end

    # add chords
    chords.each do |c|
        out_file.puts(c.toTex);
    end

    out_file.close


    ###
    ### post-generation actions
    ###

    # compile latex file inside GENDIR
    Dir.chdir GENDIR;
    system "make clean"
    system "make"

    if $?.exitstatus > 0
        puts "Some errors happen with make :'(  Please, check."
    end

    Dir.chdir "..";

    # copy resulting file to dest file
    FileUtils.cp(GENRESULTFILE,DESTFILE);


    ###
    ###
    ###


    ###
    ###
    ###

end
'''