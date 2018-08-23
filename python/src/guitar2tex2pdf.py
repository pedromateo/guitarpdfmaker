










'''
#require 'datamodel.rb'
load 'datamodel.rb'

require 'fileutils'

if __FILE__ == $0

    ###
    ###
    ###

    # args must be at least 2: sources and output file name
    # e.g.: ruby guitar2tex2pdf.rb sample1.g2tr mybook.pdf
    # e.g.: ruby guitar2tex2pdf.rb sample1.g2tr sample2.g2tr mybook.pdf
    # e.g.: ruby guitar2tex2pdf.rb *.g2tr mybook

    if ARGV.length < 2
        puts "Usage: guitar2tex2pdf.rb inputFile(s) outputFile"
        puts "-----------------------------------------------------------------"
        puts "Usage example: ruby guitar2tex2pdf.rb sample1.g2tr mybook.pdf"
        puts "Usage example: ruby guitar2tex2pdf.rb sample1.g2tr sample2.g2tr mybook.pdf"
        puts "Usage example: ruby guitar2tex2pdf.rb *.g2tr mybook"
        return
    end

    puts "Analyzing file(s):"
    for i in 0..ARGV.length-2
        puts "- " + ARGV[i]
    end
    puts "Output directory: " + ARGV[ARGV.length-1]
    puts "---------------------------------------------------------------------"

    ###
    ### declare lists and constants
    ###

    # create lists
    chords = Array.new;
    tabs = Array.new;
    currentTab = 0;

    # data constants
    BAND = "$BB";
    SONG = "$SS";
    CHORD = "$CH";
    MULTICOL = "$MC";

    # generation constants
    BASEDIR = "./texbase";
    GENDIR = "./tmp";
    GENBASEFILE = "./tmp/input.body";
    GENRESULTFILE = "./tmp/base.pdf";
    DESTFILE = ARGV[ARGV.length-1];

    theFirst = true;

    ###
    ### read each file line by line
    ###

    line_num=0
    for i in 0..ARGV.length-2
        puts "Processing file " + ARGV[i]

        # open file
        text = File.open(ARGV[i]).read
        text.gsub!(/\r\n?/, "\n")
        # read line by line
        text.each_line do |line|

            # latex changes:
            # ´ by '
            # & by \&

            line.gsub!("´","'");
            line.gsub!("&","\&");

            ####################################################################
            # avoid comments
            if line.start_with?("#")
                #do nothing
                #puts "comment";

            ####################################################################
            # band
            elsif  line.start_with?(BAND)
                #puts "band";
                # remove identifier
                line.slice! BAND;
                # trim string
                line.strip!;
                # remove last \n
                line.gsub!("\n","");

                # add old tablature to the list
                if theFirst
                    theFirst = false;
                else
                    tabs << currentTab;
                end

                # create a new tab
                currentTab = Tablature.new;

                # set the band name
                currentTab.band = line;

            ####################################################################
            # song
            elsif  line.start_with?(SONG)

                #clean line
                line.slice! SONG;
                line.strip!;
                line.gsub!("\n","");

                # set the song name
                currentTab.song = line;

                puts "adding song: " + currentTab.band + " :: " + currentTab.song;

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