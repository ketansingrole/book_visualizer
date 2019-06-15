from translate import Translator
translator= Translator(from_lang="en",to_lang="ta")
new = open("test.txt","r")
new2 = open("output.txt","w")
translation = translator.translate(new.read())
print(translation)
new2.write(translation)

