"""TweetRate Library

Stores number of tweets per hour, minute, and/or second, with decreasing
retention for increasing granularity
    per hour stored for last year
    per minute stored for last 30d
    per second stored for last 7d

Exposes,
    post_tweet(tweet_id: str) -> None
        API for adding tweets to buckets
    get_tweet_counts(
        start: datetime,
        end: datetime,
        granularity: Granularity
    ) -> List[int]
        API for retrieving tweet counts per bucket at specified granularity
"""

from __future__ import annotations
from typing import DefaultDict, List

from collections import defaultdict
from datetime import datetime, timedelta
from enum import Enum

import pytz

TIMESTAMP_FMT = "%Y-%m-%d %H:%M"


class Granularity(Enum):
    PER_HOUR = 1
    PER_MINUTE = 2
    PER_SECOND = 3


def get_current_time(timezone: str = "America/Los_Angeles") -> datetime:
    utc_dt = datetime.utcnow()
    pst_dt = utc_dt.replace(tzinfo=pytz.timezone("UTC")).astimezone(
        pytz.timezone(timezone))
    return pst_dt


class Tweet:
    def __init__(self, tweet_id: str):
        self.tweet_id = tweet_id
        self.ts = get_current_time()


class TweetRate:
    GRANULARITY_TO_BUCKET = {
        Granularity.PER_SECOND: "per_second",
        Granularity.PER_MINUTE: "per_minute",
        Granularity.PER_HOUR: "per_hour",
    }

    GRANULARITY_TO_DT_REPLACE = {
        Granularity.PER_SECOND: ["microsecond"],
        Granularity.PER_MINUTE: ["second", "microsecond"],
        Granularity.PER_HOUR: ["minute", "second", "microsecond"],
    }

    GRANULARITY_TO_DT_DELTA = {
        Granularity.PER_SECOND: "seconds", Granularity.PER_MINUTE: "minutes",
        Granularity.PER_HOUR: "hours"
    }

    def __init__(self) -> None:
        self.per_second: DefaultDict[datetime, int] = defaultdict(set)
        self.per_minute: DefaultDict[datetime, int] = defaultdict(set)
        self.per_hour: DefaultDict[datetime, int] = defaultdict(set)

    def post_tweet(self, tweet_id: str) -> None:
        """Post tweet to all buckets"""
        tweet = Tweet(tweet_id=tweet_id)
        ts_s = tweet.ts.replace(microsecond=0)
        self.per_second[ts_s].add(tweet)
        ts_m = tweet.ts.replace(second=0, microsecond=0)
        self.per_minute[ts_m].add(tweet)
        ts_h = tweet.ts.replace(minute=0, second=0, microsecond=0)
        self.per_hour[ts_h].add(tweet)

    def _dt_at_granularity(self, dt: datetime, granularity: Granularity) -> dt:
        """Convert start and end to dt at specified granularity."""
        replace_kwargs = {
            arg: 0 for arg in TweetRate.GRANULARITY_TO_DT_REPLACE[granularity]
        }
        return dt.replace(**replace_kwargs)

    def _bucket_at_granularity(
            self, granularity: Granularity) -> DefaultDict[datetime, int]:
        """Get bucket at specified granularity."""
        bucket = getattr(self, TweetRate.GRANULARITY_TO_BUCKET[granularity])
        if bucket:
            return bucket
        else:
            raise Exception(f"Not Implemented {granularity}")

    def _timdelta_at_granularity(self, granularity: Granularity) -> timedelta:
        """Get timedelta at specified granularity."""
        delta_kwargs = {TweetRate.GRANULARITY_TO_DT_DELTA[granularity]: 1}
        return timedelta(**delta_kwargs)

    def get_tweet_counts(self, start: datetime, end: datetime,
                         granularity: Granularity) -> List[int]:
        """Return counts per granularity increment between start and end."""
        start_dt = self._dt_at_granularity(start, granularity)
        end_dt = self._dt_at_granularity(end, granularity)
        bucket = self._bucket_at_granularity(granularity)
        tweet_counts = []
        curr_dt = start_dt
        while curr_dt < end_dt:
            tweet_counts.append(len(bucket.get(curr_dt, set())))
            curr_dt += self._timdelta_at_granularity(granularity)
        return tweet_counts
