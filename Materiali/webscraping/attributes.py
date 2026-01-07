from bs4 import BeautifulSoup 

testTag = BeautifulSoup("<div class='testTag'></div>",'lxml')
tag2 = testTag.div
print(tag2['class'])
# ['testTag']

tag2['class'] = 'Online-Learning'
tag2['style'] = '2023'
print(tag2)
#  <div class="Online-Learning" style="2023"></div>

del tag2['style']
print(tag2)
#  <div class="Online-Learning"></div>

del tag2['class']
print(tag2)
# <b SecondAttribute="2">testTag2</b> >>>

del tag2['SecondAttribute']
print(tag2)
# <b>testTag2</b>

print(tag2['class'])
# 'Online-Learning'

print(tag2['style'])
# KeyError: 'style'
