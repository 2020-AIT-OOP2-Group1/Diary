from diaries.AbstractDiary import AbstractDiary


class HarukiDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "Gitを頑張りたい"

    def get_author(self):
        return "Haruki"
