# 파일 입출력

f = open('C:/STUDY/StudyPython22/temp.txt', mode='w', encoding='utf-8')

f.write('안녕하세요.\n')
f.write('저는 지동주입니다.\n')
f.write('한국사람이죠.\n')

f.close() ##필수
print('파일 생성완료')