import sys
import os
import numpy as np
import qubogen

import time

from scipy.optimize import minimize
from scipy.spatial.distance import pdist, squareform

from pulser.devices import DigitalAnalogDevice
from pulser import Pulse, Sequence, Register
from pulser_simulation import QutipEmulator

from joblib import Parallel, delayed

def perform_minimization(guess, Q):
    try:
        res = minimize(
            func,
            args=Q,
            x0=np.r_[guess["t"], guess["s"]],
            method="Nelder-Mead",
            tol=1e-5,
            options={"maxiter": 30},
        )
        return res.fun, res.x
    except Exception as e:
        return None, None

def evaluate_mapping(new_coords, *args):
    """Cost function to minimize. Ideally, the pairwise
    distances are conserved"""
    Q, shape = args
    new_coords = np.reshape(new_coords, shape)
    new_Q = squareform(
        DigitalAnalogDevice.interaction_coeff / pdist(new_coords) ** 6
    )
    return np.linalg.norm(new_Q - Q)

def quantum_loop(parameters):

    params = np.array(parameters, dtype=int).reshape(2, LAYERS)
    t_params, s_params = params
    assigned_seq = seq.build(t_list=t_params, s_list=s_params)
    
    # Initialisation et exécution de la simulation
    simul = QutipEmulator.from_sequence(assigned_seq, sampling_rate=0.01)
    results = simul.run()
    
    # Échantillonnage de l'état final
    count_dict = results.sample_final_state()  # sample from the state vector
    
    return count_dict

def get_cost_colouring(bitstring, Q):
    z = np.array(list(bitstring), dtype=int)
    cost = z.T @ Q @ z
    return cost

def get_cost(counter, Q):
    cost = sum(counter[key] * get_cost_colouring(key, Q) for key in counter)
    return cost / sum(counter.values())  # Divide by total samples

def func(param, *args):
    Q = args[0]
    C = quantum_loop(param)
    cost = get_cost(C, Q)
    return cost


matrice_results = {}
minimal_results = {}

# Charger les fichiers .dat depuis le dossier "matrice"
directory = 'matrice'
for nom_fichier in os.listdir(directory):
    if nom_fichier.endswith('.dat'):
        chemin_fichier = os.path.join(directory, nom_fichier)
        data = np.loadtxt(chemin_fichier, delimiter=',', dtype='float')
        key = nom_fichier.replace('.dat', '')
        matrice_results[key] = data

# Charger les fichiers .dat depuis le dossier "minimal"
directory = 'minimal'
for nom_fichier in os.listdir(directory):
    if nom_fichier.endswith('.dat'):
        chemin_fichier = os.path.join(directory, nom_fichier)
        data = np.loadtxt(chemin_fichier, delimiter=',', dtype='float')
        key = nom_fichier.replace('.dat', '')
        minimal_results[key] = data
#####FIN CHARGEMENT#####



all_results = {}

for key, Q in {**matrice_results}.items():
    print(f"Traitement de {key}")

    #####CREATION REGISTRE QUANTIQUE#####
    shape = (len(Q), 2)
    costs = []
    np.random.seed(5)
    x0 = np.random.random(shape).flatten()
    res = minimize(
        evaluate_mapping,
        x0,
        args=(Q, shape),
        method="Nelder-Mead",
        tol=1e-6,
        options={"maxiter": 200000, "maxfev": None},
    )
    coords = np.reshape(res.x, (len(Q), 2))
    qubits = dict(enumerate(coords))
    reg = Register(qubits)

    #####CREATION DE LA SEQUENCE D'IMPULSION#####
    LAYERS = 2
    seq = Sequence(reg, DigitalAnalogDevice)
    seq.declare_channel("ch0", "rydberg_global")

    t_list = seq.declare_variable("t_list", size=LAYERS)
    s_list = seq.declare_variable("s_list", size=LAYERS)

    for t, s in zip(t_list, s_list):
        pulse_1 = Pulse.ConstantPulse(1000 * t, 1.0, 0.0, 0)
        pulse_2 = Pulse.ConstantPulse(1000 * s, 0.0, 1.0, 0)

        seq.add(pulse_1, "ch0")
        seq.add(pulse_2, "ch0")

    seq.measure("ground-rydberg")

    np.random.seed() #seed randomizer
    guess = {
        "t": np.random.uniform(8, 10, LAYERS),
        "s": np.random.uniform(1, 3, LAYERS),
    }

    example_dict = quantum_loop(np.r_[guess["t"], guess["s"]])

    print("Entrée dans la minimisation, cela peut prendre du temps (< 3 minutes)")

    n_jobs = 1
    start = time.time()
    results = Parallel(n_jobs=n_jobs)(
        delayed(perform_minimization)(
            {"t": np.random.uniform(1, 10, LAYERS), "s": np.random.uniform(1, 10, LAYERS)},
            Q
        ) for _ in range(20)
    )

    end = time.time()

    print(f"Temps d'exécution: {end - start} secondes")

    results = [(score, param) for score, param in results if score is not None]

    scores, params = zip(*results)

    optimal_count_dict = quantum_loop(params[np.argmin(scores)])
    all_results[key] = optimal_count_dict

