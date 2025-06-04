# Informações das instâncias EC2

Este projeto em Python possui um script simples que utiliza a biblioteca `boto3` para coletar e exibir informações de todas as instâncias EC2 em uma conta AWS. A execução do script retorna detalhes como ID da instância, tipo, estado atual e região onde está provisionada.

## Pré-requisitos

- Python 3.8 ou superior
- Biblioteca [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- Credenciais AWS configuradas (via `~/.aws/credentials` ou variáveis de ambiente)

## Instalação

1. Clone este repositório:

   ```bash
   git clone <url-do-repositorio>.git
   cd aws
   ```

2. Crie um ambiente virtual (opcional, mas recomendado) e instale as dependências:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install boto3
   ```

## Uso

O script `listar_ec2.py` (não incluído neste repositório de exemplo) se conecta à AWS e lista todas as instâncias EC2, exibindo os principais atributos.

Execute o script da seguinte forma:

```bash
python listar_ec2.py
```

O resultado será uma listagem semelhante a:

```
ID da Instância: i-0123456789abcdef0
Tipo: t2.micro
Estado: running
Região: us-east-1
```

Repita para cada instância encontrada.

## Observações

- Certifique-se de que suas credenciais possuem permissões suficientes para listar instâncias EC2 (política `AmazonEC2ReadOnlyAccess` ou semelhante).
- Para mais detalhes sobre autenticação e configuração da AWS via `boto3`, consulte a [documentação oficial](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

