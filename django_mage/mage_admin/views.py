import pathlib

from django.shortcuts import render, redirect

from django_mage.mage_admin.forms import SimpleDiscordCommandForm, BotSettingsForm, ServerSettingsForm, SdcSettingsForm
from django_mage.mage_admin.models import SimpleDiscordCommand, BotSettingsModel, SdcSettingsModel
from utils.SimpleCogsGenerator import SimpleCogsGenerator

from config import ROOT_DIR, DJANGO_COGS_PATHS

# Create your views here.

TEMPLATE_PATH = ROOT_DIR + "/django_mage/templates"


def bot_index(request):
    return render(request, f'{TEMPLATE_PATH}/base.html')


def sdc(request):
    sdc_list = SimpleDiscordCommand.objects.all()

    if request.method == 'POST':
        sdc = SimpleDiscordCommand.objects.filter(name=request.POST.get("name")).first()
        form = SimpleDiscordCommandForm(request.POST, instance=sdc)
        if form.is_valid():
            form.save()

    form = SimpleDiscordCommandForm

    return render(request, f'{TEMPLATE_PATH}/sdc.html', {
        'page_title': 'Simple Discord Commands',
        'sdc_list': sdc_list,
        'form': form
    })


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

    return render(request, f'{TEMPLATE_PATH}/build-output.html', {
        'page_title': 'Generated File - Simple Discord Commands',
        'output': str(file_contents)
    })


def settings_page(request):
    if request.method == 'POST':
        pass

    bot_settings_form = BotSettingsForm
    sdc_settings_form = SdcSettingsForm

    return render(request, f'{TEMPLATE_PATH}/settings-page.html', {
        'page_title': 'Settings',
        'bot_settings_form': bot_settings_form,
        'sdc_settings_form': sdc_settings_form
    })


def server_settings(request):
    if request.method == 'POST':
        _id = request.POST.get("discord_server_id")
        form_data = BotSettingsModel.objects.filter(discord_server_id=_id).first()
        form = ServerSettingsForm(request.POST, instance=form_data)
        if form.is_valid():
            form.save()

    form = ServerSettingsForm

    return render(request, f'{TEMPLATE_PATH}/bot-settings.html', {
        'page_title': 'Discord Bot Settings',
        'form': form
    })