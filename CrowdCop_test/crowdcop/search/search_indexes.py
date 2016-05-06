import datetime
from haystack import indexes
from .models import Campaign

class CampaignIndex(indexes.SearchIndex, indexes.Indexable):
	campaign_title=indexes.CharField(document=True, use_template=True)
	campaign_description=indexes.CharField(model_attr='campaign_description')

	def get_model(self):
		return Campaign

	def index_queryset(self, using=None):
		return self.get_model().objects
