import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")    

    numbers = np.array(numbers).reshape(3,3)

    dictionary = {
        'mean': [np.mean(numbers, axis=0).tolist(), np.mean(numbers, axis=1).tolist(), np.mean(numbers).tolist()], 
        'variance': [np.var(numbers, axis=0).tolist(), np.var(numbers, axis=1).tolist(), np.var(numbers).tolist()],
        'standard deviation': [np.std(numbers, axis=0).tolist(), np.std(numbers, axis=1).tolist(), np.std(numbers).tolist()],
        'max': [np.max(numbers, axis=0).tolist(), np.max(numbers, axis=1).tolist(), np.max(numbers).tolist()],
        'min': [np.min(numbers, axis=0).tolist(), np.min(numbers, axis=1).tolist(), np.min(numbers).tolist()],
        'sum': [np.sum(numbers, axis=0).tolist(), np.sum(numbers, axis=1).tolist(), np.sum(numbers).tolist()]
    }

    return dictionary  # Retorna el diccionario con listas
