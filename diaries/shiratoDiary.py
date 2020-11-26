from diaries.AbstractDiary import AbstractDiary


class DiarySample(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "やることが多すぎる日だった"

    def get_author(self):
        return "白戸大智"
