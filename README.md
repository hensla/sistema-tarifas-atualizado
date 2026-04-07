# sistema-tarifas-atualizado
Este programa calcula o valor final da passagem de transporte público com base na distância percorrida em quilômetros e na categoria do passageiro, aplicando descontos específicos para estudantes, trabalhadores e idosos.

🧠 Lógica do Programa

O menu exibe as 4 categorias disponíveis.
O usuário escolhe a categoria do passageiro.
Se a opção for válida (1 a 4), o programa solicita a distância em km.
O match/case aplica o desconto correto conforme a categoria.
O valor final é exibido formatado em reais.
Entradas inválidas exibem uma mensagem de erro.

🛠️ Tecnologias

Linguagem: Python 3.10+
Conceitos aplicados:

Entrada e conversão de dados (input, int, float)
Condicionais if/else
Estrutura match/case (Pattern Matching — Python 3.10+)
Formatação de valores monetários com f-strings (:.2f)

⚠️ Observações

O programa não aceita opções fora do intervalo 1–4 — uma mensagem de erro é exibida.
A distância em km aceita valores decimais (ex: 5.5).
Para idosos, o valor é sempre R$ 0,00 independente da distância.


💡 Possíveis Melhorias

Adicionar validação para km negativos ou zero
Permitir calcular passagens para múltiplos passageiros
Salvar o histórico de cálculos em um arquivo .txt ou .csv
Criar versão com interface gráfica (Tkinter)


📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
