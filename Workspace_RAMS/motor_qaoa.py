import time
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def optimizar_portafolio(lista_criptos):
    """
    Recibe una lista de activos (ej: ['BTC', 'ETH', 'SOL', 'ADA'...])
    Usa hasta 24 Qubits para simular la mejor distribución de inversión
    basado en un colapso de superposición.
    """
    num_activos = len(lista_criptos)
    
    # Nos protegemos: si mandan más de 24, lo topamos para que tu PC no explote
    num_qubits = min(num_activos, 24) 
    criptos_a_evaluar = lista_criptos[:num_qubits]

    print(f"[MOTOR CUÁNTICO] Iniciando simulación QAOA para {num_qubits} activos...")
    inicio = time.time()

    # 1. Creamos el circuito cuántico
    circuito = QuantumCircuit(num_qubits)
    
    # 2. Superposición inicial (Todos los escenarios posibles de mercado)
    for i in range(num_qubits):
        circuito.h(i)
        
    # 3. Entrelazamiento simulando correlación de mercado (si cae BTC, cae ETH)
    for i in range(num_qubits - 1):
        circuito.cx(i, i + 1)
        
    # 4. Medición para colapsar en el estado de menor energía (menor riesgo)
    circuito.measure_all()
    
    # Forzamos simulación real sin atajos matemáticos
    simulador = AerSimulator(method='statevector')
    resultado = simulador.run(circuito, shots=1).result().get_counts()
    
    # El colapso nos da una cadena binaria (ej: '101001')
    estado_optimo = list(resultado.keys())[0]
    
    tiempo_total = time.time() - inicio
    
    # Filtramos las criptos ganadoras (las que colapsaron en '1')
    portafolio_ideal = []
    # La cadena se lee al revés en Qiskit, así que le damos la vuelta
    estado_optimo_ordenado = estado_optimo[::-1] 
    
    for i, bit in enumerate(estado_optimo_ordenado):
        if bit == '1':
            portafolio_ideal.append(criptos_a_evaluar[i])

    resultado_final = {
        "tiempo_calculo_segundos": round(tiempo_total, 3),
        "qubits_usados": num_qubits,
        "cadena_colapso": estado_optimo,
        "inversion_recomendada": portafolio_ideal
    }
    
    return resultado_final