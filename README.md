# Identificador Antológico

## *Um Bot para identificação de Tapirus terrestris em conjuntos de dados de fotografias.*

**Requerimentos:**

Antes de tudo, configure seu ambiente computacional, conforme as seguintes especificações:

- Sistema operacional **MS Windows** (versão *10* ou mais recente);
- Ter o **Python Anaconda** (alguma de suas versões mais recentes - [*link*](https://www.anaconda.com/products/distribution)) instalado.

**Passos (obrigatórios!) para rodar a análise:**

1) Primeiramente, faça o *download* deste repositório para sua máquina local (extraia todos os arquivos em um diretório dedicado exclusivamente para este trabalho). A opção de download fica no *botão verde*, na parte superior à direita desta página. (Ou apenas clique [aqui](https://github.com/AndersonEduardo/tapirus_detection/archive/refs/heads/main.zip)).

2) Faça download do arquivo de pesos da rede neural, a partir deste [*link*](https://drive.google.com/file/d/1sIUXOMhglIfQ8rapCSox-ohVxHZnCEE2/view). Mova o arquivo baixado para a pasta `model_weights`.

3) Para a atual versão, coloque suas fotos (formato `.jpg`) na pasta `test_images`.

4) Pelo *menu inciar* do Windows, abra o *Anaconda Prompt*;

5) Pelo *Anaconda Prompt*, navegue até o diretório contendo os aquivos extraídos deste repositório (veja o *passo 1*).

6) Estando no diretório, execute o comando **run -i true** (para a versão iterativa) ou **run -i false** (para a versão de triagem das fotos). Acompanhe **toda a execução** do programa de execução da análise. Caso haja algum problema com seu ambiente computacional ou seus dados, mensagens serão exibidas na tela durante a execução.
