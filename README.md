# Hackaton-2022
Este repositorio contiene los entregables del hackaton del equipo "mean(girls)" con el proyecto "Autenticación incluyente", así como una guía para pobar el producto final y el catálogo de las variables utilizadas en la creación del modelo.

#### Intrucciones para probar la API

1. Ingresar a Postman mediante el siguiente link:

    https://web.postman.co/workspace/My-Workspace~2abe3400-c264-490a-8031-2648b6eabc11/request/24023029-44a8f1fe-b816-4ab3-8ca5-6fb1f7aca287

    Con los siguientes datos de acceso:

    username: meanGirls

    password: mean_girls

2. Una vez en Postman seleccion la pestaña: Body --> Raw 
   *al final del renglón (letras azules) asegurarse que esté seleccionado JSON
                                               
3. Para realizar la consulta utilizaremos un diccionario para dar valor a las variables:

{
  "id": "567",
  "edad": "",
  "tot_transacciones_anio": "",
  "tot_transacciones_medicas_anio": "",
  "gastomed_vs_gasto": "",
  "gastomed_vs_ingreso": "",
  "num_transacciones_dvisual": "",
  "num_transacciones_dauditiva": "",
  "num_transacciones_dmotriz": ""
}

Nota: Se puede consultar el ID del cliente o las variables del modelo.

4. Para probar la API se pueden ingresar los siguientes números de clientes que se clasificaron con cada perfil y de acuerdo a ello se recomiendan diversas formas de autenticación.

   124 – Cliente sin discapacidad

   298 – Cliente con discapacidad visual

   3 – Cliente con discapacidad auditiva

   567 – Cliente con discapacidad motriz
   
   Adulto mayor - [75,265960,227799,1.19,1.2,8506.39,335914.01,6609.6]

    Es importante mencionar que se está proponiendo incluir CISCO como canal de atención a clientes para aquellos identificados con discapacidad auditiva, ya que se les podría dar soporte mediante una video-llamada con un ejecutivo que manejara lenguaje de señas.

#### Archivos adicionales

Video de negocio presentando la iniciativa - https://www.canva.com/design/DAFPyd5pi-w/VAltwXQPMvt89UQHruo_6A/watch?utm_content=DAFPyd5pi-w&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink

Diccionario de datos para el desarrollo del modelo - TAD_Diccionario.xlsx

Tabla Analitica de Datos (TAD) simulada - TAD.ipynb

Código usado para desarrollar el recomendador - FnRecomendador.py

Código de Lambda AWS - lambda_handler.py

Diagrama de la implementación - Diagrama.pdf

