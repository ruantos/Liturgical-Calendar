# Web Scraping do Calendário Litúrgico - salvemaria.com.br

Este é um projeto de web scraping que coleta dados do calendário litúrgico tradicional do site salvemaria.com.br e envia as informações de cada dia litúrgico para o email do usuário.

## Descrição

Este script Python utiliza as bibliotecas BeautifulSoup (bs4), Requests, DateTime e SMTP para realizar o web scraping do calendário litúrgico e enviar as informações de cada dia litúrgico por email.

## Funcionalidades

- Coleta dados do calendário litúrgico tradicional do site salvemaria.com.br.
- Prepara as informações de cada dia litúrgico no formato específico.
- Envia as informações por email para o usuário.

## Requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- BeautifulSoup (bs4)
- Requests
- DateTime
- smtplib

Você pode instalá-las individualmente via pip:

```
pip install beautifulsoup4 requests
```
Ou pode instá-las de uma vez utilizando o arquivo requirements.txt:

```
pip install -r requirements.txt
```
## Utilização

1. Clone este repositório ou baixe os arquivo .py.
2. Configure o script com suas credenciais de email e as informações de SMTP nas variáveis de ambiente.
3. Execute o script `main.py`.
4. Verifique seu email para receber as informações do calendário litúrgico.
5. Para melhor aproveitamento, agende o script com um gerenciador de tarefas ou pythonannywhere.

## Modelo do Email

O email enviado terá o seguinte formato:

```
Missa:
Féria - 4 Classe

Calendario Mariano:

Liturgia:
Paramentos: Branco
Gloria , Sem Credo
Prefacio Pascal - 1 Jo 5,4-10  Jo 20,19-31
```

## Avisos

- Este script foi desenvolvido para fins educacionais e de uso pessoal.
- Certifique-se de usar este script de acordo com as políticas do site salvemaria.com.br e da legislação aplicável.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
