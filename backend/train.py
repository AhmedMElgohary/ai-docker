# backend/train.py
import torch
import torch.nn as nn
import torch.optim as optim

# --- 1. DEFINE THE ARCHITECTURE (Must match main.py EXACTLY) ---
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

# --- 2. THE DATA ---
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

# --- 3. INITIALIZE THE MODEL ---
# Now we use the Class, not just raw nn.Linear
model = LinearRegressionModel()

# --- 4. TRAINING LOOP ---
optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

print("Training started...")
for epoch in range(100):
    prediction = model(X)
    loss = criterion(prediction, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# --- 5. EXPORT ---
torch.save(model.state_dict(), "model_artifact.pth")
print("Training complete. New brain structure saved to 'model_artifact.pth'")