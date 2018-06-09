# *PlantMonitor - Steps*



## Para reproduzir esse projeto siga os passos abaixo:

### Raspberry
*	Necessário iniciar uma instancia do Node-Red
  1.	Iniciar o terminal
  2.	Digitar sudo node-red-start
  3.	Pressionar enter
*	Entrar no link apresentado no terminal
*	No Node-Red, deve-se colar os flows clicando no ícone de hambúrguer no canto superior direito da tela e em Import e em Clipboard.
*	Copiar todo o conteúdo do arquivo Raspberry_NodeRed_Flows.txt
*	Uma vez copiado, será necessário colocar as coordenadas de onde está no nó “weather request location” e as Credenciais do serviço de Weather da Cloud da IBM.
  1.	OBS. Caso o nó fique com a descrição de UNKNOWN deve-se importar as bibliotecas conforme orientações no link: https://www.npmjs.com/package/node-red-node-watson
*	Criar a conexão com IBM – IoT Plataform
*	Na pasta “/pi” do raspberry colar os 3 scripts em python para que o circuito do arquivo “Projeto_Plant-Monitor_bb.jpg” funcione corretamente.


### IBM-Cloud
*	Criar um serviço de IoT “Internet of Things Platform Starter”
*	Criar a conexão do raspberry com o IBM Cloud
  1.	OBS. Caso tenha dificuldades, siga o tutorial do vídeo: https://www.youtube.com/watch?v=nlvAFwifU9c
*	Uma vez criado o serviço de IoT, entrar no link fornecido /red
*	Uma vez no Node-Red on-line, importar os flows assim como feito no Raspberry, o arquivo que contem os nós é o Raspberry_IBM-Cloud_Flows.txt
*	Há um nó de cloudant nesse fluxo, o qual armazena as informações obtidas do Raspberry em um banco de dados NoSQL, porém esse nó é opcional, caso queira, pode excluir o mesmo, se quiser o manter, será necessário criar uma tabela no cloudant (já criado pelo IoT Pltaform), basta entrar no serviço que fica no dashboard do IBM Plataform e em lauch para acessar a ferramenta do cloudant e por fim criar a tabela.
*	Provavelmente os nós de dashboard apresentaram o mesmo problema dos nós do IBM-Cloud no raspberry (UNKNOWN) deve-se importar esses nós para que funcionem corretamente, link: https://flows.nodered.org/node/node-red-dashboard
