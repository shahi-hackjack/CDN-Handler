import os
import requests
import bs4
import re

def cdndownload(x):
    f=open(fullfilepath, 'r') #reads the content of html  file obj
    soup=bs4.BeautifulSoup(f.read(),'html.parser') #parse the object as html dom

    for link in soup.find_all(x):#this loops searches for link and script tag
         flag=0
         if((link.parent.name)=="head"):
             #print(link.get('href'))
            #   print(str(link))
            #if there is any url that has http and https type that is actual url is considered as cdn
              url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(link))
              #print(url) if url list is not empty
              if url:
                 filename=url[0].split('/')[-1] #gets the filename which will be used for saving on localcomputer
                 foldername=url[0].split('.')[-1] #gets js or cs extension
                 realdirectory=directory+"\\"+"cdn"+foldername+"\\"+filename #gets full working directory with file
                 newpath=directory+"\\"+"cdn"+foldername  # gets pwd used for creating folder css and js
                 #  print(realdirectory)
                #  print(newpath)
                 if not os.path.exists(newpath):
                      os.makedirs(newpath)
                      print("Directory created",newpath)
                 else:
                     print("Directory already there",newpath)

                 if os.path.exists(realdirectory):
                     print( "The cdn file is already present on ur localcomputer")
                 else:
                     print("New file will be created on localcomputer")
                     flag=1
                 f= open(realdirectory, 'w')
                 r = requests.get(url[0]) #url is a list of string [0] have the the url string
                 f.write(r.text) #write the content into the file
                 f.close()
                 #change tag depending upon  link or script
                 if(x=="link"):
                     new_link = soup.new_tag("link", rel="stylesheet",  href="cdn"+foldername+"/"+filename)
                 elif(x=="script"):
                     new_link = soup.new_tag("script" ,src="cdn"+foldername+"/"+filename)

                #  insert tag into the document
                 soup.head.append(new_link)
                 if flag:
                     with open(fullfilepath, "w") as outf:
                         outf.write(str(soup))


fullfilepath=input("Enter the complete path of ur html file[eg.,D:\cdnhandler\index.html]")
# fullfilepath="D:\cdnhandler\index.html"
directory="\\".join(fullfilepath.split('\\')[:-1])
#print(directory) this has current working directory that is without html
# calling function
cdndownload("link")
cdndownload("script")
