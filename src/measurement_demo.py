from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

# Circuit
qc = QuantumCircuit(1, 1)

# Hadamard Gate
qc.h(0)

# Measurement
qc.measure(0, 0)

# Simulator
simulator = AerSimulator()

compiled = transpile(qc, simulator)

job = simulator.run(compiled, shots=1000)

result = job.result()

counts = result.get_counts()

print("Measurement Results:")
print(counts)