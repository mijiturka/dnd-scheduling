import unittest

from failcalc import probability_of_failure

class SciShowVideo(unittest.TestCase):

    def test_busy_friends(self):
        # So in my hypothetical, if each person rejects one time slot,
        # there will be a time that works for everyone.
        self.assertEqual(probability_of_failure(5, 10, 1), 0)
    def test_busier_friends(self):
        # But as soon as each person rejects 2 time slots, it becomes possible
        # that our DnD campaign will fail before it even starts
        self.assertEqual(
            round(probability_of_failure(5, 10, 2), 5),
            0.00061
        )
    def test_busiest_friends(self):
        # What happens if each of us is already booked for
        # half of the 10 possible meeting times?
        # If you do the math... we have a whopping 71% chance of failure!
        self.assertEqual(
            round(probability_of_failure(5, 10, 5), 2),
            0.71
        )

    def test_party_size_small_according_to_dm_guide(self):
        # If we only have four people to deal with,
        # we'd have just better than a 50-50 chance of finding a time everyone can attend.
        self.assertEqual(
            round(probability_of_failure(4, 10, 5), 2),
            0.48
        )

    def test_party_size_max_recommended(self):
        # But if we have the maximum recommended party size, that percent drops to 15.
        self.assertEqual(
            round(probability_of_failure(6, 10, 5), 2),
            0.85
        )

    def test_party_size_max_pickier(self):
        # Meanwhile, if those six people are just a bit pickier...
        # rejecting just one more time slot... then we only have a 4% chance of succeeding
        self.assertEqual(
            round(probability_of_failure(6, 10, 6), 2),
            0.96
        )

    def test_party_size_3(self):
        # Text on screen
        self.assertEqual(
            round(probability_of_failure(3, 10, 5), 2),
            0.18
        )

    def test_work(self):
        # Maybe you set aside your dream of a years-long DnD campaign with your friends,
        # and just need to schedule a 1-hour work meeting sometime between 9 and 5 o'clock.
        # If everyone is already booked for half of those 40 hour-long slots,
        # your odds are pretty good of getting five people in a room,
        self.assertEqual(
            round(probability_of_failure(5, 40, 20), 2),
            0.25
        )

        # while six is a coin flip
        self.assertEqual(
            round(probability_of_failure(6, 40, 20), 2),
            0.52
        )

        # But if your coworkers only have prior commitments for just 10 hours per week,
        # then you can probably swing a 14-person meeting without pulling your hair out.
        self.assertEqual(
            round(probability_of_failure(14, 40, 10), 2),
            0.47
        )



class Paper(unittest.TestCase):    

    def test_histogram_red(self):
        # The histogram on the left (red) is for l=15, m=9, r=4
        # The failure probability is 0.34 for the first case

        # That is not how you round 0.346 ... physicists
        whole, fractional = str(probability_of_failure(9, 15, 4)).split('.')
        result = float(f"{whole}.{fractional[:2]}")

        self.assertEqual(
            result,
            # wolframalpha: 0.0346
            0.34
        )

    def test_histogram_blue(self):
        # The histogram on the right (blue) is for l=20, m=9, r=4
        # and 0.027 for the second case
        self.assertEqual(
            round(probability_of_failure(9, 20, 4), 3),
            # wolframalpha: 0.0274
            0.027
        )

if __name__ == '__main__':
    unittest.main()
