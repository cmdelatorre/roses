from django.db import models
from django.core.urlresolvers import reverse


NAME_MAX_LEN = 256
SKILL_NAME_MAX_LEN = 1024


class Role(models.Model):
    name = models.CharField(max_length=NAME_MAX_LEN)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skills:roles')


class Seniority(models.Model):
    name = models.CharField(max_length=NAME_MAX_LEN)
    rank = models.PositiveSmallIntegerField()
    role = models.ForeignKey('skills.Role', related_name='seniorities')

    def __str__(self):
        return '{self.role} - {self.name}'.format(self=self)

    def get_absolute_url(self):
        return reverse('skills:seniority_update', kwargs={'pk': self.pk})

class Skill(models.Model):
    name = models.CharField(max_length=SKILL_NAME_MAX_LEN)
    seniority = models.ManyToManyField('skills.Seniority',
                                       through='skills.SenioritySkills',
                                       related_name='skills')

    def __str__(self):
        return self.name

    def related_seniorities(self):
        # For the admin
        return ['{ss.seniority}: {ss.level}'.format(ss=ss)
                for ss in self.seniority_levels.all()]
    #related_seniorities.short_description = 'Related seniorities'

class SenioritySkills(models.Model):
    NONE = 'none'
    LOW = 'low'
    MID = 'mid'
    HIGH = 'high'
    EXPERT = 'expert'
    LEVEL_CHOICES = (
        (NONE, 'None'),
        (LOW, 'Low'),
        (MID, 'Medium'),
        (HIGH, 'High'),
        (EXPERT, 'Expert'),
    )
    seniority = models.ForeignKey('skills.Seniority',
                                  related_name='skill_levels')
    skill = models.ForeignKey('skills.Skill',
                              related_name='seniority_levels')
    level = models.CharField(choices=LEVEL_CHOICES, max_length=NAME_MAX_LEN)

    def __str__(self):
        return '{ss.seniority} -- {ss.skill}: {ss.level}'.format(ss=self)