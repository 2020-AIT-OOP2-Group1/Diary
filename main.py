from diaries.DiarySample import DiarySample
from shiratoDiary import shiratoDiary
diaries = [DiarySample(), shiratoDiary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
