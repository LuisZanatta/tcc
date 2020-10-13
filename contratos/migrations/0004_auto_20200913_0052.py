# Generated by Django 3.1 on 2020-09-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0003_auto_20200709_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='descricao_produto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='descricao_servico',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='quantidade_produto',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tipo_produto',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='aditivo',
            name='arquivo',
            field=models.FileField(upload_to='aditivos'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='arquivo',
            field=models.FileField(upload_to='contratos/', verbose_name='Arquivo do Contrato:'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='data_fim',
            field=models.DateField(verbose_name='Data de Término:'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='data_inicio',
            field=models.DateField(verbose_name='Data de Inicio:'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='motivo_cancelamento',
            field=models.TextField(blank=True, null=True, verbose_name='Motivo do Cancelamento:'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='numero_contrato',
            field=models.CharField(max_length=50, verbose_name='Nome do contrato:'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='status',
            field=models.CharField(choices=[('1', 'Ativo'), ('2', 'Concluido'), ('3', 'Cancelado')], default='1', max_length=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='tipo',
            field=models.CharField(choices=[('1', 'Serviços'), ('2', 'Produtos')], max_length=1, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor:'),
        ),
    ]