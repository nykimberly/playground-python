#!/usr/local/bin/envwrap PATH=.:..:../..:../../.. shebang-test
#
# Copyright 2022 Quip

from __future__ import annotations

from datetime import timedelta

import lib.test
import lib.twitter


class TweetRateTest(lib.test.TestCase):
    def test_get_tweet_counts(self) -> None:
        rater = lib.twitter.TweetRate()
        rater.post_tweet("test_tweet_1")
        counts = rater.get_tweet_counts(
            lib.twitter.get_current_time(),
            lib.twitter.get_current_time() + timedelta(hours=1),
            lib.twitter.Granularity.PER_HOUR)
        self.assertEqual(counts, [1])


def main() -> None:
    lib.test.main()
