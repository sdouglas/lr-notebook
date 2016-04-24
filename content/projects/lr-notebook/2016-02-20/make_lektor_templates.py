#!/usr/bin/python

import calendar
import getopt, os, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:y:h', ['user=', 'year=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-u', '--user'):
            user = arg
        elif opt in ('-y', '--year'):
            year = arg
        else:
            usage()
            sys.exit(2)

    cal = calendar.Calendar()
    
    for month in range(1,13):
        month_str = '%02d'%month
        month_num_with_abbr = month_str + '-' + calendar.month_abbr[month]
        for day in range(1,1+calendar.monthrange(int(year),month)[1]):
            day_str = '%02d'%day
            path = "/".join([year,month_num_with_abbr,day_str])
            os.makedirs(path)
            with open(path+'/contents.lr', 'w+') as f:
                pub_date = '%s-%s-%s' % (year, month_str, day_str)
                f.write(lektor_day_template % (day_str, user, pub_date))
        month_path = "/".join([year,month_num_with_abbr,'contents.lr'])
        with open(month_path, 'w+') as f:
            f.write(lektor_month_template % (month_str, month_str, calendar.month_name[month], calendar.month_abbr[month]))
    with open(year+'/contents.lr', 'w+') as f:
        f.write(lektor_year_template % (year, year))

usage_str = """Usage:
    python foo.py -u username -y year
    python foo.py --user username --year year"""

def usage():
    print(usage_str)


lektor_year_template = """_model: year
---
name: %s
---
label: %s
"""

lektor_month_template = """_slug: %s
---
title: %s
---
description: %s
---
label: %s
"""

lektor_day_template = """_hidden: yes
---
title: %s
---
username: %s
---
pub_date: %s
---
categories:
---
description: 
---
body:


"""

if __name__ == "__main__":
    main()
