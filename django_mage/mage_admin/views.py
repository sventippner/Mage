import pathlib

from django.shortcuts import render, redirect

from discord_mage.models.SimpleDiscordCommand import SimpleDiscordCommand
# from django_mage.mage_admin.forms import SimpleDiscordCommandForm
from utils.SimpleCogsGenerator import SimpleCogsGenerator

from config import ROOT_DIR, DJANGO_COGS_PATHS

# Create your views here.

TEMPLATE_PATH = ROOT_DIR + "/django_mage/templates/"


def bot_index(request):
    return render(request, f'{TEMPLATE_PATH}base.html')

"""
def sdc(request):
    sdc_list = SimpleDiscordCommand.objects.all()

    if request.method == 'POST':
        sdc = SimpleDiscordCommand.objects.filter(name=request.POST.get("name")).first()
        form = SimpleDiscordCommandForm(request.POST, instance=sdc)
        if form.is_valid():
            form.save()

    form = SimpleDiscordCommandForm

    return render(request, f'{TEMPLATE_PATH}/templates/sdc.html', {
        'page_title': 'Simple Discord Commands',
        'sdc_list': sdc_list,
        'form': form
    })
"""

def del_sdc(request, name=None):
    if name:
        SimpleDiscordCommand.objects.filter(name=name).first().delete()

    return redirect('/sdc/')


def sdc_build(request):
    scg = SimpleCogsGenerator()
    sdc_list = SimpleDiscordCommand.objects.all()

    for sdc in sdc_list:
        scg.add_cog(sdc.name, sdc.output, sdc.brief, sdc.description)

    file_contents = scg.write_file(f"{DJANGO_COGS_PATHS}", True)

    return render(request, f'{TEMPLATE_PATH}build-output.html', {
        'page_title': 'Generated File - Simple Discord Commands',
        'output': str(file_contents)
    })
