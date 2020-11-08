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
from django.utils import timezone

from taiga.base.api import serializers
from taiga.base.fields import Field, MethodField


class TimeSpentSerializerMixin(serializers.LightSerializer):
    time_spent_to_date = Field()
    total_time_spent = MethodField()
    time_spent_status = MethodField()

    def get_total_time_spent(self, obj):
        if obj.set_in_progress_date:
            delta = timezone.now() - obj.set_in_progress_date
            return obj.time_spent_to_date + divmod(delta.total_seconds(), 60)[0]
        else:
            return obj.time_spent_to_date

    def get_time_spent_status(self, obj):
        if obj.status and obj.status.is_closed:
            return 'no_longer_applicable'
        elif obj.set_in_progress_date:
            return 'in_progress'
        else:
            return 'stopped'
