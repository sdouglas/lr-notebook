#!/usr/bin/python

import getopt, re, os, sys, time
import shutil
from collections import defaultdict

usage_str = """Usage:
    python import_files.py -s source_path -d dest_path
    python import_files.py --src source_path --dest dest_path"""

def usage():
    print(usage_str)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:d:h', ['src=', 'dest=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    if len(opts) == 0:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-s', '--src'):
            src = arg
        elif opt in ('-d', '--dest'):
            dest = arg
        else:
            usage()
            sys.exit(2)

    ### traverse source_path to build list of files
    print "source =", src
    print "dest =", dest

    src_to_dest = {}
    dest_to_src = defaultdict(list)
    dest_to_description = {}
    dest_to_subfolder = {}

    # set up regex to extract dates from directory names
    # entry_pattern = re.compile("\/(\w+)\/(\d{4})-(\d{2})-(\d{2})_(\w+)\/")
    entry_pattern = re.compile("\/(\w+)\/(\d{4})-(\d{2})-(\d{2})_(\w+)\/(.+)\/")
    folder_pattern = re.compile("(\d{4}-\d{2}-\d{2}_(\w+)\/(.+))")

    # entries_with_spaces_pattern = re.compile("\/(\w+)\/(\d{4})-(\d{2})-(\d{2})_.+\ ")
    
    print "walking", src
    for (dirpath, dirnames, filenames) in os.walk(src):
        # print "dirpath", dirpath

        match = entry_pattern.search(dirpath)
        folder_match = folder_pattern.search(dirpath)


        if match:
            project = match.group(1)
            (year, month, day) = match.group(2,3,4)
            description = ' '.join(match.group(5).split('_'))
            subfolder = '/' + match.group(6)

            # map source files to lektor log-entry destination
            dest_sub_folder = '/%s/%s/%s' % (year, month, day)
            dest_path = dest + 'content/log' + dest_sub_folder + '/' + project
            for file in filenames:
                # if file[-3:] == '.md':
                #     print file
                
                file_project_path = "/Users/shawn/Desktop/projects/crane/experiments" 
                file_subfolder_path = folder_match.group(1)
                subfolder_only = folder_match.group(2)
                file_path = '/'.join([dirpath,file])
                src_to_dest[file_path] = dest_path
                dest_to_src[dest_path].append(file_path)
                dest_to_description[dest_path] = description
                dest_to_subfolder[dest_path] = subfolder_only + "\n" +file_subfolder_path
                file_subfolder_path
                # print file_path, "->", dest_path

    for fp, dp in src_to_dest.items():
        # print fp
        print "mkdir \"" + dp + "\""


    # for d, src_list in dest_to_src.items():
    #     print "mkdir "+ bcolors.WARNING + d + bcolors.ENDC
    #     print "echo " + bcolors.OKGREEN, "\"description: %s\"" % dest_to_description[d], bcolors.ENDC + ">> "+d+"/contents.lr"
    #     print dest_to_subfolder[d]
    #     for s in src_list:
    #         print "\t", s

        # for file in filenames:
        #     if file == "Icon\r":
        #         continue
        #     file_path = dirpath+'/'+file
        #     ### convert creation_date to dest_path subfolder
        #     t = time.gmtime(os.path.getmtime(file_path))
        #     dest_sub_folder = "/%s/%02d/%02d" % (t[0],t[1],t[2])
        #     dest_path = dest + "/content/log" + dest_sub_folder
        #     # print "cp " + file_path + " " + dest_path
        #     src_to_dest[file_path] = dest_path
        #     # time.strptime(created, "%Y/%m/%d")

    print "done."
    # sys.exit(0)
    # for key, value in src_to_dest.items():
    #     print "copy", key, "to", value
    #     shutil.copy2(key, value)
    #     contents_path = value + "/contents.lr"
    #     # print "update", contents_path
    #     ### update contents.lr in folders to unhide
    #     with open(contents_path, 'r') as f:
    #         read_data = f.read()
    #     new_data = read_data.replace(hidden_str,"")
    #     if read_data != new_data:
    #         with open(contents_path, 'w') as f:
    #            f.write(new_data)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
    main()
