en_key=input("영어 단어를 입력하세요:")
if en_key!='q':
    ko_key = input("한국어 뜻을 입력하세요:")
    with open('vocabulary.txt', 'w', encoding='UTF-8') as f:
        f.write("{}: {}\n".format(en_key, ko_key))
en_key = input("영어 단어를 입력하세요:")
while en_key!='q':
    ko_key=input("한국어 뜻을 입력하세요:")
    with open('vocabulary.txt','a',encoding='UTF-8') as f:
        f.write("{}: {}\n".format(en_key,ko_key))
    en_key = input("영어 단어를 입력하세요:")