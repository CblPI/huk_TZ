import random
from .models import Round, RouletteCell

state_rulet = [20, 100, 45, 70, 15,
               140, 20, 20, 140, 45, 0]



def create_new_round():
    round = Round.objects.create()

    cells = []

    for num in range(1, 11):
        RouletteCell.objects.filter(number=num).update(
            weight=random.randint(1, 200))
        obj = RouletteCell.objects.filter(number=num).first()
        cells.append(obj)

    cells.append(RouletteCell.objects.filter(number=11).first())
    round.cells.set(cells)

    return round



# def create_new_round():
#     round = Round.objects.create()
#
#     cells = []
#
#     for num in range(1, 11):
#         obj = RouletteCell.objects.create(number=num,
#                                           weight=random.randint(1, 200))
#         cells.append(obj)
#
#     cells.append(RouletteCell.objects.create(number=11,
#                                              weight=200,
#                                              is_jackpot=True))
#
#     round.cells.set(cells)
#
#     return round