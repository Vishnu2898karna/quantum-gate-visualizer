from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import os

# images folder create if not exists
os.makedirs("images", exist_ok=True)


def visualize_gate(gate_name):

    qc = QuantumCircuit(1)

    if gate_name == "X":
        qc.x(0)

    elif gate_name == "Y":
        qc.y(0)

    elif gate_name == "Z":
        qc.z(0)

    elif gate_name == "H":
        qc.h(0)

    else:
        print("Invalid Gate!")
        return

    print(f"\n===== {gate_name} Gate =====")

    state = Statevector.from_instruction(qc)

    print("\nCircuit:")
    print(qc)

    print("\nStatevector:")
    print(state)

    # Save Circuit Diagram
    circuit_fig = qc.draw(output="mpl")
    circuit_fig.savefig(f"images/{gate_name}_circuit.png")
    plt.close(circuit_fig)

    # Save Bloch Sphere
    bloch_fig = plot_bloch_multivector(state)
    bloch_fig.savefig(f"images/{gate_name}_bloch.png")
    plt.close(bloch_fig)

    print(f"\nSaved:")
    print(f"images/{gate_name}_circuit.png")
    print(f"images/{gate_name}_bloch.png")


print("\nQuantum Gate Visualizer")
print("-----------------------")
print("Available Gates: X, Y, Z, H")

gate = input("\nEnter Gate: ").upper()

visualize_gate(gate)

