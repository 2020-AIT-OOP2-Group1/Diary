from diaries.DiarySample import DiarySample
from diaries.HisamatsuDiary import HisamatsuDiary
from diaries.SobueDiarynew import SobueDiarynew
from diaries.msd05keisuke_diary import msd05keisuke_diary
from diaries.HarukiDiary import HarukiDiary

diaries = [DiarySample(), HisamatsuDiary(), msd05keisuke_diary(), SobueDiarynew(), HarukiDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
