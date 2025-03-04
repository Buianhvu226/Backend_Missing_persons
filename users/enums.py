from django.db import models
import unicodedata

class BaseEnum(models.TextChoices):
    @classmethod
    def normalize_value(cls, value):
        """Normalize Unicode string to ASCII"""
        return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('utf-8')

    @classmethod
    def get_normalized_choices(cls):
        """Get choices with normalized values"""
        return [(choice[0], cls.normalize_value(choice[1])) for choice in cls.choices]

class Gender(BaseEnum):
    MALE = 'MALE', 'Nam'
    FEMALE = 'FEMALE', 'Nữ'
    OTHER = 'OTHER', 'Khác'

class MissingStatus(BaseEnum):
    FOUND = 'FOUND', 'Đã tìm thấy'
    MISSING = 'MISSING', 'Đang mất tích'
    SEARCHING = 'SEARCHING', 'Đang tìm kiếm'

class DiscoveryStatus(BaseEnum):
    FOUND = 'FOUND', 'Đã tìm thấy'
    SEARCHING = 'SEARCHING', 'Đang tìm kiếm'