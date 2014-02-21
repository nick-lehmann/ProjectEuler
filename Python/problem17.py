onetonine = len("onetwothreefourfivesixseveneightnine")
tentonineteen = len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
a = len("and")
twentytoninety = len("twentythirtyfortyfiftysixtyseventyeightyninety")
hundred = len("hundred")
thousand = len("thousand")
count = len("one") + thousand + 900*hundred + 100*onetonine + 100*twentytoninety + 891*a + 80*onetonine + 10*(onetonine + tentonineteen);

print count
