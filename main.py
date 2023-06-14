# def string_counter(s):
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sym] = syms_counter.get(sym, 0) + 1
#
#         for sym, count in syms_counter.items():
#             print(sym, count)
#
#
# string_counter('aaaabbsbdbd')

# ДЗ (урок 1, модуль 4)

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False