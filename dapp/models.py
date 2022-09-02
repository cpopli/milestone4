from django.db import models


class Project(models.Model):
    project_id = models.CharField(max_length=200, blank=False, default='')
    creator = models.CharField(max_length=200, blank=False, default='')
    title = models.CharField(max_length=70, blank=False, default='', primary_key=False)
    description = models.CharField(max_length=200, blank=False, default='')


class Issue(models.Model):
    issue_id = models.CharField(max_length=200, blank=False, default='')
    type = models.CharField(max_length=200, blank=False, default='')
    issue_title = models.CharField(max_length=200, blank=False, default='')
    issue_description = models.CharField(max_length=200, blank=False, default=''),
    project_title = models.ForeignKey(to=Project, related_name='items', on_delete=models.CASCADE)


class IssueAssign(models.Model):
    issue_id = models.ForeignKey(to=Issue, related_name='asdata', on_delete=models.CASCADE)
    assignee = models.CharField(max_length=200, blank=False, default='')


class IssueReporter(models.Model):
    issue_id = models.ForeignKey(to=Issue, related_name='redata', on_delete=models.CASCADE)
    reporter = models.CharField(max_length=200, blank=False, default='')
