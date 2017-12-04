from django.db import connection
from django.db.models.base import ModelBase
from django.test import TestCase


class ModelMixinTestCase(TestCase):
    """
    Base class for tests of model mixins. To use, subclass and specify
    the mixin class variable. A model using the mixin will be made
    available in self.model.
    """

    def setUp(self):
        """Create a dummy model which extends the mixin"""
        self.model = ModelBase(
            '__TestModel__' + self.mixin.__name__,
            (self.mixin,),
            {'__module__': self.mixin.__module__}
        )

        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(self.model)

    def tearDown(self):
        """Delete the schema for the test model"""
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(self.model)
