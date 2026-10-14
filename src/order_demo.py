from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# H then X
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.x(0)

state1 = Statevector.from_instruction(qc1)

print("H -> X")
print(state1)

print("\n")

# X then H
qc2 = QuantumCircuit(1)
qc2.x(0)
qc2.h(0)

state2 = Statevector.from_instruction(qc2)

print("X -> H")
print(state2)