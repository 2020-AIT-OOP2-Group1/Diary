from diaries.AbstractDiary import AbstractDiary


class msd05keisuke_diary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "GitHubを頑張って理解したい。"

    def get_author(self):
        return "Masuda Keisuke"