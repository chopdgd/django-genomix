from genomix import models, test


class TestTimeStampedLabelModel(test.ModelMixinTestCase):
    mixin = models.TimeStampedLabelModel

    def setUp(self):
        super(TestTimeStampedLabelModel, self).setUp()
        self.instance = self.model.objects.create(
            label='Label Test',
            description='description',
            active=False,
        )

    def test_fields(self):
        assert self.instance.label == 'Label Test'
        assert self.instance.description == 'description'
        assert self.instance.slug == 'label-test'
        assert self.instance.active is False
        assert str(self.instance) == 'Label Test'
