from diaries.AbstractDiary import AbstractDiary


class HisamatsuDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "疲れた"

    def get_author(self):
        return "久松"