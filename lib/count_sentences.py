#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self.value = value

  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if type(value) ==str:
      self._value = value
    else:
      print("The value must be a string.")
  def is_sentence(self):
    return self.value.endswith(".")
  def is_question(self):
    return self.value.endswith("?")
  def is_exclamation(self):
    return self.value.endswith("!")
  def count_sentences(self):
        modified_value = self.value.replace("!", ".").replace("?", ".")
        sentences = [sentence.strip() for sentence in modified_value.split(".") if sentence.strip()]
        return len(sentences)

