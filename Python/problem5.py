i = 1
for d in range(2,21):
    if i % d != 0:
        for new in range(2, 21):
            if(i * new) % d == 0:
                i = i*new
                break

print i
