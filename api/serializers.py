from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile




class profileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class reviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class tagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class projectSerializers(serializers.ModelSerializer):
    owner = profileSerializers(many=False)
    tags = tagSerializers(many=True)
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializers = reviewSerializers(reviews, many=True)
        return serializers.data


