from django.db import models

OPCOES_MARCA = [
    ('HONDA', 'Honda'),
    ('YAMAHA', 'Yamaha'),
    ('BMW', 'BMW'),
    ('AUDI', 'Audi'),
    ('FIAT', 'Fiat'),
    ('CHEVROLET', 'Chevrolet'),
    ('VOLVO', 'Volvo'),
    ('IVECO', 'Iveco'),
    ('DUCATI', 'Ducati'),
    ('HYUNDAI', 'Hyundai'),
    ('TRIUMPH', 'Triumph'),
]

OPCOES_VEICULO = [
    ('MOTO', 'Moto'),
    ('CARRO', 'Carro'),
    ('VANS', 'Vans'),
    ('CAMINHOES', 'Caminhoes'),
]


def upload_to(instance, filename):
    veiculo_id = instance.veiculo.id
    numero = instance.veiculo.fotos.count() + 1
    nome, ext = filename.split('.')
    nome_arquivo = f'{veiculo_id}_{nome}_{numero}.{ext}'
    return f'foto/{nome_arquivo}'


class Veiculo(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    marca = models.CharField(max_length=30, choices=OPCOES_MARCA, default='')
    ano = models.CharField(max_length=12, null=False, blank=False)
    km = models.FloatField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    tipo = models.CharField(max_length=30, choices=OPCOES_VEICULO, default='')
    legenda = models.TextField(max_length=80, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    veiculo = models.ForeignKey(Veiculo, related_name='fotos', on_delete=models.CASCADE, default=1)
    imagem = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return f'Foto {self.pk} - Veiculo {self.veiculo.nome}'

