from qiskit import IBMQ
import qiskit
IBMQ.save_account('4db1f51f9ff428e7c2ed755e17189c47b3ec25d001d9d91e6eca47960a0bb4b06a6ee5c2ff3f5d70411f5fe3691b168d770bb003757ce2fab8901bf745760665')

qiskit.__qiskit_version__
import numpy as np
from qiskit import(QuantumCircuit,execute,Aer)
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=2000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
# Draw the circuit
circuit.draw()

plot_histogram(counts)

#just check
