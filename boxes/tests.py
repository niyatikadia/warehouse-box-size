from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Box
from .services import find_best_box

class BoxSelectionTests(TestCase):
    def setUp(self):
        self.box_small = Box.objects.create(name="Small", internal_length=20, internal_width=20, internal_height=20, max_weight=5, cost=10)
        self.box_large = Box.objects.create(name="Large", internal_length=50, internal_width=50, internal_height=50, max_weight=20, cost=25)

    def test_fits_small_box(self):
        result = find_best_box(10, 10, 10, 2, [self.box_small, self.box_large])
        self.assertEqual(result.name, "Small")

    def test_overweight_no_box(self):
        result = find_best_box(10, 10, 10, 25, [self.box_small, self.box_large])
        self.assertIsNone(result)

    def test_oversized_no_box(self):
        result = find_best_box(100, 100, 100, 2, [self.box_small, self.box_large])
        self.assertIsNone(result)

    def test_cost_tiebreak(self):
        # identical fit, cheaper box should win — add this scenario explicitly
        pass
    def test_cost_tiebreak(self):
        pass