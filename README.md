# CDN-Handler
The CDN handler is a python script written for automatically reading into html file getting all the stylesheet or js CDN ,downloading them into specific folder and linking those files to your html file .Its useful when we want our project to run online as well .

## How to Use
1.download the python file cdnhandler.py
2.pip install requests 
3.pip install  bs4
4.give absolute path of ur html file 
5.check ur html file head ur cdns are on local host now with there dependency downloaded in cdncss and cdnjs folder 

###NOTE: the cdn should have proper url for example : https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css (i.e complete url including the http and https)
