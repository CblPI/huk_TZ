from django.db import models
from django.contrib.auth.models import AbstractUser


class RouletteCell(models.Model):
    """Модель ячейки"""
    weight = models.IntegerField()
    number = models.IntegerField(default=0)
    is_jackpot = models.BooleanField(default=False)


class Round(models.Model):
    """Модель раунда"""
    cells = models.ManyToManyField(to='RouletteCell')
    jackpot_cell = models.ForeignKey(to='RouletteCell',
                                     on_delete=models.PROTECT,
                                     related_name='jackpot_round',
                                     null=True)

    is_active = models.BooleanField(default=True)

    def users_in_round(self):
        """Метод для получения кол-ва участников рулетки"""
        ussr = []
        for roulettelogs in self.roulettelogs.all():
            if roulettelogs.user not in ussr:
                ussr.append(roulettelogs.user)

        return len(ussr)


class RouletteLog(models.Model):
    """Модель логов"""
    round = models.ForeignKey(Round,
                              on_delete=models.PROTECT,
                              related_name='roulettelogs')

    cell = models.ForeignKey(RouletteCell,
                             on_delete=models.PROTECT,
                             related_name='roulettelogs')

    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(to='FortuneUser',
                             on_delete=models.PROTECT,
                             related_name='roulettelogs', null=True)


class FortuneUser(AbstractUser):
    """Модель пользователеля"""
    part_in_rounds = models.PositiveIntegerField(default=0)
