#-------------------------------------------------------------------------------
# Name:        New Job
# Purpose:     Creates new job folder in the current directory
#
# Author:      brandan
#
# Created:     04/09/2013
# Copyright:   (c) brandan 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import shutil, datetime, os, time
from Tkinter import Tk
from tkFileDialog import askopenfilename

globaltemp_dir = "P:\\CADD\\Drafting\\Northshore Job Templates\\Clean Template - 08.12.2013"

def main():
    job_name = ""
    job_number = ""
    drafter_int = ""
    Workorder = ""
    date_today = datetime.date.today()
    date_today = date_today.strftime("%m-%d-%Y")

    print date_today
    print globaltemp_dir

    job_name = raw_input("Job Name: ")
    job_number = raw_input("Job Number: ")
    drafter_int = raw_input("Initials: ")

    folder_name = job_name + " " + job_number + " " + drafter_int.upper() + " " + date_today
    print "\n" + folder_name

    Workorder_q = raw_input("Load Workoder? (y/n): ")
    if Workorder_q.lower() == "y":
        Tk().withdraw()
        Workorder = askopenfilename()
        #print Workorder

    shutil.copytree(globaltemp_dir, folder_name)

    if Workorder != "":
        new_Workorder = folder_name + "\\Support\\Job Information.xls"
        shutil.copyfile(Workorder, new_Workorder)
        #dwg_info = folder_name + "\\Job Specific XREF's\\Job Information.dwg"
        #os.system(os.curdir + folder_name + "\\Job Specific XREF's\\Job Information.dwg")
        #execfile(dwg_info)

    os.system('cls')
    #print dwg_info
    print "Job Creation Complete\n\t~Brandan Haertel"
    time.sleep(2.5)

if __name__ == '__main__':
    main()
