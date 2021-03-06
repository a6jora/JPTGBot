from ChapterClass import ChapterClass


class ChapterAdjectiveClass(ChapterClass):

    def __init__(self):
        dictionary = {'良い': 'いい', 'хороший': 'いい',
                      '悪い': 'わるい', 'плохой': 'わるい',
                      '大きい': 'おおきい', 'большой': 'おおきい',
                      '小さい': 'ちいさい', 'маленький': 'ちいさい',
                      '高い': 'たかい', 'высокий': 'たかい',
                      '低い': 'ひくい', 'низкий': 'ひくい',
                      '広い': 'ひろい', 'широкий': 'ひろい',
                      '狭い': 'せまい', 'узкий': 'せまい',
                      '重い': 'おもい', 'тяжелый (о весе)': 'おもい',
                      '軽い': 'かるい', 'легкий (о весе)': 'かるい',
                      '新しい': 'あたらしい', 'новый': 'あたらしい',
                      '古い': 'ふるい', 'старый': 'ふるい',
                      '面白い': 'おもしろい', 'интересный': 'おもしろい',
                      '詰まらない': 'つまらない', 'скучный': 'つまらない',
                      '綺麗': 'きれい', 'чистый, красивый': 'きれい',
                      '汚い': 'きたない', 'грязный': 'きたない',
                      '寒い': 'さむい', 'холодный (о погоде)': 'さむい',
                      '暑い': 'あつい', 'жаркий (о погоде)': 'あつい',
                      '簡単': 'かんたん', 'легкий, простой (о понимании)': 'かんたん',
                      '便利': 'べんり', 'удобный': 'べんり',
                      '元気': 'げんき', 'бодрый, активный, здоровый': 'げんき'}
        super().__init__(dictionary)
