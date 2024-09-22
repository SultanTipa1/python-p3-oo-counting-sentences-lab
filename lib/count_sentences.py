#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        self.value = value  # This will call the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        self._value = new_value

    def count_sentences(self):
        if not self.value:
            return 0
        # Split by sentence-ending punctuation and filter out empty strings
        sentences = re.split(r'[.!?]+', self.value)
        return len([s for s in sentences if s.strip()])

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')
