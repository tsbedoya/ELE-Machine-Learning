import os, sys, re
import pandas as pd

parameters = {
    'path': os.path.dirname(sys.path[0]),
    'path_in': 'c:\\Users\\tatia\\OneDrive - Universidad de San Buenaventura Seccional Medellin\\Universidad\\ELECTIVA MACHINE LEARNING\\ELE-Machine-Learning\\01_data',
    'path_out': os.path.join(os.path.dirname(sys.path[0]), '02_output')
}

def cargar_datos():
    proyect_name = 'poker-hand'
    datasets = {
        'testing': os.path.join(parameters['path_in'], proyect_name, 'poker-hand-training-true.data'),
        'training': os.path.join(parameters['path_in'], proyect_name, 'poker-hand-testing.data')
    }

    df_testing = pd.read_csv(datasets['testing'], header=None, names=['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS'])
    df_training = pd.read_csv(datasets['training'], header=None, names=['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS'])

    df = pd.concat([df_testing, df_training], ignore_index=True)
    return df

# Se llama a la función para obtener el DataFrame
df = cargar_datos()
