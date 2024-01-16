import unittest as ut
from generator import generate_audio, validate_input_text
import os


class AppTests(ut.TestCase):

    def test_generateaudio(self):
        generate_audio("This is test text sample", "test.wav")

        self.assertTrue("test.wav" in os.listdir("."))

        os.remove("test.wav")

    def test_validation(self):
        self.assertFalse(validate_input_text("a"))
        self.assertFalse(validate_input_text("a" * 101))
        self.assertTrue(validate_input_text("a" * 25))
