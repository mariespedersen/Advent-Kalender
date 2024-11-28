import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns

########################################
# 1. Advent
########################################
# Definér grænserne for trekanten (tre hjørner)
Koordinator = np.array([
    [0, 0],   # Nederste venstre hjørne
    [1, 0],   # Nederste højre hjørne
    [0.5, 1]  # Øverste hjørne
])


# Generer tilfældige punkter inden for trekanten
def Koordinator_funktion(vertices, num_points):
    # Brug barycentriske koordinater til at generere punkterne
    r1 = np.random.rand(num_points)
    r2 = np.random.rand(num_points)
    # Sørg for, at r1 + r2 <= 1
    mask = r1 + r2 > 1
    r1[mask] = 1 - r1[mask]
    r2[mask] = 1 - r2[mask]
    # Kombiner med hjørnerne for at finde punkterne
    points = (1 - r1 - r2).reshape(-1, 1) * vertices[0] + \
             r1.reshape(-1, 1) * vertices[1] + \
             r2.reshape(-1, 1) * vertices[2]
    return points

svar_1 = "C"

########################################
# 2. Advent
########################################
def generate_direction(row):
    # Regler baseret på feature-kombinationer
    if row["Farve"] == 1 and row["Mønster"] == 1:
        return 1  # Venstre
    elif row["Farve"] == 2 and row["Form"] == 2:
        return 2  # Midten
    elif row["Størrelse"] == 1 and row["Mønster"] == 3:
        return 3  # Højre
    else:
        return np.random.choice([1,2])  # Tilfældig retning som fallback

########################################
# 4. Advent
########################################
# Generér data for juleposer med eksponentiel fordeling for vægten
np.random.seed(42)
n_poses = 300
lambda_param = 1.0  # Rate parameter for eksponentiel fordeling

data = {
    "Farve": np.random.choice(["Rød", "Grøn", "Blå", "Gul"], size=n_poses),
    "Størrelse": np.random.choice(["Lille", "Mellem", "Stor"], size=n_poses, p=[0.6, 0.3, 0.1]),
    "Vægt": np.round(np.random.exponential(scale=lambda_param, size=n_poses), 2),  # Vægt følger eksponentiel fordeling
    "LagerX": np.random.randint(0, 100, size=n_poses),
    "LagerY": np.random.randint(0, 100, size=n_poses),
}


# Mynte's gavepose er en stor, tung rød pose
myntes_pose = pd.DataFrame({
    "Farve": ["Rød"],
    "Størrelse": ["Stor"],
    "Vægt": [30],  # Maksimal vægt
    "LagerX": [50],
    "LagerY": [50],
})

# Lav DataFrame
df = pd.DataFrame(data)

# Tilføj Mynte's gavepose til data
df = pd.concat([df, myntes_pose], ignore_index=True)

Røde_poser = df[df['Farve']=="Rød"].count()[0]
Rigtig_størrelse = myntes_pose['Størrelse'][0]
Rigtig_vægt = myntes_pose['Vægt'][0]

print("Pakker og nødvendige variabler er indlæst")