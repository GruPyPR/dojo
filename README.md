# dojo Grupy-PR

Respositório contendo o código das sessões de dojo do Grupy-PR.


## Testes Unit Test e BDD

A sessões do dojo são feitas com a metodologia TDD e códigos de teste
escritos em [unittest](https://docs.python.org/3/library/unittest.html).

Alguns testes foram escritos também em BDD com [behave](http://python-behave.readthedocs.io).



### Unit Test

Para executar os testes em Unit Test, basta rodar os arquivos test_*.py

Exemplo:

    $ cd romanos_20170111
    $ python test_romanos.py


### BDD

Para executar os teste em BDD, é necessário instalar o behave primeiro:
    
    $ pip install behave


Depois basta rodar o comando behave. Exemplo:

    $ cd romanos_20170111
    $ behave


A saída do behave é mais extensa por padrão, cada passo de cada cenário é impresso. Se preferir uma saída mais compacta, parecida com a do unittest, com um ponto para cada cenário, pode rodar:

    $ behave --format progress




