# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20160824_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprofilerole',
            name='role',
            field=models.CharField(help_text='function performed by the responsible party', max_length=255, choices=[(b'author', 'kelompok yang membuat'), (b'processor', 'kelompok yang telah memproses dan memperbaharui data'), (b'publisher', 'kelompok yang mempublikasikan'), (b'custodian', 'pihak yang menerima akuntabilitas dan tanggung jawab atas data dan memastikan perawatan yang tepat dan pemeliharaan sumber daya'), (b'pointOfContact', 'kelompok yang dapat dihubungi untuk memperoleh pengetahuan mengenai pengadaan'), (b'distributor', 'kelompok yang mendistribusikan'), (b'user', 'kelompok yang menggunakan'), (b'resourceProvider', 'kelompok yang menyediakan'), (b'originator', 'kelompok yang membuat'), (b'owner', 'kelompok yang memiliki'), (b'principalInvestigator', 'kelompok kunci yang bertanggungjawab untuk mengumpulkan informasi dan melaksanakan penelitian')]),
        ),
    ]
