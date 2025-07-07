Injecting Adversarial Noise (Start)
 Set up Google Colab with required libraries (`torch`, `torchvision`, `matplotlib`)
-Loaded the MNIST dataset (handwritten digits) using torchvision
- Built a **simple neural network** with:
  - Input layer: 784 neurons (28x28 pixels)
  - Hidden layer: 128 neurons
  - Output layer: 10 neurons (for digits 0–9)
- Passed a sample image through the model to generate prediction
-  Visualized the digit image and confirmed the model's guess
- Understood the internal structure of a neural network:
How images are represented as tensors
How neurons process data layer-by-layer
How final predictions are made using argmax

Also realized:
- This is **shallow learning** (1 hidden layer)
- Deep learning would have **multiple hidden layers**
- Layer sizes (128, 64, etc.) are **not division-based**, but based on experience, logic, and performance tuning
and also do some python coding on google colab which result on the making of some blurry image.if you want to check it then see the next file

