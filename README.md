# GestaoEventos
Trabalho Senac Titione Gestao de eventos Python Desktop

## 📚 Descrição do trabalho: 

Sistema de Gerenciamento de Eventos: 


* Classes:
  * Evento: atributos incluem nome do evento, data, lista de participantes.
  * Participante: atributos incluem nome, e-mail, eventos inscritos.
  * Sessao: atributos incluem tema, palestrante, horário.

* Relacionamento:
  * Um Evento pode conter várias Sessao e cada Participante pode se inscrever em múltiplas sessões.

* Comportamento Detalhado:
  * Criação de eventos com datas, horários e informações detalhadas.
  * Inscrição e desinscrição dos participantes em sessões específicas.
  * Geração de agenda personalizada para participantes com base em suas sessões.

* Funcionalidade Adicional:
  * Feedback e avaliação pós-evento, onde participantes podem avaliar as sessões e fornecer comentários.

 
## 📄 Pontos a serem avaliados:

* Qualidade do Código e Estrutura:
  * Legibilidade: O código segue as convenções do PEP 8?
  * Manutenibilidade: O código é bem organizado e fácil de entender e modificar?
  * Reutilização: Existem componentes ou classes que podem ser reutilizados em outros contextos ou projetos?
  * Uso de Padrões de Projeto: Padrões de projeto foram usados apropriadamente para resolver problemas comuns?
 
* Funcionalidade e Lógica:
  * Corretude: Todas as funcionalidades implementadas funcionam como esperado?
  * Tratamento de Erros: O sistema lida adequadamente com entradas inválidas e falhas durante a execução?
  * Persistência de Dados: Os dados são salvos e recuperados de forma correta e eficiente?
  * Testes: O sistema possui testes automatizados para garantir sua corretude e robustez?
  
* Interface do Usuário e Experiência do Usuário (UI/UX):
  * Clareza: A interface é intuitiva e as informações são fáceis de encontrar?
  * Design: A interface é visualmente agradável e consistente?
  * Responsividade: A interface responde bem a diferentes ações do usuário?
  * Acessibilidade: O sistema é acessível para usuários com diferentes habilidades?
 
* Performance e Otimização:
  * Eficiência: O sistema responde rapidamente às interações do usuário?
  * Consumo de Recursos: O sistema faz uso eficiente de memória e outros recursos?
  * Escalabilidade: O sistema pode lidar com um aumento no volume de dados ou usuários?
 
* Funcionalidades Adicionais:
  * Inovação: As funcionalidades adicionais oferecem melhorias significativas ao uso do sistema?
  * Integração: As funcionalidades adicionais estão bem integradas ao sistema existente?
  * Valor Agregado: As funcionalidades adicionais aumentam o valor do sistema para o usuário final?

## ⚙️ Instalação:

#### 1. Clonar esse repositório do Git usando o seguinte comando:
```bash
git clone https://github.com/DaniloMenezesXML/GestaoEventos.git
```
#### 2. Acessar a pasta dos arquivos clonados:
```bash
cd TrabalhoEventos
```
#### 3. Criar a venv:
```bash
python -m venv venv
```
#### 4. Ativar a venv:
```bash
.\venv\Scripts\activate
```
#### 5. Instalar as depedências: 
```bash
pip install -r requirements.txt
```
Assim, o sistema consiguirá realizar suas funções de maneira apropriada. 

## 📁 Conversão de arquivos: 

Para o software funcionar de maneira apropriada deverá ser convertido o arquivo .ui em .py da seguinte maneira:

```bash
pyside6-uic participante_ui.ui -o participante_ui.py
pyside6-uic inscricao_ui.ui -o inscricao_ui.py
pyside6-rcc icon.qrc -o resource_rc.py
```

## 🔧 Ferramentas usadas:

* Python;
* PySide6;
* QTDesign;
* SQLAlchemy;
* Pandas;

🖥️ Layout de telas:

Tela Inicio:
![1](https://github.com/DaniloMenezesXML/GestaoEventos/assets/141193621/07908ffc-c8a8-4479-945f-cce7539145a4)

Tela Agenda:
![2](https://github.com/DaniloMenezesXML/GestaoEventos/assets/141193621/7bc904fe-6183-4e61-bbb0-9fa05dbc4a6c)

Tela Participante:
![3](https://github.com/DaniloMenezesXML/GestaoEventos/assets/141193621/6b7f07e8-ed53-4785-9726-4d38e93a07e0)

Tela Criar Evento:
![4](https://github.com/DaniloMenezesXML/GestaoEventos/assets/141193621/cb3e7126-ef18-44a1-a821-dbcc03b1fb73)

Tela Criar Sessao:
![5](https://github.com/DaniloMenezesXML/GestaoEventos/assets/141193621/a2056d55-addf-4c03-9353-d364dc7ef3aa)

Tela Inscrever e Desinscrever Participante:
![6](https://github.com/DaniloMenezesXML/GestaoEventos/assets/141193621/4e492149-bde6-4466-a9e3-2056b963b5d9)

🧠 Desenvolvido por:
Os seguintes desenvolvedores foram responsáveis pelo projeto:
```
Henrique Jardel Nagao Prudêncio.
```
```
Lucas Amaral Farias.
```
```
Danilo Silva de Menezes.
```
