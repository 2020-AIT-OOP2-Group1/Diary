from diaries.DiarySample import DiarySample
from diaries.HisamatsuDiary import HisamatsuDiary
from diaries.msd05keisuke_diary import msd05keisuke_diary
from diaries.SobueDiarynew import SobueDiarynew
from diaries.shiratoDiary import shiratoDiary
from diaries.HarukiDiary import HarukiDiary
from diaries.Tanaka_new import Tanaka_new

diaries = [DiarySample(), HisamatsuDiary(), msd05keisuke_diary(), SobueDiarynew(), shiratoDiary(), HarukiDiary(), Tanaka_new()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
