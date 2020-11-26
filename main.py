from diaries.DiarySample import DiarySample
from diaries.HisamatsuDiary import HisamatsuDiary

diaries = [DiarySample(),HisamatsuDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
