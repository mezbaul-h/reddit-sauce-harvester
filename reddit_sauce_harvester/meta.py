from enum import Enum


class SortChoice(Enum):
    HOT = "hot"
    NEW = "new"
    RISING = "rising"
    TOP_ALL_TIME = "top_all"
    TOP_HOUR = "top_hour"
    TOP_DAY = "top_day"
    TOP_WEEK = "top_week"
    TOP_MONTH = "top_month"
    TOP_YEAR = "top_year"


SORT_TOP_CHOICES = [choice for choice in SortChoice if choice.value.startswith("top_")]
