word1, word2 = input().split()

result1 = f'!{word2} ! {word1}!'
result2 = '!{word2} ! {word1}!'.format(word1=word1, word2=word2)

assert result1 == result2
print(result1, result2, sep='\n')
