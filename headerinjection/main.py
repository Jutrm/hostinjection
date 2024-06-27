import webbrowser
from units import banner
from units import chknet
from units import url
from includes import file
from includes import scan
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="enter the domain name")
parser.add_argument("-l","--list",help="enter the file name")
parser.add_argument("-o","--output",help="enter output file name")
parser.add_argument("-b","--blog",action='store_true',help="for more info about the bug")
args = parser.parse_args()

def main():
    if args.url:
        banner.banner()
        scan.cvescan(args.url,args.output)
    if args.list:
        banner.banner()
        file.reader(args.list,args.output)
    if args.blog:
        banner.banner()
        webbrowser.open(url.data.blog)
    
if __name__ == "__main__":
    if chknet.net():
        main()
    else:
        print("check internet")