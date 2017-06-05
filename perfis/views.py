# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from perfis.models import Perfil


def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == '1':
        perfil = Perfil('Flavio Almeida', 'flavio@flavio.com.br', '77777777', 'Alura')

    if perfil_id == '2':
        perfil = Perfil('Romulo Henrique', 'romulo@romulo.com.br', '123123123', 'Caelum')

    return render(request, 'perfil.html', {"perfil": perfil})

