import pathlib

from django.shortcuts import render, redirect

from django_mage.mage_admin.forms import SimpleDiscordCommandForm, BotSettingsForm, ServerSettingsForm, SdcSettingsForm
from django_mage.mage_admin.models import SimpleDiscordCommand, BotSettingsModel, SdcSettingsModel, ServerSettingsModel
from django_mage.view_helper import get_server_list, get_server_data
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
    # init forms and fields
    sdc_form_data = SdcSettingsModel.objects.all().first()
    sdc_settings_form = SdcSettingsForm(instance=sdc_form_data)

    bot_form_data = BotSettingsModel.objects.all().first()
    bot_settings_form = BotSettingsForm(instance=bot_form_data)

    # check for updates
    if request.method == 'POST':
        # sdc settings form
        sdc_settings_form = SdcSettingsForm(request.POST, instance=sdc_form_data)
        if sdc_settings_form.is_valid():
            sdc_settings_form.save()

        # bot settings form
        bot_settings_form = BotSettingsForm(request.POST, instance=bot_form_data)
        if bot_settings_form.is_valid():
            bot_settings_form.save()



    # build website
    return render(request, f'{TEMPLATE_PATH}/settings-page.html', {
        'page_title': 'Settings',
        'bot_settings_form': bot_settings_form,
        'sdc_settings_form': sdc_settings_form,
        'server_list': get_server_list()
    })


def server_settings_page(request, id=None):
    form_data = ServerSettingsModel()
    message = None

    server_data = None
    if id:
        server_data = get_server_data(id)

    if request.method == 'POST':
        server_data.bot_prefix = request.POST.get("bot_prefix")
        server_data.points_name = request.POST.get("points_name")
        server_data.save()
        message = "Daten wurden gespeichert."

    form_data.bot_prefix = server_data.bot_prefix
    form_data.points_name = server_data.points_name

    form = ServerSettingsForm(instance=form_data)

    return render(request, f'{TEMPLATE_PATH}/server-settings-page.html', {
        'page_title': 'Discord Bot Settings',
        'form': form,
        'server_data': server_data,
        'message': message
    })