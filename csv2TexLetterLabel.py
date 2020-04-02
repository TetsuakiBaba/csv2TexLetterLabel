# coding: utf-8
import csv

message_header = 'Hello World'
message_footer = "Industrial Art, Tokyo Metropoitan University"

header=r'\documentclass[twocolumn,dvipdfmx]{article}'\
r'\usepackage[top=15truemm,bottom=15truemm,left=15truemm,right=15truemm]{geometry}'\
r'\renewcommand{\baselinestretch}{1.25}'\
r'\usepackage[utf8]{inputenc}'\
r'\usepackage{tcolorbox}'\
r'\tcbuselibrary{raster,skins}'\
r'\newtcolorbox{note}[1]{'\
 'enhanced,'\
 'skin=bicolor,'\
 r'before skip=10pt plus 10pt minus 10pt,'\
 r'after skip=10pt plus 10pt minus 10pt,'\
 r'boxrule=0.4pt,'\
 r'colframe=black,'\
 r'colback=white,'\
 r'coltitle=white,'\
 r'fonttitle=\textbf,'\
 'bottom=4pt,'\
 'top=5pt,'\
 'toprule=1pt,sharp corners,'\
 'toptitle=-12pt,'\
 'bottomtitle=1pt,'\
 r'title=\flushright \strut {#1},'\
'segmentation hidden,'\
'segmentation style={color=black},'\
'}'\
r'\newcommand{\addressbox}[3]{'\
 r'\begin{note}{\footnotesize{\textbf{'+message_header+'}}}'\
 r'\centering'\
 r'\vspace{25pt}'\
 r'〒 #1 \par'\
 r'#2 \par'\
 r'\large{#3}　様'\
 r'\vspace{25pt}'\
 r'\tcblower'\
 r'\centering'\
 r'\color{white}{\textbf{\footnotesize{'+message_footer+'}}}'\
 r'\end{note}'\
'}' \
r'\begin{document}' \
'\n'

def insert_string_to_base(target_string, insert_point, insert_string):
     return target_string[:insert_point] + insert_string + target_string[insert_point:]

f = open('personal_infomation.csv', 'r')
reader = csv.reader(f, delimiter=",")

with open('label.tex', 'w') as f:
     print(header,file=f)
     for r in reader:
          address = str(r[3])+' \\\\ ' + str(r[4])+ '\\\\ '  + str(r[5] + '\\\\' + str(r[6]))
          post =  insert_string_to_base(r[2], 3, '-')
          name = r[1]
          print('\\addressbox{%s}{%s}{%s}' % (post,address,name, file=f)    
     print(r'\end{document}', file=f)