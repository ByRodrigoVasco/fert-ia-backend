'''Módulo do sensor de água — leitura via porta serial.

create_sensor_data()
Abre a porta serial configurada (PORTA/BAUD), lê linhas do sensor e grava as
leituras numéricas em data/sensor.txt. Encerra com Ctrl+C.'''

import serial
import os


# === Configuração da porta serial ===

PORTA = 'COM6'
BAUD  = 115200


# === Helper de caminho ===

def _caminho_arquivo():
    pasta_data = os.path.join(os.path.dirname(__file__), "..", "data")
    return os.path.join(pasta_data, "sensor.txt")


# === Leitura do sensor ===

def create_sensor_data():
    caminho = _caminho_arquivo()
    try:
        with serial.Serial(PORTA, BAUD, timeout=1) as ser:
            with open(caminho, 'a') as f:
                print("Lendo sensor... (Ctrl+C para voltar)")
                while True:
                    linha = ser.readline().decode().strip()
                    if linha and linha[0].isdigit():
                        f.write(linha + '\n')
                        f.flush()
                        print(" ", linha)
    except KeyboardInterrupt:
        print("\nLeitura encerrada.")
    except Exception as e:
        print(f"Erro: {e}")
