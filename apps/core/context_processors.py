from apps.home.models import ConfiguracoesSite

def configuracoes(request):
    dados = ConfiguracoesSite.objects.all()

    for d in dados:
        site = d.tituloSite
        telefone = str(d.telefone)
        email = d.email
        end = d.endereco
        sobre = d.sobre

    return {
        'site': site,
        'telefone': telefone,
        'email': email,
        'end': end.title(),
        'sobre': sobre


    }