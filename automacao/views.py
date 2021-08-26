from django.shortcuts import render
from automacao.forms import AutomacaoForms
from automacao.calculo import AutomacaoCalculo

def index(request):
  if request.method == "GET":
    form = AutomacaoForms()
    contexto = {'form':form}
    return render(request, 'index.html', context=contexto)
  else:
    form = AutomacaoForms(request.POST)
    if form.is_valid:
      peso = form.data['peso']
      cilindros = form.data['cilindros']
      aceleracao = form.data['aceleracao']
      anomodelo = form.data['anomodelo']
      calculo = AutomacaoCalculo(peso, cilindros, aceleracao, anomodelo)
      aValor = calculo.calcular()

    form = AutomacaoForms()
    if aValor:
      sRetorno = f'A sua autonomia será de {aValor[0][0]:.1f} km por litro'
      sDesempenho = f'O desenho da RNA foi de {aValor[1]:.1f} - quanto mais próximo de 1, mais próximo dos dados reais'

      contexto = {'form':form, 'retorno':sRetorno, 'desempenho':sDesempenho}
    else:
      contexto = {'form':form}

    return render(request, 'index.html', context=contexto)
