import sys
import numpy as np
import qubogen

from scipy.optimize import minimize
from scipy.spatial.distance import pdist, squareform

from pulser.devices import DigitalAnalogDevice
from pulser import Pulse, Sequence, Register
from pulser_simulation import QutipEmulator

from joblib import Parallel, delayed

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

size = input("Taille de la matrice: ")
size = np.int32(size)

match size:
    case 2:
        l = 2
    case 3:
        l = 4
    case 4:
        l = 6
    case 5:
        l = 10
    case 6:
        l = 20
    case 7:
        l = 50
    case 8:
        l = 220  
    case 9:
        l = 450
    case _:
        print("Taille de matrice non supportée")
        sys.exit()

# Génération aléatoire de la matrice QUBO selon size
s = np.random.randint(1,12,size)
Q = qubogen.qubo_number_partition(s)

print('Matrice QUBO:\n' + str(Q))

# Calcul de la solution exacte classiquement (méthode Pasqal)
bitstrings = [np.binary_repr(i, len(Q)) for i in range(2 ** len(Q))]
costs = []
for b in bitstrings:
    z = np.array(list(b), dtype=int)
    cost = z.T @ Q @ z
    costs.append(cost)
zipped = zip(bitstrings, costs)
sort_zipped = sorted(zipped, key=lambda x: x[1])
print("Solution minimale, énergie associé" + str(sort_zipped[:l]))
indexes = sort_zipped[:l]
indexes = [item[0] for item in indexes if '0' in item[0] and '1' in item[0]]

# Création du registre atomique pour placer les qubits
# La fonction evaluate_mapping permet de trouver la position optimal des 
# atomes dans le registre et qui réplique au mieux les termes de la diagonale de Q
shape = (len(Q), 2)
costs = []
np.random.seed(0)
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


LAYERS = 2
# Création de la séquence d'impulsions
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
scores = []
params = []
for repetition in range(20):
    guess = {
        "t": np.random.uniform(1, 10, LAYERS),
        "s": np.random.uniform(1, 10, LAYERS),
    }

    try:
        res = minimize(
            func,
            args=Q,
            x0=np.r_[guess["t"], guess["s"]],
            method="Nelder-Mead",
            tol=1e-5,
            options={"maxiter": 20},
        )
        scores.append(res.fun)
        params.append(res.x)
    except Exception as e:
        pass

optimal_count_dict = quantum_loop(params[np.argmin(scores)])
# print("Solutions obtenues : tirage associé \n" + str(optimal_count_dict))
# print("Solutions attendues: \n" + str(indexes))

yes_match = {}
no_match = {}

for key in optimal_count_dict.keys():
    if key in indexes:
        yes_match[key] = optimal_count_dict[key]
    else:
        no_match[key] = optimal_count_dict[key]

sorted_match = dict(sorted(yes_match.items(), key=lambda item: item[1], reverse=True))
print("Matching keys:count", sorted_match)
print("Non-matching keys:count", no_match)

# if next(iter(optimal_count_dict)) == next(iter(sorted_match)) :
#     print("Meilleure solution trouvé !" + str(optimal_count_dict(0)))
# else:
#     print("La meilleure solution n'a pas été trouvé")