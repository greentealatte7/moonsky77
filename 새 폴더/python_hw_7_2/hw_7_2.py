# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
   class_val = 0

   def repeat_string(self, cnt, word ) :
      for _ in range(cnt) :
         print(word)
      return self

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")