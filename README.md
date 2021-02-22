# Coding DOJO - Napp

## Coding Dojo realizado em 20 de fevereiro de 2021.

&nbsp;
## Problema 1 - FizzBuzz

Criar uma lista de 0 a 100. No entanto, qualquer número divisível por três é substituído pela palavra 'fizz' e qualquer número divisível por cinco pela palavra 'buzz'. Os números divisíveis por 15 tornam-se 'fizzbuzz'.

Exemplo:

    1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32,

&nbsp;
## Problema 2 - Regras ABNT

Quando se lista o nome de autores de livros, artigos e outras publicações é comum que se apresente o nome do autor ou dos autores da seguinte forma: sobrenome do autor em letras maiúsculas, seguido de uma vírgula e da primeira parte do nome apenas com as iniciais maiúsculas.

Por exemplo:

- SILVA, Joao 

- COELHO, Paulo

- ARAUJO, Celso de

Seu desafio é fazer um programa que recebe um nome e imprima a versão formatada no estilo exemplificado acima.

As seguintes regras devem ser seguidas nesta formatação:
o sobrenome será igual a última parte do nome e deve ser apresentado em letras maiúsculas;

Se houver apenas uma parte no nome, ela deve ser apresentada em letras maiúsculas (sem vírgula): se a entrada for “ Guimaraes” , a saída deve ser “ GUIMARAES”;

Se a última parte do nome for igual a "FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA" ou "JUNIOR" e houver duas ou mais partes antes, a penúltima parte fará parte do sobrenome. Assim: se a entrada for "Joao Silva Neto", a saída deve ser "SILVA NETO, Joao" ; se a entrada for "Joao Neto" , a saída deve ser "NETO, Joao";

As partes do nome que não fazem parte do sobrenome devem ser impressas com a inicial maiúscula e com as demais letras minúsculas;

"da", "de", "do", "das", "dos" não fazem parte do sobrenome e não iniciam por letra maiúscula.