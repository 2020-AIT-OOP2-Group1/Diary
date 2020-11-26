from diaries.DiarySample import DiarySample
from SobueDiarynew import SobueDiarynew

diaries = [DiarySample(),SobueDiarynew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
