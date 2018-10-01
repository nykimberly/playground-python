from timeit import timeit

N=500000

pop_end = timeit('c.pop()', setup=f'c=list(range({N}))', number=N)
pop_beg = timeit('c.pop(0)', setup=f'c=list(range({N}))', number=N)
print(f"pop() completed in {pop_end} seconds"\
        f"\npop(0) completed in {pop_beg} seconds!")

# pop() completed in 0.04164045899960911 secondspop(0) completed in {pop_beg} seconds!
# ╭─  …/pop_time-complexity                                                                                                master   20:23:45 
# ╰─ python3 main.py
# pop() completed in 0.0413246690004598
