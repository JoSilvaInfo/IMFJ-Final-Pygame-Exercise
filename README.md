# ExRecurso_JoanaSilva_21805651
### Feito por Joana Silva; Nº: a21805651

## Instruções de Utilização
• Para o utilizador saber o que fazer para correr o programa como jogar

## Introdução
• Este projeto vei da cadeira da Introdução à Matemática e Física para videojogos 2 (IMFJ2), da
licenciatura de videojogos.
• O objetivo é desenvolver um jogo em python e pygames, em que o jogador pode correr e saltar pelo nivel usando plataformas flutuantes, e desviando-se de obstaculos que lhe vão ser atirados.
• O projeto visa perceber se os conhecimentos adquiridos na cadeira de IMFJ2 são aplicados corretamente.

## Metodologia
• O jogo começa no Menu principal, este sendo chamado no Main.py com base na classe menu.py, com uma musica de fundo. Aqui, os jodaroes podem começar o jogo, ver as opções onde se emcontrão os controlos e a opção de tirar os soms, embora este não esteja operacional, ou fechar o jogo. Os botões estão dependentes da class butons.py.
• Após o começo de jogo, começa a main loop do jogo no Main.py. É começado por ser dezenhado as imagems de fundo. Logo, o jogo faz uma comfirmação se o jogador ainda esta vivo antes de começar a fazer os randoms e fazer updates de acordo com os valores especificados das plataformas, cannonballs, e balls.
• O jogador é instanciado em cima da plataforma do meio, assim como as plataformas e o canhão. Estes caem e assim comessa o jogo. O jogador movementa-se e salta com as setas. 
• As plataformas têm um comportamento boyante, que também é afetado pelo jogador quando este está em cima, ou salta para fora delas. 
• Em cada 30 segundos, irão cair bombas que o jogador terá que se desviar. Estas são instanciadas no Mai.py, mas estão dependentes de freefal.py. Um canhão estará tabem a disparar balas a cada 5 segundos, tambem instanciado no Main.py, mas dependente do shoot.py.
• Existem algums problemas, nomeadamente com o salto, a opção de som, o frame drop quando as bombas são instanciadas, e porvezes o calculo e trajetoria do canhão.

## Agradecimentos
• Gostaria de agradecer aos professores, assim como tambem a minha colega de curso Diana, e o meu gerente de turno, que me tentaram ajudar com o problema previo das plataformas em que todas estavam a detectar collis~~oes em simultaneo.

## Referencias
### Som:
• Os soms foram todos tirados de Freesound.org

### Imagems:
• As imagems foram todas tirados do google images, e sites como OpenGameArt.org e Vecteezy.

### ChatGPT:
• Foi usado para temtar perceber como resolver o problema referenciado anteriormente das plataformas, assim como implementar o som.

### YouTube:
How to make a Menu in Pygame: https://www.youtube.com/watch?v=2iyx8_elcYg&ab_channel=CodingWithRuss 
