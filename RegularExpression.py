import re

patternURL = re.compile(r'www.{1,20}com')
patternBQG = re.compile(r'笔趣阁')



def processALine(line):
    result = ""
#     for uchar in ustring:
#         inside_code = ord(uchar)
#         if inside_code == 0x0020:
#             inside_code = 0x3000
#         else:
#             if not (0x0021 <= inside_code and inside_code <= 0x7e):
#                 rstring += uchar
#                 continue
#             inside_code += 0xfee0
#         rstring += chr(inside_code)
    return result