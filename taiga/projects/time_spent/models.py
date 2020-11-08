# Copyright (C) 2018 Miguel González <migonzalvar@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class TimeSpentMixin(models.Model):
    time_spent_to_date = models.IntegerField(
        default=0, verbose_name=_('time spent'),
    )

    set_in_progress_date = models.DateTimeField(
        blank=True,
        null=True,
        default=None,
        verbose_name=_('set in progress time'),
    )

    def save(self, *args, **kwargs):
        # start timer
        if self.status.name.lower() in ['in progress', 'in bearbeitung']:
            if not self.set_in_progress_date:
                self.set_in_progress_date = timezone.now()
        # add timer to time spent and remove
        elif self.set_in_progress_date:
            delta = timezone.now() - self.set_in_progress_date
            self.time_spent_to_date += divmod(delta.total_seconds(), 60)[0]
            self.set_in_progress_date = None

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
