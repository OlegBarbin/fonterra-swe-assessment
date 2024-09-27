import matplotlib.pyplot as plt
from model import run_model
# Run the model to get the pH curve
pH_curve = run_model(1, -15, 12, [10**6, 10**-6])

# Plot the results as a way to see what happens
plt.figure(figsize=(10, 6))
plt.plot(pH_curve[0], pH_curve[1], label='pH vs Time')
plt.xlabel('Time (hours)')
plt.ylabel('pH')
plt.title('pH vs Time Curve')
plt.legend()
plt.grid(True)
plt.show()
