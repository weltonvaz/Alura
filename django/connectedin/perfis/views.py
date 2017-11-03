# connectedin/perfis/views.py 

# código anterior omitido

def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', { "perfil" : perfil})

