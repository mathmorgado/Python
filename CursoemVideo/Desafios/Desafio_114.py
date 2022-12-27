import urllib.request

try:
      pudim = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
      print('Erro na conexão com a internet ou URL não encontrada!')
else:
      print('Conexão estabelecida com sucesso!')