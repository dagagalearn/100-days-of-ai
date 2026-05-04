import torch
from torchvision import datasets, transforms
from torch import optim,nn
from torch.utils.data import DataLoader

data = datasets.FashionMNIST(".",train=True,download=True,transform=transforms.ToTensor())
loader = DataLoader(data,batch_size=64,shuffle=True)

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28*28,100),
    nn.ReLU(),
    nn.Linear(100,10)
)

optimizer = optim.Adam(params=model.parameters())
loss_fun = nn.CrossEntropyLoss()
for epochs in range(3):
    for images,labels in loader:
        preds = model(images)
        loss = loss_fun(preds,labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"\n\tEpoch {epochs+1}\n\tLoss {loss}")
