from collections import defaultdict

alphabet = [
    '\x00', ' ', '৩', '১', '৪', '৮', '৯', '৭', '০', '৬', '৫', '২', '(', ',', '-', '।', ')',
    'ি', 'ৃ', 'া', 'ূ', 'ো', 'ু', 'ী', 'ে', 'ৌ', 'অ', 'ঔ', 'ঊ', 'ও', 'আ', 'ঈ', 'ঋ',
    'ঐ', 'ই', 'এ', 'উ', 'স', 'ম', 'ন', 'প', 'য', 'ণ', 'গ', 'ঘ', 'দ', 'খ', 'ক', 'ব',
    'ত', 'র', 'ল', 'ট', 'থ', 'ফ', 'ধ', 'ছ', 'হ', 'ষ', 'চ', 'শ', 'য়', 'জ', 'জ্ঞ', 'র্ধ',
    'র্ম', 'ল্প', 'ত্র', 'র্ত', 'র্গ', 'র্ট', 'প্ত', 'প্স', 'ন্দ', 'র্য', 'শ্চ', 'ক্র', 'স্থ', 'ম্প', 'ধ্য', 'শ্ব',
    'ন্য', 'দ্য', 'র্ব', 'স্ত', 'ঙ্গ', 'ত্য', 'প্র', 'ক্ষ', 'চ্চ', 'ন্ত', 'ব্দ', 'ষ্ট', 'শ্র', 'র্ষ', 'র্ক', 'স্ট',
    'গ্র', 'ত্ব', 'ং', '্'
]

alphabet_ord = [i for i in range(len(alphabet))]
# bangla [0, 1, 2, 3] english [0, 32, 33, 34]

alpha_to_num = defaultdict(int, list(map(reversed, enumerate(alphabet))))
# bangla {'\x00': 0, '৩': 1, '১': 2, '৪': 3} english {'\x00': 0, ' ': 1, '!': 2, '"': 3}

num_to_alpha = dict(enumerate(alphabet_ord))
# bangla {0: 0, 1: 1, 2: 2, 3: 3} english {0: 0, 1: 32, 2: 33, 3: 34}

class stringProcessing(object):

    def __init__(self, text):
        self.text = text
        self.sequence = self.extract()

    def is_hasant(self, char):
        return char == '\u09CD'

    def is_consonant(self, char):
        return '\u0995' <= char <= '\u09B9' or char in {'\u09DC', '\u09DD', '\u09DF'}

    def is_vowel(self, char):
        return '\u0985' <= char <= '\u0994'

    def is_digit(self, char):
        return '\u09E6' <= char <= '\u09EF'

    def is_punctuation(self, char):
        return char in {'\u0964', '\u0965', ',', ';', '?', '!', ':', '-', '—', "'", '"', '(', ')', '{', '}', '[', ']'}

    def is_others(self, char):
        return '\u0980' <= char <= '\u0983' or char == '\u09CE' or self.is_hasant(char)

    def is_diacritic(self, char):
        return '\u09BE' <= char <= '\u09CC' or char in ('\u09D7', '\u09E2', '\u09E3')

    def extract(self):
        i = 0
        res = []

        while i < len(self.text):
            # print(is_diacritic(text[i]))
            if self.text[i].isspace():
                pass
            elif i < len(self.text) - 1 and self.is_consonant(self.text[i]) and self.is_hasant(self.text[i + 1]):
                this = self.text[i:i + 2]
                i += 2
                while i < len(self.text) - 1 and self.is_consonant(self.text[i]) and self.is_hasant(self.text[i + 1]):
                    this += self.text[i:i + 2]
                    i += 2
                if self.is_consonant(self.text[i]):
                    this += self.text[i]
                res.append(this)
            else:
                res.append(self.text[i])
            i += 1
        return res

    def getSequence(self):
        return self.sequence

if __name__ == '__main__':
    text = '''সর্বোচ্চ আদালত, যা শীর্ষ আদালত বা সুপ্রিম
কোর্ট নামেও পরিচিত, আদালতের অনুক্রমের
সর্বোচ্চ স্তরে অবস্থিত।

ধূমকেতু কাজী নজরুল ইসলাম সম্পাদিত
একটি অর্ধ-সাপ্তাহিক পত্রিকা, যা ১৩২৯
বঙ্গাব্দের ২৬ শ্রাবণ (১৯২২ সালের ১১ আগস্ট)
প্রথম প্রকাশিত হয়।

০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯

বানৌজা দুরন্ত বাংলাদেশ নৌবাহিনীর একটি
টাইপ ০২৪ ক্ষেপণাস্ত্রবাহী নৌকা। এটি ১৯৮৩
থেকে ২০১৭ পর্যন্ত বাংলাদেশ নৌবাহিনীতে
সক্রিয় ছিল।

ঈশ্বরচন্দ্র বিদ্যাসাগরের পূর্বপুরুষগণ অধুনা
পশ্চিমবঙ্গের হুগলি জেলার অন্তর্গত
বনমালীপুর নামক গ্রামের অধিবাসী ছিলেন।

বহু সমালোচক, যাদের মধ্যে মৃণাল সেন ও
ঋত্বিক ঘটক অন্যতম, ছবিটিকে সত্যজিতের
প্রথম ছবিটির চেয়েও ওপরে স্থান দেন।

এসময় কল্পকাহিনী ও গোয়েন্দা কাহিনী থেকে
শুরু করে ঐতিহাসিক ছবিও তিনি বানান।

ঔষধ জীবদেহের উপর কী ক্রিয়া ও প্রতিক্রিয়া
সৃষ্টি করে সে সম্পর্কে বিজ্ঞানের বিশেষ শাখা
ফার্মাকোলজি আলোচনা করে।

ঊর্বশী হিন্দুধর্মে একজন অপ্সরা। তাকে সমস্ত
অপ্সরার মধ্যে সবচেয়ে সুন্দরী ও বিশেষজ্ঞ
নর্তকী বলে মনে করা হয়।
'''
    # text = 'টাইপ ০২৪ ক্ষেপণাস্ত্রবাহী নৌকা। এটি ১৯৮৩'
    test = stringProcessing(text)
    print(test.getSequence())