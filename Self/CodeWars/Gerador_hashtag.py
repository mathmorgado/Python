"""
A equipe de marketing está gastando muito tempo digitando hashtags.
Vamos ajudá-los com nosso próprio Gerador de Hashtag!

Aqui está o acordo:

Deve começar com uma hashtag ( #).
Todas as palavras devem ter a primeira letra maiúscula.
Se o resultado final for maior que 140 caracteres, ele deve retornar -false-.
Se a entrada ou o resultado for uma string vazia, ela deverá retornar -false-.

Ex:
' Hello there thanks for trying my Kata'  =>  '#HelloThereThanksForTryingMyKata'
'    Hello     World   '                  =>  '#HelloWorld'
''                                        =>  false
"""
def generate_hashtag(string):
    return '#'+''.join(list(map(lambda word: word.capitalize(), string.split(' ')))) if len(string) <= 140 and string else False


print(generate_hashtag(''))