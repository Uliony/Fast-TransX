"""
Implementation of the Hit@10 metrics
"""


class HitAt10:
    """Hit@10 metrics implementation"""

    def __init__(self):
        self._total_samples_number = 0
        self._hit1_count = 0
        self._hit3_count = 0
        self._hit10_count = 0

    def clear(self):
        """Reset the metrics"""
        self._total_samples_number = 0
        self._hit1_count = 0
        self._hit3_count = 0
        self._hit10_count = 0

    def update(self, scores, ref_score, mask):
        """Update the metrics"""
        self._total_samples_number += 1

        misses_num = ((scores < ref_score) & mask).sum()

        if misses_num < 10:
            self._hit10_count += 1

        if misses_num < 3:
            self._hit3_count += 1

        if misses_num < 1:
            self._hit1_count += 1

    @property
    def hit10(self):
        """Get Hit@10 metric result"""
        return self._hit10_count / max(1, self._total_samples_number)

    @property
    def hit3(self):
        """Get Hit@3 metric result"""
        return self._hit3_count / max(1, self._total_samples_number)

    @property
    def hit1(self):
        """Get Hit@1 metric result"""
        return self._hit1_count / max(1, self._total_samples_number)

    def eval(self):
        """Get the evaluation results"""
        return self.hit10, self.hit3, self.hit1
