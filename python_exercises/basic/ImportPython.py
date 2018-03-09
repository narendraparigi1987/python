#!/usr/bin/python -tt

import subprocess
import os
from subprocess import *
import sys
import platform

#Global variables declarations
currentDir=''
pmrepPath=''
domainFile=''

#Function to connect to the repository expects name of repository , domain and user details
def connect_to_repo(Repository,Domain,User):
    RepoCommand="pmrep connect -r "+Repository+" -d "+Domain+" -n "+User+" -X DOMAIN_PWD"
    RepoCommand=RepoCommand.rstrip()
    p=subprocess.Popen(RepoCommand,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    out,err=p.communicate()
    if p.returncode or err:
        print "\n\n ERROR : Connection Failed !!!"
        sys.stdout.flush()
        sys.stdin.flush()
    else:
        print "Connection Successful !!!"
        sys.stdout.flush()
        sys.stdin.flush()
    return p.returncode

#Executes any os command, here provided pre defined commands
def execute_pmrep_command(command,output_file_name):
    out=open(output_file_name,'w')
    return_code=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    output,error=return_code.communicate()
    out.writelines(output.strip())
    out.close()
    return 
  
#Function to make output dirs , create if not exist
def create_output_directories():
    if platForm == 'Windows':
        try:
            os.makedirs(currentDir.strip()+"\LogFiles")
            print "Log files generated and stored in 'LogFiles' directory" #
        except OSError:
            print "Log files generated and stored in 'LogFiles' directory" #
            pass
    elif platForm == 'Linux':
        try:
            os.makedirs(currentDir.strip()+"/LogFiles")
            print "Log files generated and stored in 'LogFiles' directory" #
        except OSError:
            print "Log files generated and stored in 'LogFiles' directory" #
            pass
    elif platForm == 'SunOS':                
        try:
            os.makedirs(currentDir.strip()+"/LogFiles")
            print "Log files generated and stored in 'LogFiles' directory" #
        except OSError:
            print "Log files generated and stored in 'LogFiles' directory" #
            pass
						
#Checking for all necessary environment variables
def check_platform():
    global domainFile
    global currentDir
    global pmrepPath
    global platForm
    platForm=platform.system()
    print "Platform recognized : "+platForm
    if not os.getenv('INFA_HOME'):
        print "INFA_HOME environment variable is not set in your "+platForm+" platform." #
        print "\nPlease set INFA_HOME and run the script." #
        raw_input()
        sys.exit(0)
    elif not os.getenv('INFA_DOMAIN_INFO'):
        print "INFA_DOMAIN_INFO environment variable is not set in your "+platForm+" platform." #
        print "\nPlease set INFA_DOMAIN_INFO and run the script." #
        raw_input()
        sys.exit(0)
    elif not os.getenv('DOMAIN_PWD'):
        print "DOMAIN_PWD environment variable not set in your "+platForm+" platform." #
        print "\nPlease set DOMAIN_PWD and run the script." #
        sys.exit(0)
    else:
        if platForm == 'Windows':
            pmrepPath=os.getenv('INFA_HOME').strip()+"\clients\PowerCenterClient\client\\bin"
        elif platForm == 'Linux':
            pmrepPath=os.getenv('INFA_HOME').strip()+"/server/bin"
        elif platForm == 'SunOS':
            pmrepPath=os.getenv('INFA_HOME').strip()+"/server/bin"
        currentDir=os.getcwd()
        domainFile=os.getenv('INFA_DOMAIN_INFO').strip()

#Start of the main program body
def main():
    if len(sys.argv) != 3:
        print 'usage: python ImportPython.py controlFile xmlfile'
        sys.exit(1)
    
    if platform.system()=='Windows':
        os.system('cls')
    elif platform.system()=='Linux':
        os.system('clear')
    elif platform.system()=='SunOS':
        os.system('clear')
    
    print "Checking for all necessary environment variables ....\n"
    check_platform()
    print "\n\n***********************************************************************\n\n"
    
    lines=open(domainFile,'rU').readlines()
    os.chdir(pmrepPath)
    if platForm == 'Windows':
        logFileLoc=currentDir.strip()+"\LogFiles\importlog.txt"
    elif platForm == 'Linux':
        logFileLoc=currentDir.strip()+"/LogFiles/importlog.txt"
    elif platForm == 'SunOS':
        logFileLoc=currentDir.strip()+"/LogFiles/importlog.txt"
    
    for line in lines:
        fields=line.split(',')
        Repository=fields[0]
        Domain=fields[1]
        User=fields[2]
        
        print Repository+ ' ' +Domain+ ' ' +User
        
        return_code=connect_to_repo(Repository,Domain,User)
        
        print "\n***********************************INPUT*******************************\n\n"
        if return_code:
            continue
            #controlFile=raw_input("Enter control file name : ")
            controlFile=sys.argv[1]		
        if platForm == 'Windows':
            controlFile=currentDir.strip()+"\\"+controlFile.strip()
        elif platForm == 'Linux':
            controlFile=currentDir.strip()+"/"+controlFile.strip()
        elif platForm == 'SunOS':
            controlFile=currentDir.strip()+"/"+controlFile.strip()
        cLines=open(controlFile,'r').readlines()
        open("controlFile.txt",'w').writelines(cLines)
        
        #xmlFile=raw_input("\n\nEnter the xml file to import : ")
        xmlFile=sys.argv[2]		
        impFile=xmlFile
        print "\n\n***********************************OUTPUT******************************\n\n"
        create_output_directories()
        if platForm == 'Windows':
            xmlFile=currentDir.strip()+"\\"+xmlFile.strip()
        elif platForm == 'Linux':
            xmlFile=currentDir.strip()+"/"+xmlFile.strip()
        elif platForm == 'SunOS':				
            xmlFile=currentDir.strip()+"/"+xmlFile.strip()
        
        iLines=open(xmlFile,'r').readlines()
        open(impFile,'w').writelines(iLines)
        import_command="pmrep objectimport -i "+impFile.strip()+" -c controlFile.txt"
        execute_pmrep_command(import_command,logFileLoc)
        os.remove("controlFile.txt")
        os.remove(impFile)
        print "\n\nImport operation completed, \n\nFor more details please refer 'importlog.txt' in LogFiles directory.\n\n***********************************************************************"

if __name__ == '__main__':
  main()