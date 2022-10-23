import json as js

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
        
    ------
    Está función recibe los valores de las variables utilizadas para el modelo de recomendación 
       según el tipo de cliente
       Variables:
                  y = id cliente
                 x0 = edad
                 x1 = tot_transacciones_anio
                 x2 = tot_transacciones_medicas_anio
                 x3 = gastomed_vs_gasto
                 x4 = gastomed_vs_ingreso
                 x5 = num_transacciones_dvisual
                 x6 = num_transacciones_dauditiva
                 x7 = num_transacciones_dmotriz

    Nota. Para este ejemplo, se dejaron cuatro opciones de ids de clientes predefinidos y la opción de meter los valores de las variables 
          debido a que no se cuenta con una base de datos a la cual conectarse, pero se podría realizar un ETL que reciba la información, 
          haga el tratamiento de las variables, lo deposite en una tabla, la cual consultaríamos desde la lambda para tomar los valores y ejecutar el modelo de recomendación 
          (El modelo también se puede guardar en un archivo binario y utilizarse en la lambda, sólo tendríamos que installar las librerías y cargar los archivos necesarios).
    """
    
    cl = {0:'Cliente sin discapacidad',
          1:'Cliente con discapacidad motriz',
          2:'Cliente con discapacidad visual',
          3:'Cliente con discapacidad auditiva'}
    
    
    if event["id"] == '124':
        x0,x1,x2,x3,x4,x5,x6,x7 = [45,252998,225682,3,3.3,5301.5,1863.7,5916.9]
    elif event["id"] == '567':    
        x0,x1,x2,x3,x4,x5,x6,x7 = [44,126898,252804,0.9,0.94,5937,1497,11662.9]
    elif event["id"] == '298':
        x0,x1,x2,x3,x4,x5,x6,x7 = [44.8,374598,256180.03,0.9,0.948,12443.36,1413,1036.16]
    elif event["id"] == '3':
        x0,x1,x2,x3,x4,x5,x6,x7 = [44.7,265960,227799,1.19,1.2,8506.39,335914.01,6609.6]
    else:
         x0,x1,x2,x3,x4,x5,x6,x7 = [int(event["edad"]),int(event["tot_transacciones_anio"]),int(event["tot_transacciones_medicas_anio"]),int(event["gastomed_vs_gasto"]),int(event["gastomed_vs_ingreso"]),int(event["num_transacciones_dvisual"]),int(event["num_transacciones_dauditiva"]),int(event["num_transacciones_dmotriz"])]
    
    if x0 >= 60:
        """Adultos de la tercera edad"""
        clust_recom_dic ={0:"Elija autenticarse por  Identifcación facial, Reconocimiento de voz o Contraseña",
                            1:"Elija autenticarse por Identifcación facial o Reconocimiento de voz",
                            2:"Elija autenticarse por  Reconocimiento de voz",
                            3:"Elija autenticarse por  Identifcación facial o Contraseña"}
    else:
        """Menores a 60 años"""
        clust_recom_dic = {0:"Elija autenticarse por Lector de Huella, Identifcación facial, Reconocimiento de voz o Contraseña",
                           1:"Elija autenticarse por Identifcación facial o Reconocimiento de voz",
                           2:"Elija autenticarse por Lector de Huella, Reconocimiento de voz",
                           3:"Elija autenticarse por Lector de Huella, Identifcación facial o Contraseña"}
    
    cl_0 = [44.9737316121285,252998.261933353,225682.447763434,3.33417372173243,3.32108783754579,5301.53032122486,1863.74226958871,5916.8706094266]
    cl_1 = [44.2728756645835,126898.820912228,252803.949818114,0.948765201619497,0.948395809117195,5937.19848894693,1496.61705997575,11662.915306408]
    cl_2 = [44.8217099221884,374598.368614373,256180.038760814,0.948722705832584,0.948471540110485,12443.3660528732,1413.21777584457,1036.16374269006]
    cl_3 = [44.7278008298755,265960.726141079,227799.122821577,1.19554498265672,1.23293858753953,8506.39336099585,335914.019917012,6609.62738589212]


    headers = {"Access-Control-Allow-Origin": "*"}
   
        
    d1 = (((cl_0[0]-x0)**2+(cl_0[1]-x1)**2+(cl_0[2]-x2)**2+(cl_0[3]-x3)**2+(cl_0[4]-x4)**2+(cl_0[5]-x5)**2+(cl_0[6]-x6)**2+(cl_0[7]-x7)**2))**(1/2)
    d2 = (((cl_1[0]-x0)**2+(cl_1[1]-x1)**2+(cl_1[2]-x2)**2+(cl_1[3]-x3)**2+(cl_1[4]-x4)**2+(cl_1[5]-x5)**2+(cl_1[6]-x6)**2+(cl_1[7]-x7)**2))**(1/2)
    d3 = (((cl_2[0]-x0)**2+(cl_2[1]-x1)**2+(cl_2[2]-x2)**2+(cl_2[3]-x3)**2+(cl_2[4]-x4)**2+(cl_2[5]-x5)**2+(cl_2[6]-x6)**2+(cl_2[7]-x7)**2))**(1/2)
    d4 = (((cl_3[0]-x0)**2+(cl_3[1]-x1)**2+(cl_3[2]-x2)**2+(cl_3[3]-x3)**2+(cl_3[4]-x4)**2+(cl_3[5]-x5)**2+(cl_3[6]-x6)**2+(cl_3[7]-x7)**2))**(1/2)
    
    lst_cl = [d1,d2,d3,d4]
    minimo = min(lst_cl)
    rcl    = lst_cl.index(minimo)
    
    resultado = {cl[rcl]:clust_recom_dic[rcl]}
    
    return {
            "statusCode": 200,
            "headers": headers,
            "body": js.dumps({
                "message": "Success",
                "results": resultado})
            }