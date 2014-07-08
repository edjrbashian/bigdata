#!/usr/bin/python

import sys, os, re
from socket import *
import getopt
import time
import datetime
import urllib
import shutil
import telnetlib
import operator
import pdb

################################################################
#
#    Modified wordlist in the original file and write to modified file
#
################################################################

def replace_words ( original, modified, wordlist):

    f = open( original, "r")
    template = f.read()
    f.close()

    for key in wordlist.keys():
        p = re.compile ( key )
        template = p.sub( wordlist[key], template)
        
    fout = open (modified, "w")
    fout.write( template)
    fout.close()

################################################################        
#
#    Main
#
################################################################

def main (args):
    """
    media_express.py file=[movie filename]

    """
    if len(args) == 0:
        print main.__doc__
        sys.exit()

    if not os.path.exists( args['file']):
        print "Specified file [%s] doesn't exist." % args['file']
        sys.exit()

    fullpath = os.path.abspath( args['file'])    

    command = "qt_info %s" % fullpath
    response = os.popen(command).readlines()

    media_sample_count = re.compile('media sample count \: \d+')

    frames = ''
    for each_line in response:
        matching = media_sample_count.search(each_line.strip())
        if matching:           # If 'media sample count : line' is found,
            # extract the number of frames.
            frames = matching.group().split()[-1]
            break

    if frames == '':            # No info found
        print "Specified file [%s] is not a playable movie." % fullpath
        sys.exit()

    word_list = {}    
    word_list['FRAMES'] = frames
    word_list['PATHURL']  = fullpath
    word_list['FILENAME'] = os.path.split(fullpath)[-1]

    template = '/usr/local/bin/MediaExpressPlayback_template.xml'
    playback_xml = '/tmp/MeadiaExpress.xml'
    replace_words( template, playback_xml, word_list)
            
    script_path = "/usr/local/bin/playMediaExpress.scptd"
    command = "arch -i386 osascript %s %s" % (script_path, playback_xml)
    response = os.popen(command).readlines()
    if len(response):
        print response

################################################################
#
#    Make argument dictionary
#
################################################################

def argv_to_dictionary ():
    dictionary = {}
    for index in range (1, len(sys.argv)):
        pair = sys.argv[index]
        words = pair.split('=')
        try:
            value = words[1]
        except:
            value = ''
        dictionary[ words[0]] = value

    return dictionary        



################################################################
#
#    Main starts here.
#
################################################################

if __name__ == '__main__':    

    args = argv_to_dictionary()

    main ( args)


