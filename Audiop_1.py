import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Parámetros
frecuencia = 440
fs = 44100
duracion = 1
amplitud = 0.1

# Duración de la onda
t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)
onda_seno = amplitud * np.sin(2 * np.pi * frecuencia * t)

# Parámetros de la envolvente ADSR
attack_time = 0.1  # tiempo de ataque en segundos
decay_time = 0.1   # tiempo de decaimiento en segundos
sustain_level = 0.7  # nivel de sustain (relativo a la amplitud máxima)
sustain_time = 0.6  # tiempo de sustain en segundos
release_time = 0.2  # tiempo de liberación en segundos

# Crear envolvente ADSR
envolvente = np.zeros_like(t)

# Attack
attack_samples = int(attack_time * fs)
envolvente[:attack_samples] = np.linspace(0, 1, attack_samples)

# Decay
decay_samples = int(decay_time * fs)
envolvente[attack_samples:attack_samples + decay_samples] = np.linspace(1, sustain_level, decay_samples)

# Sustain
sustain_samples = int(sustain_time * fs)
envolvente[attack_samples + decay_samples:attack_samples + decay_samples + sustain_samples] = sustain_level

# Release
release_samples = int(release_time * fs)
envolvente[attack_samples + decay_samples + sustain_samples:] = np.linspace(sustain_level, 0, release_samples)

# Asegurar que la longitud de la envolvente sea correcta
envolvente = envolvente[:len(t)]

# Onda senoidal con envolvente aplicada
onda_envolvente = onda_seno * envolvente

# Reproducir el sonido con envolvente
sd.play(onda_envolvente, fs)
sd.wait()

# Graficar la onda y su envolvente
plt.figure(figsize=(10, 4))
plt.plot(t, onda_envolvente, label='Onda con Envolvente')
plt.plot(t, envolvente, label='Envolvente ADSR', linestyle='--')
plt.title(f'Onda Senoidal con Envolvente ADSR - {frecuencia} Hz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()







