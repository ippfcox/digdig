#!usr/bin/python

from defs import ManagePath
from html.parser import HTMLParser
import time

filepath = ManagePath.gettargethtm()

print('待处理文件路径:' + filepath)

currentfilename = ManagePath.getprjdir() + 'output' + time.strftime("%Y%m%d%H%M%S", time.localtime())  + '.log'
output = open(currentfilename, 'w', encoding = 'utf-8')

class aparser(HTMLParser):
    count = {'f-wrap' : 0, 'f-info' : 0, 'ui-mr8' : 0, 'c_tx_qnamecard' : 0, 'comments_content' : 0, 'ui-mr10_state' : 0}
    tag_f_info = 0
    tag_c_tx_qnamecard = 0
    tag_comments_content = 0
    tag_ui_mr10_state = 0
    
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for name, value in attrs:
                #这个条件不错，有455个匹配
                if name == 'class' and value == 'f-wrap':
                    self.count['f-wrap'] = self.count['f-wrap'] + 1
                if name == 'class' and value == 'f-info':
                    self.count['f-info'] = self.count['f-info'] + 1
                    self.tag_f_info = 1
                if name == 'class' and value == 'comments_content':
                    self.count['comments_content'] = self.count['comments_content'] + 1
                    self.tag_comments_content = 1
        if tag == 'a':
            for name, value in attrs:
                if name == 'class' and value == 'c_tx q_namecard':
                    self.count['c_tx_qnamecard'] = self.count['c_tx_qnamecard'] + 1
                    self.tag_c_tx_qnamecard = 1
        if tag == 'span':
            for name, value in attrs:
                if name == 'class' and value == ' ui-mr10 state':
                    self.count['ui-mr10_state'] = self.count['ui-mr10_state'] + 1
                    self.tag_ui_mr10_state = 1
    def handle_endtag(self, tag):
         if tag == 'div':
            output.write('\n')
            self.tag_comments_content = 0
            self.tag_c_tx_qnamecard = 0
#        if tag == 'a':
            
    def handle_data(self, data):
        if(self.tag_f_info == 1):
            output.write( '\n----\n[feed]:' + data + '\n')
            self.tag_f_info = 0
        if(self.tag_c_tx_qnamecard == 1):
#            output.write('\t[person]:' + data + '\n')
            output.write(data)
#            self.tag_c_tx_qnamecard = 0
#        if(self.tag_comments_content == 1):
#            output.write('\t[comment]:' + data + '\n')
#            self.tag_comments_content = 0
#           self.tag_c_tx_qnamecard = 0
#        if(self.tag_ui_mr10_state == 1):
#            output.write('\n')
#            output.write('\t[time]:' + data + '\n')
#            self.tag_ui_mr10_state = 0

parser = aparser()

htmcontent = open(filepath, 'r', encoding = 'utf-8')
htmstr = htmcontent.read()
htmcontent.close()

parser.feed(htmstr)

print(parser.count)
#print(len(htmstr))

#output.write(str(parser.tmp))
output.close()

fid = open(currentfilename, 'r', encoding = 'utf-8')
lines = fid.readlines()
fid.close()
newlines = ''
for line in lines:
    if line.strip() != '':
        newlines = newlines + line
output2 = open(currentfilename, 'w', encoding = 'utf-8')
output2.write(newlines)
output2.close()
