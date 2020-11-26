from diaries.DiarySample import DiarySample
from SobueDiarynew import SobueDiarynew
from diaries.msd05keisuke_diary import msd05keisuke_diary

diaries = [DiarySample(),msd05keisuke_diary(),SobueDiarynew(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
