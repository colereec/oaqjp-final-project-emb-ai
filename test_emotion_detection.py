#Import emotion_detector function from EmotionDetection package for unit testing.
from EmotionDetection.emotion_detection import emotion_detector
#Import unittest library for unit testing.
import unittest

#Class for emotion_detector test cases.
class TestEmotionDetector(unittest.TestCase):
    #Test cases for emotion_detector dominant emotion finder functionality.
    def test_emotion_detector(self):
        #Test for joy dominance.
        joy_test_result = emotion_detector('I am glad this happened')
        self.assertEqual(joy_test_result['dominant_emotion'], 'joy')

        #Test for anger dominance.
        anger_test_result = emotion_detector('I am really mad about this')
        self.assertEqual(anger_test_result['dominant_emotion'], 'anger')

        #Test for disgust dominance.
        disgust_test_result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust_test_result['dominant_emotion'], 'disgust')

        #Test for sadness dominance.
        sadness_test_result = emotion_detector('I am so sad about this')
        self.assertEqual(sadness_test_result['dominant_emotion'], 'sadness')

        #Test for fear dominance.
        fear_test_result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear_test_result['dominant_emotion'], 'fear')

#Run the unit tests.
unittest.main()