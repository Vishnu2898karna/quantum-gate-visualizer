from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
    plot_bloch_multivector,
    plot_histogram
)
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

print("=" * 50)
print("INTERACTIVE QUANTUM CIRCUIT BUILDER")
print("=" * 50)

print("\nAvailable Gates:")
print("X Y Z H")

gate_input = input(
    "\nEnter gates separated by spaces (Example: H X Z): "
)

gates = gate_input.upper().split()

# Create circuit
qc = QuantumCircuit(1)

# Apply gates
for gate in gates:

    if gate == "X":
        qc.x(0)

    elif gate == "Y":
        qc.y(0)

    elif gate == "Z":
        qc.z(0)

    elif gate == "H":
        qc.h(0)

    else:
        print(f"Skipping invalid gate: {gate}")

print("\nGenerated Circuit:")
print(qc)

# Statevector
state = Statevector.from_instruction(qc)

print("\nFinal Statevector:")
print(state)

# Save circuit image
circuit_fig = qc.draw(output="mpl")
circuit_fig.savefig("images/custom_circuit.png")
plt.close(circuit_fig)

# Save Bloch sphere
bloch_fig = plot_bloch_multivector(state)
bloch_fig.savefig("images/custom_bloch.png")
plt.close(bloch_fig)

# -----------------------
# Measurement Section
# -----------------------

measure_qc = qc.copy()

measure_qc.add_register(
    QuantumCircuit(1, 1).cregs[0]
)

measure_qc.measure(0, 0)

simulator = AerSimulator()

compiled = transpile(
    measure_qc,
    simulator
)

job = simulator.run(
    compiled,
    shots=1000
)

result = job.result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

# Histogram
hist_fig = plot_histogram(counts)

hist_fig.savefig(
    "images/custom_histogram.png"
)

plt.close(hist_fig)

print("\nSaved Files:")
print("images/custom_circuit.png")
print("images/custom_bloch.png")
print("images/custom_histogram.png")