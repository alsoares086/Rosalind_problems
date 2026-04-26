'''
Given: A string s  of length at most 200 letters and four integers a , b, c and d

Return: The slice of this string from indices a through b and c through d
 (with space in between), inclusively. In other words, we should include elements s[b]
 and s[d] in our slice.

'''

text = 'wAFrp63vxtCUM31RV2DL2EUs2zjfa80mgsKY6t6rUHxcb72SaglybRD6cdOoe9PThCChrysemysqf3NxWjN5Rn7pkvpcI5V4KYc34b7LkMb29xdGFtMe1lxWOGeGIfchGsWAmrwX9klGOaRuPKpendulinusJQYXma1M920evCbMk1bh'
a = 66
b = 74
c = 146
d = 155

print(text[a:b+1], text[c:d+1]) # +1 porque o fatiamento em Python não inclui o índice final (b e d)

