#!/usr/bin/python

import getopt, os, sys, time
import shutil

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

    print "walking", src
    for (dirpath, dirnames, filenames) in os.walk(src):
        # print "dirpath", dirpath
        # print "dirnames",dirnames
        # print "filenames",filenames

        ok = False
        if '01_photos' in dirpath:
            ok = True
        elif '02_xyz' in dirpath:
            ok = True
        elif '03_pointfuse' in dirpath:
            ok = True

        if ok:
            continue

        for file in filenames:
            if file == "Icon\r":
                continue
            file_path = dirpath+'/'+file
            ### convert creation_date to dest_path subfolder
            t = time.gmtime(os.path.getmtime(file_path))
            dest_sub_folder = "/%s/%02d/%02d" % (t[0],t[1],t[2])
            dest_path = dest + "/content/log" + dest_sub_folder
            # print "cp " + file_path + " " + dest_path
            src_to_dest[file_path] = dest_path
            # time.strptime(created, "%Y/%m/%d")

    print "done."
    # sys.exit(0)
    for key, value in src_to_dest.items():
        print "copy", key, "to", value
        shutil.copy2(key, value)
        contents_path = value + "/contents.lr"
        # print "update", contents_path
        ### update contents.lr in folders to unhide
        with open(contents_path, 'r') as f:
            read_data = f.read()
        new_data = read_data.replace(hidden_str,"")
        if read_data != new_data:
            with open(contents_path, 'w') as f:
               f.write(new_data)


hidden_str = """_hidden: yes
---
"""

usage_str = """Usage:
    python import_files.py -s source_path -d dest_path
    python import_files.py --src source_path --dest dest_path"""

def usage():
    print(usage_str)


if __name__ == "__main__":
    main()
