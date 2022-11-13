# Curso de Udemy: https://www.udemy.com/course/python-para-el-mundo-real/
# Python para el mundo real!
# Aprende Python realizando ejercicios y aplicaciones reales.

# Is Palindrome? Python programming: Let's create a simple Python program 
# to check if a string is Palindrome or not - Let's do it in 3 different ways!

# Palindrome definition: a word, phrase, or sequence that reads the same backwards as forwards.

# Palindrome phrases:
# "No lemon No melon" | "Socorram me subi no onibus em Marrocos" | "Top spot" | "My gym" | "Anotaram a data da maratona" | "A rua Laura"
# Palindrome words:
# Racecar | Radar | Kayak | Madam | Level | Rotator | Repaper


'''💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥
# Method 1  --|--  Basic version:
💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥
'''
x = "racecar"
rev = x[::-1]

if (x == rev):
  print("Yes! The word {} is Palindrome".format(x))
else:
  print("No! The word {} is NOT Palindrome".format(x))


'''💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥
# Method 1.1  --|--  Improved version:
💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥
'''
x = "rotator"
x_lower = x.casefold()
x_split = x_lower.split(' ')
x_join = ''.join(x_split)

x_rev = x_join[::-1]
# print(x_rev)

if (x_join == x_rev):
  print("Yes! The word '{}' is Palindrome".format(x))
else:
  print("No! The word '{}' is NOT Palindrome".format(x))
  
''' 
💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥
# Method 1.3  --|--  Optimized version:
💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥
'''
x = "Top spot".casefold()
x = x.split(' ')
x = ''.join(x)
x_rev = x[::-1]

if (x == x_rev):
  print("Yes! The word '{}' is Palindrome".format(x))
else:
  print("No! The word '{}' is NOT Palindrome".format(x))
  
'''  
📝 ✏️🎀📎 🖇 📐 📏 📌 📍 ✂️ 🎊 🎉  📝 ✏️ 🎀📎🖇📐
  # Method 2  --|--  Ask the user for data input 
📝 ✏️🎀📎 🖇 📐 📏 📌 📍 ✂️ 🎊 🎉 📝 ✏️ 🎀📎 🖇📐 
  '''
user_input = str(input("Enter your word: "))
lower_user_input = user_input.casefold()
rev_user_input = reversed(lower_user_input)

if (list(lower_user_input) == list(rev_user_input)):
  print("YES!!! The word {} is palindrome.".format(user_input))
else:
  print("NOOO!!! The word {} is NOT palindrome.".format(user_input))
  
''' 
📝 ✏️🎀📎 🖇 📐 📏 📌 📍 ✂️ 🎊 🎉  📝 ✏️ 🎀📎🖇📐
  # Method 2.1  --|--  Define your own data input 
📝 ✏️🎀📎 🖇 📐 📏 📌 📍 ✂️ 🎊 🎉 📝 ✏️ 🎀📎 🖇📐 
  '''
user_input = "radar"
lower_user_input = user_input.casefold()
rev_user_input = reversed(lower_user_input)

if (list(lower_user_input) == list(rev_user_input)):
  print("YES!!! The word {} is palindrome.".format(user_input))
else:
  print("NOOO!!! The word {} is NOT palindrome.".format(user_input))
  
''' 
🔈 🔇 🔉 🔊 🔔 🔕 📣 📢 👁‍🗨 💬 💭 🗯🔈 🔇 🔉 🔊 🔔 
  # Method 3  --|--  Using for loop and temp variable 
🔈 🔇 🔉 🔊 🔔 🔕 📣 📢 👁‍🗨 💬 💭 🗯🔈 🔇 🔉 🔊 🔔 
  '''
palindrome = "rotaTOR".casefold()
rev = palindrome[::-1]
print(rev)
temp = "" 

for i in rev: 
  temp = temp + i  # temp += i
if (palindrome == temp): 
  print("YES! Is palindrome!")
else:
  print("NOOO!!!! Is NOTTTTT palindrome!")
'''  
🔈 🔇 🔉 🔊 🔔 🔕 📣 📢 👁‍🗨 💬 💭 🗯🔈 🔇 🔉 🔊 🔔 
  # Method 3.1  --|--  Optimized version: 
🔈 🔇 🔉 🔊 🔔 🔕 📣 📢 👁‍🗨 💬 💭 🗯🔈 🔇 🔉 🔊 🔔 
'''
palindrome = "Repaper".casefold()
rev = palindrome[::-1]
print(rev)
#temp = "" 

# for i in rev: 
#   temp = temp + i 
if (palindrome == rev): 
  print("YES! Is palindrome!")
else:
  print("NOOO!!!! Is NOTTTTT palindrome!")

'''
📌 📍 ✂️📌 📍 ✂️📌 📍 ✂️📌 📍 ✂️📌 📍 ✂️ 
 # What about numbers? Try this out! 
📌 📍 ✂️📌 📍 ✂️📌 📍 ✂️📌 📍 ✂️📌 📍 ✂️
'''
print("Check if your number is palindrome or not!!!")
user_input = input('Please, enter a number: ')
try:
    val = int(user_input)
    if user_input == str(user_input)[::-1]:
        print('YEAHHHH!!! The number {} is Palindrome!!!'.format(user_input))
    else:
        print('OHHHHH! The number {} is NOT a palindrome!'.format(user_input))
except ValueError:
    print("UPPPSSS! You have entered an invalid number! Try Again !")
