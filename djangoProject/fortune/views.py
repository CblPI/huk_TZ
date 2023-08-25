from random import choices

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import RouletteCell, Round, RouletteLog, FortuneUser
from .utils import create_new_round

@csrf_protect
def spin_roulette(request):
    if request.method == 'POST':

        user = request.user

        round = Round.objects.filter(is_active=True).first()

        if not round:
            round = create_new_round()

        if round.cells.filter(is_jackpot=False).exists():
            cells = round.cells.filter(is_jackpot=False)
            cell = choices(cells, [cell.weight for cell in cells])[0]
        else:
            cell = round.cells.filter(is_jackpot=True).first()

        if not RouletteLog.objects.filter(round=round, user=user).exists():
            user.part_in_rounds += 1
            user.save()

        RouletteLog.objects.create(round=round, cell=cell, user=user)

        round.cells.remove(cell)

        if not round.cells.exists() and not round.jackpot_cell:
            round.jackpot_cell = RouletteCell.objects.filter(
                is_jackpot=True).first()

            round.is_active = False
            round.save()

        data = {'number': cell.number,
                             'jackpot': round.jackpot_cell is not None}

        return JsonResponse(data)
    else:
        return render(request, template_name='fortune/index.html')


def get_user_count(request):
    rounds = Round.objects.all().order_by('-id')

    data = []

    for r in rounds:
        data.append({'round_id': r.id, 'user_count': r.users_in_round()})
    return JsonResponse({'data': data})


def get_active_users(request):
    users = (FortuneUser.objects.filter(
        Q(is_active=True),
        ~Q(part_in_rounds=0)).order_by('-part_in_rounds').distinct())

    data = []

    for user in users:
        avg = RouletteLog.objects.filter(user=user).count()/user.part_in_rounds
        data.append({'user_id': user.id,
                     'rounds_count': user.part_in_rounds,
                     'avg': round(avg, 4)})

    return JsonResponse({'active_users': data})

