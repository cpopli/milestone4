from rest_framework import serializers

from dapp.models import Project, Issue, IssueAssign, IssueReporter


class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueAssign
        fields = ('assignee',)


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueReporter
        fields = ('reporter',
                  )


class IssueSerializer(serializers.ModelSerializer):
    asdata = AssignSerializer(many=True)

    # redata = ReporterSerializer(many=True)
    class Meta:
        model = Issue
        fields = ('issue_id',
                  'type',
                  'issue_title',
                  'project_title_id',
                  'project_title',
                  'asdata')


class ProjectSerializer(serializers.ModelSerializer):
    items = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'project_id',
            'creator',
            'title',
            'description',
            'items')
