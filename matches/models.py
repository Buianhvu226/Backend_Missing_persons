import uuid
from django.db import models
from django.utils.timezone import now
from reports.models import MissingReport, SightingReport

class AIMatch(models.Model):
    match_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    missing_report = models.ForeignKey(MissingReport, on_delete=models.CASCADE)
    sighting_report = models.ForeignKey(SightingReport, on_delete=models.CASCADE)
    face_similarity = models.FloatField()
    text_similarity = models.FloatField()
    match_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')])
    analyzed_at = models.DateTimeField(default=now)

    @property
    def combined_score(self):
        return 0.7 * self.face_similarity + 0.3 * self.text_similarity
