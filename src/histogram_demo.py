from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)

qc.h(0)

qc.measure(0, 0)

sim = AerSimulator()

compiled = transpile(qc, sim)

job = sim.run(compiled, shots=1000)

result = job.result()

counts = result.get_counts()

print(counts)

fig = plot_histogram(counts)

fig.savefig("images/histogram.png")

plt.show()