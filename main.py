def string_counter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

        for sym, count in syms_counter.items():
            print(sym, count)


string_counter('aaaabbsbdbd')
