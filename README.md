# Análise e Projeto de Algoritmo

### Descrição do Projeto
O projeto final de Análise e Projeto de algoritmo(APA) propõe que resolvemos algumas instâncias do problema de roteamento de veículo (VRP) e com isso tivemos que implementar pelo menos uma heurística construtiva, três movimentos de vizinhança e um algoritmo de busca local chamado VND. 

Para uma descrição mais detalhada do projeto [clique aqui](description/Trabalho_final.pdf).

***

## Algoritmos Implementados
<!--ts-->
* Heurística Construtiva
    * Vizinho Mais Proximo
    * Vizinho Mais Próximo e uma Busca Local para o TSP da instância e depois fizemos a separação dessa rota para se encaixar com o problema do projeto.
        * Como foi implementado depois da entrega do projeto a saída do programa na função Main() apenas terá o algoritmo do vizinho mais próximo como heurística construtiva.
* Movimentos de Vizinhança.
    * Intra-Rotas
        * 2-OPT
        * Swap
        * Uma modificação do 2-OPT
* Algoritmo de busca local
    * VND(Variable Neighborhood Descent).
<!--te-->

***

## Pré-requisitos
Antes de testar em sua máquina verifique se tudo listado abaixo está instalado.
<!--ts-->
* [Python 3](https://www.python.org)
* [Numpy](https://numpy.org)
* [Pandas](https://pandas.pydata.org)
<!--te-->

*** 

## Rodando o Projeto
Para executar o projeto basta fazer no terminal
```bash
# Clonar o repositorio
git clone git@github.com:italonicacio/APA-Projeto-Final.git

# Abra a pasta do projeto
cd APA-Projeto-Final

# Vá para a pastar src 
cd src

# Execute o arquivo main.py
python3 main.py
```
Ao executar o programa ele vai chamar a função main() onde apenas fará a execução do programa quando foi feito para a entrega do projeto.
 
Para testar a execução do programa com as instâncias da copa basta alterar esse trecho do código de. 

```python
if __name__ == "__main__":
    Main()
```

Para.

```python
if __name__ == "__main__":
    MainCup()
```

Uma observação, a heurística construtiva que faz o uso do TSP para gerar uma rota que será separada em outras rotas para o VRP está com um custo de tempo alto.

Para o uso dessa heurística construtiva alterar a chamada da função abaixo de.

```python
CreateDataForTable(problem, problem.NearestNeighbor)
```

Para.

```python
CreateDataForTable(problem, problem.HeuristicTest)
```


